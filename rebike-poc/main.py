"""
FACOM ReBike - POC (niveau A : vision)
=======================================

Demontre le reemploi du FACOM SCANDIAG(R) DX.TSCANPB comme controleur d'usure
de pneus de mobilite douce (velo / trottinette).

Principe : l'outil projette une LIGNE laser sur la bande de roulement ; une
camera decalee d'un angle connu observe la DEFORMATION de cette ligne. La
"chute" de la ligne dans une rainure, convertie par un facteur de calibration
(mm/pixel), donne la PROFONDEUR de la rainure -> verdict d'usure.

C'est exactement la chaine de mesure native du SCANDIAG (triangulation laser),
ici reproduite cote logiciel SANS dependre du firmware proprietaire.

Usage :
    python main.py                      # mode demo : genere 3 cas + rapport
    python main.py photo.jpg            # analyse une vraie photo de ligne laser
    python main.py photo.jpg --calibration 0.05   # mm par pixel

Dependances : numpy, pillow
"""

from __future__ import annotations

import argparse
import os

import numpy as np
from PIL import Image

# --- Seuils d'usure pour la mobilite douce (valeurs de demonstration) ---------
SEUIL_CONFORME = 3.0      # mm : >= 3 mm -> bon etat
SEUIL_SURVEILLANCE = 1.5  # mm : entre 1,5 et 3 mm -> a surveiller

# Calibration par defaut (mm par pixel). En conditions reelles, ce facteur
# s'obtient en mesurant l'adaptateur de verification (geometrie connue).
MM_PAR_PIXEL = 0.05


# --- 1. Extraction du profil laser -------------------------------------------
def extraire_profil_laser(img: np.ndarray) -> np.ndarray:
    """Renvoie, pour chaque colonne, la position verticale (en pixels) de la
    ligne laser verte, estimee au sous-pixel par centroide pondere.

    img : tableau RGB (H, W, 3), uint8.
    Retour : tableau (W,) de float, NaN la ou aucun laser n'est detecte.
    """
    img = img.astype(np.float64)
    # On isole le vert (laser 510-530 nm) en retranchant le rouge et le bleu.
    score = img[:, :, 1] - 0.5 * (img[:, :, 0] + img[:, :, 2])
    score = np.clip(score, 0, None)

    hauteur, largeur = score.shape
    seuil = score.max() * 0.5 if score.max() > 0 else 0.0
    lignes = np.arange(hauteur)[:, None]

    profil = np.full(largeur, np.nan)
    for x in range(largeur):
        col = score[:, x]
        masque = col > seuil
        if masque.any():
            poids = col[masque]
            profil[x] = float((lignes[masque, 0] * poids).sum() / poids.sum())
    return profil


# --- 2. Mesure de la profondeur ----------------------------------------------
def mesurer_profondeur_mm(profil_px: np.ndarray, mm_par_px: float) -> float | None:
    """Profondeur = ecart entre la surface (ligne sur la bande) et le fond de la
    rainure. En coordonnees image, y augmente vers le bas : la surface est la
    valeur dominante (mediane), le fond de rainure est la valeur la plus basse
    (grand y, estime de facon robuste au 98e percentile)."""
    valides = profil_px[~np.isnan(profil_px)]
    if valides.size < 10:
        return None
    surface = np.median(valides)          # niveau de la bande de roulement
    fond = np.percentile(valides, 98)     # fond de rainure (robuste au bruit)
    profondeur_px = max(fond - surface, 0.0)
    return profondeur_px * mm_par_px


# --- 3. Verdict d'usure ------------------------------------------------------
def verdict(profondeur_mm: float | None) -> tuple[str, str, str]:
    """Renvoie (etat, couleur, recommandation)."""
    if profondeur_mm is None:
        return ("MESURE INVALIDE", "Gris",
                "Laser non detecte : repositionner l'outil et recommencer.")
    if profondeur_mm >= SEUIL_CONFORME:
        return ("CONFORME", "Vert",
                "Le pneu peut continuer a etre utilise.")
    if profondeur_mm >= SEUIL_SURVEILLANCE:
        return ("A SURVEILLER", "Orange",
                "Le pneu reste utilisable mais doit etre recontrole prochainement.")
    return ("A REMPLACER", "Rouge",
            "Usure trop importante : remplacer le pneu (securite).")


