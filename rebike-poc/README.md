# FACOM ReBike — POC (niveau A : vision)

Preuve de concept du réemploi du **FACOM SCANDIAG® DX.TSCANPB** en contrôleur
d'usure de pneus de mobilité douce (vélo / trottinette).

## Idée

Le SCANDIAG mesure une profondeur par **triangulation laser** : il projette une
ligne laser sur la surface, une caméra décalée observe la déformation de cette
ligne, et la géométrie en déduit un profil. Ce POC **reproduit cette chaîne
côté logiciel**, à partir d'une image de la ligne laser — donc **sans dépendre
du firmware propriétaire** de l'outil.

```
Image ligne laser → extraction du profil → profondeur (mm) → verdict d'usure
```

## Prérequis

```bash
pip install numpy pillow
```

## Utilisation

```bash
# Mode démo : génère 3 cas de test, les analyse et écrit un rapport
python main.py

# Analyse d'une vraie photo de ligne laser projetée sur un pneu
python main.py photo.jpg --calibration 0.05 --objet "pneu velo"
```

Le facteur `--calibration` (mm par pixel) s'obtient en conditions réelles en
mesurant l'**adaptateur de vérification** fourni avec le SCANDIAG (géométrie
connue) — c'est sa fonction d'origine de calibration.

## Seuils (mobilité douce, valeurs de démonstration)

| Profondeur | État | Couleur |
|---:|---|---|
| ≥ 3 mm | Conforme | 🟢 Vert |
| 1,5 – 3 mm | À surveiller | 🟠 Orange |
| < 1,5 mm | À remplacer | 🔴 Rouge |

## Fonctions

| Fonction | Rôle |
|---|---|
| `extraire_profil_laser(img)` | Position sous-pixel de la ligne laser par colonne |
| `mesurer_profondeur_mm(profil, mm_px)` | Convertit le profil en profondeur réelle |
| `verdict(profondeur)` | Classe l'usure (conforme / à surveiller / à remplacer) |
| `construire_rapport(...)` | Génère un rapport texte |
| `generer_image_synthetique(...)` | Crée une image de test (mode démo) |

## Contenu

```
rebike-poc/
├── main.py              # pipeline complet + mode démo
├── README.md           # ce fichier
├── rapport_exemple.txt # rapports générés par le mode démo
└── images/             # images de test générées (ligne laser + rainure)
```

## Limites et extensions

- En l'absence de photo réelle, le POC tourne sur des **images synthétiques**
  (ligne laser + rainure) qui valident la chaîne de traitement.
- **Niveau B** (Bluetooth) : réutiliser l'acquisition du logiciel SCANDIAG sur un
  pneu vélo.
- **Niveau C** (carte) : firmware alternatif — nécessiterait l'ouverture du produit
  (hors périmètre de ce rendu).