# --- 4. Rapport --------------------------------------------------------------
def construire_rapport(objet: str, profondeur_mm: float | None,
                       operateur: str = "[Nom]", date: str = "[Date]") -> str:
    etat, couleur, reco = verdict(profondeur_mm)
    mesure = "n/a" if profondeur_mm is None else f"{profondeur_mm:.2f} mm"
    return (
        "Rapport FACOM ReBike\n"
        f"Objet controle   : {objet}\n"
        f"Profondeur mesuree : {mesure}\n"
        f"Etat             : {etat}\n"
        f"Indicateur       : {couleur}\n"
        f"Recommandation   : {reco}\n"
        f"Operateur        : {operateur}    Date : {date}\n"
    )


# --- Outils de demonstration -------------------------------------------------
def generer_image_synthetique(profondeur_px: float, largeur: int = 640,
                              hauteur: int = 480, y0: int = 180,
                              rainure: tuple[int, int] = (260, 380),
                              epaisseur: float = 3.0, graine: int = 0) -> np.ndarray:
    """Cree une image de test : une ligne laser verte sur fond sombre (caoutchouc),
    qui plonge de `profondeur_px` pixels dans une rainure. Sert a valider la
    chaine de traitement en l'absence de photo reelle."""
    rng = np.random.default_rng(graine)
    img = rng.integers(18, 42, (hauteur, largeur, 3)).astype(np.float64)  # bruit fond

    centres = np.full(largeur, float(y0))
    a, b = rainure
    centres[a:b] = y0 + profondeur_px  # la ligne descend dans la rainure

    lignes = np.arange(hauteur)[:, None]
    halo = np.exp(-((lignes - centres[None, :]) ** 2) / (2 * epaisseur ** 2))  # (H,W)
    img[:, :, 1] += halo * 230        # vert : la ligne laser
    img[:, :, 0] += halo * 35         # leger bloom
    img[:, :, 2] += halo * 35
    img += rng.normal(0, 4, img.shape)  # bruit capteur
    return np.clip(img, 0, 255).astype(np.uint8)


def analyser_image(img: np.ndarray, mm_par_px: float) -> float | None:
    return mesurer_profondeur_mm(extraire_profil_laser(img), mm_par_px)


def mode_demo(dossier: str) -> None:
    """Genere 3 cas (bon / use / hors-service), les analyse, ecrit un rapport."""
    dossier_img = os.path.join(dossier, "images")
    os.makedirs(dossier_img, exist_ok=True)

    cas = [
        ("pneu de velo - rainure profonde", 70, "conforme"),
        ("pneu de velo - rainure moyenne", 48, "surveiller"),
        ("pneu de trottinette - rainure faible", 24, "remplacer"),
    ]

    print("=" * 60)
    print("FACOM ReBike - POC (niveau A : mesure par triangulation laser)")
    print("=" * 60)

    lignes_rapport = []
    for objet, prof_px, tag in cas:
        img = generer_image_synthetique(prof_px, graine=prof_px)
        chemin = os.path.join(dossier_img, f"synth_{tag}.png")
        Image.fromarray(img, "RGB").save(chemin)

        profondeur = analyser_image(img, MM_PAR_PIXEL)
        etat, couleur, _ = verdict(profondeur)
        print(f"\n[{objet}]")
        print(f"  image       : {os.path.relpath(chemin, dossier)}")
        print(f"  profondeur  : {profondeur:.2f} mm")
        print(f"  etat        : {etat} ({couleur})")
        lignes_rapport.append(construire_rapport(objet, profondeur))

    chemin_rapport = os.path.join(dossier, "rapport_exemple.txt")
    with open(chemin_rapport, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes_rapport))
    print(f"\nRapport ecrit : {os.path.relpath(chemin_rapport, dossier)}")
    print("=" * 60)


def main() -> None:
    p = argparse.ArgumentParser(description="FACOM ReBike - POC mesure d'usure de pneu")
    p.add_argument("image", nargs="?", help="photo de la ligne laser (sinon : mode demo)")
    p.add_argument("--calibration", type=float, default=MM_PAR_PIXEL,
                   help="facteur mm par pixel (defaut : %(default)s)")
    p.add_argument("--objet", default="pneu", help="libelle de l'objet controle")
    args = p.parse_args()

    dossier = os.path.dirname(os.path.abspath(__file__))

    if args.image is None:
        mode_demo(dossier)
        return

    img = np.asarray(Image.open(args.image).convert("RGB"))
    profondeur = analyser_image(img, args.calibration)
    print(construire_rapport(args.objet, profondeur))


if __name__ == "__main__":
    main()
