# Concours National Informatique — Dossier de réemploi RSE

## FACOM SCANDIAG® DX.TSCANPB — Projet **ReBike** (verticale du concept **ReScan**)

---

### Présentation de l'équipe

- **Campus :** [Ville] Ynov Campus
- **Classe :** [B3 / M1 / M2]

| Nom / Prénom | Classe | Rôle |
|---|---|---|
| Stoffelbach Théo | [Classe] | Chef de projet / coordination |
| Remery Lucas | [Classe] | Rétro-ingénierie fonctionnelle |
| Detres Florent | [Classe] | Recherche documentaire |
| Breton Swann | [Classe] | Développement POC |
| Abadie Thomas | [Classe] | Documentation / rendu |

---

## Résumé exécutif

Le **FACOM SCANDIAG® DX.TSCANPB** est un instrument de mesure optique portable : il projette une ligne laser sur une surface et la photographie avec une micro-caméra pour en déduire un profil d'usure (disques de frein, bande de roulement). Le principe physique sous-jacent est la **triangulation laser** (lumière structurée) — une brique réutilisable bien au-delà de l'automobile.

Le produit n'étant plus commercialisé, nous proposons de **conserver son architecture complète** (laser, caméra, batterie, Bluetooth, boîtier, mallette) et de **détourner son usage** vers d'autres contrôles d'usure.

- **Vision (ReScan) :** une jauge optique multi-usages (mobilité douce, EPI, caoutchouc industriel, pédagogie).
- **Concept retenu pour ce rendu (ReBike) :** contrôle d'usure des pneus de **vélos, vélos-cargo et trottinettes électriques**, marché en forte croissance et techniquement le plus fidèle à l'outil d'origine.

Taux de réemploi estimé : **~85 %**. Double gain RSE : on évite la mise au rebut du SCANDIAG®, et on prolonge la durée de vie des objets qu'il contrôle.

> **Note de méthode :** nous avons fait le choix de **ne pas ouvrir le produit**. L'approche de réemploi retenue (POC « niveau A », par vision) reproduit la chaîne de mesure **côté logiciel, sans toucher au firmware** : l'ouverture n'est donc pas nécessaire pour la démonstration. Le dossier distingue ce qui est **vérifié** (notice constructeur + observation du kit) de ce qui ne serait accessible qu'après démontage (références exactes des puces) — ce dernier point étant hors périmètre du concept choisi.

---

## 1. Présentation du produit

Le kit se présente dans une mallette rigide FACOM. Référence produit relevée sur l'étiquette : **DX.TSCANPB** (code-barres `3 662420 415668`), libellé *« SCANDIAG POUR DISQUES ET PNEUS »*. L'appareil principal porte le marquage **DX.TSCAN-1**.

| Mallette fermée (étiquette produit) | Mallette ouverte | Kit complet |
|---|---|---|
| ![Étiquette DX.TSCANPB](images_facom/image-1782716335617.jpg) | ![Mallette ouverte](images_facom/image-1782716329368.jpg) | ![Kit complet](images_facom/image-1782716346312.jpg) |

**Contenu observé du kit** (photo de droite) : l'appareil SCANDIAG® dans sa mousse, le chargeur secteur, la clé USB (logiciel + documentation), l'adaptateur magnétique circulaire de vérification, et la notice (pictogrammes de danger laser visibles). L'appareil est portable, ergonomique, robuste, et muni d'un bouton de commande unique (marqué **MEASURE**) et d'une zone optique à son extrémité.

**Mise en situation — chaîne de mesure.** L'appareil (version **DX.TSCAN-1**) monté sur l'adaptateur de vérification magnétique, **relié en USB au PC** : c'est la configuration de calibration / d'acquisition.

![Appareil DX.TSCAN-1 sur adaptateur de vérification, relié au PC](images_facom/20260629_093647.jpg)

---

## 2. Caractéristiques techniques

*Source : notice constructeur (tableau « Caractéristiques techniques »).*

| Élément | Donnée |
|---|---|
| Produit | FACOM SCANDIAG® DX.TSCANPB |
| Fonction d'origine | Analyseur de disques de frein et de pneus |
| Alimentation externe (chargeur) | 100 / 240 V AC |
| Sortie chargeur | 5 V / 1,2 A — USB Mini-B |
| Entrée de l'outil | 5 V / 0,5 A |
| Batterie interne | Li-Ion, 0,620 Ah, 3,7 V |
| Classe laser | 3R |
| Puissance laser | > 5 mW |
| Longueur d'onde | 510 – 530 nm (vert) |
| Micro-caméra | CMOS WXGA, 1 mégapixel, 30 fps |
| Communication | Bluetooth® intégré, 2400 – 2483,5 MHz, 0 dBm |
| Interface utilisateur | Bouton poussoir + LED RVB |
| Température fonctionnement / stockage | 0 – 40 °C / −20 – 60 °C |
| Humidité | 10 – 80 %, sans condensation |
| Poids | 90 g (outil), 10 g (adaptateur) |

> ⚠️ La notice contient une ligne OCR ambiguë (« Longueur d'onde m/s 10 »), probablement une **vitesse ou durée de balayage de ~10 ms/(m·s)**. Nous ne l'affirmons pas faute de source fiable — à confirmer dans la documentation FACOM officielle.

---

## 3. Phase 1 — Rétro-ingénierie

### 3.1 Composants externes identifiés (notice)

| Repère | Élément | Fonction |
|---:|---|---|
| 1 | Bouton multifonction + LED multicolore | Marche/arrêt, déclenchement mesure, retour d'état |
| 2 | Connecteur USB | Recharge de la batterie interne |
| 3 | Diode laser | Projection de la ligne de mesure |
| 4 | Micro-caméra | Capture de l'image projetée |
| 5 | Aimant | Maintien / positionnement |
| 6 | Adaptateur analyse pneus | Positionnement sur pneu |
| 7 | Adaptateur vérification | Calibration / contrôle périodique |
| 8 / 9 | Câble / chargeur USB | Alimentation |
| 14 | Code date | Année de fabrication |

### 3.2 Fonctions internes (déduites de la notice, sans ouverture)

**Choix assumé : nous n'ouvrons pas le produit.** La rétro-ingénierie est ici **fonctionnelle** : on identifie les blocs et leur rôle à partir de la notice et du comportement de l'outil, sans relever les références physiques des puces. Ce niveau est **suffisant pour le concept retenu** (réemploi par vision, sans firmware — cf. §8).

| Bloc fonctionnel | Rôle déduit | Source |
|---|---|---|
| MCU / SoC | Pilotage, acquisition, gestion Bluetooth | Comportement + IHM |
| Module Bluetooth | Liaison sans fil avec le logiciel SCANDIAG | Notice (2400–2483,5 MHz) |
| Capteur caméra CMOS | Acquisition de l'image laser | Notice (CMOS WXGA 1 MP, 30 fps) |
| Driver + diode laser | Projection ligne 510–530 nm, classe 3R | Notice |
| Batterie + circuit de charge | Autonomie, recharge via USB 5 V | Notice (Li-Ion 3,7 V) |
| Régulation / DC-DC | Conversion d'alimentation interne | Architecture standard |
| IHM (bouton + LED RVB) | Commande et retour d'état | Notice + photo (bouton MEASURE) |

> **Si une ouverture devait avoir lieu plus tard** (hors périmètre de ce rendu), il faudrait relever les références sérigraphiées sur la carte (recto/verso, lumière rasante), télécharger les datasheets correspondantes, et chercher d'éventuels points UART/SWD/JTAG pour évaluer la faisabilité d'un firmware alternatif. Cela reste une **piste d'extension** (niveau C, §8.2), pas un prérequis.

### 3.3 Schéma fonctionnel du produit

```mermaid
flowchart LR
  USB[USB Mini-B 5V] --> CHG[Charge Li-Ion]
  CHG --> BAT[Batterie 3,7V]
  BAT --> PWR[Régulation / DC-DC]
  PWR --> MCU[MCU principal]
  BTN[Bouton multifonction] --> MCU
  MCU --> LED[LED RVB]
  MCU --> DRV[Driver laser] --> LASER[Diode laser 510-530 nm]
  CAM[Capteur CMOS 1 MP] --> MCU
  MCU <--> BT[Module Bluetooth]
  BT -. sans fil .-> PC[Logiciel SCANDIAG / PC]
```

### 3.4 Chaîne de mesure : la triangulation laser

C'est le point clé pour le réemploi. La diode projette une **ligne** sur la surface ; la caméra, décalée d'un angle connu, observe la **déformation** de cette ligne. La géométrie (triangulation) convertit cette déformation en **profil de profondeur**. C'est exactement la même physique qu'un scanner 3D à lumière structurée — d'où la généralisation possible à tout objet présentant des rainures ou un relief.

```mermaid
flowchart LR
  P[Positionnement] --> L[Activation laser]
  L --> C[Capture caméra]
  C --> T[Transmission Bluetooth]
  T --> S[Traitement logiciel]
  S --> R[Classement de l'usure]
  R --> O[Rapport / affichage couleur]
```

---

## 4. Sécurité

**Risques :** faisceau laser classe 3R (lésion oculaire), batterie Li-Ion (court-circuit, échauffement, >130 °C = explosion), choc électrique à la recharge, fragilité caméra/lentilles.

**Règles pendant le TP :**
- Ne jamais regarder le faisceau ni le pointer vers une personne ; pas d'instrument optique pour l'observer.
- N'activer le laser qu'une fois l'outil correctement positionné.
- Ne pas court-circuiter / percer / chauffer la batterie ; charge entre 4 °C et 40 °C uniquement.
- Pas d'usage en milieu humide ni près de liquides/gaz inflammables.
- Toute pièce démontée reste dans la zone de travail (RSE).

---

## 5. Phase 2 — Champ des possibles

### 5.1 Fonctions matérielles réutilisables

| Fonction | Réemploi | Intérêt |
|---|---|---|
| Laser 510–530 nm | Mesure optique, repère, profil | Très élevé |
| Caméra CMOS 1 MP | Capture, analyse visuelle, relief | Très élevé |
| Bluetooth intégré | Transmission PC/app | Élevé |
| Batterie Li-Ion | Autonomie portable | Élevé |
| Bouton + LED RVB | Déclenchement + retour d'état | Élevé |
| Boîtier ergonomique | Outil portable prêt à l'emploi | Très élevé |
| Adaptateurs + aimant | Positionnement / calibration | Élevé |
| Mallette | Kit pro / pédagogique | Très élevé |

### 5.2 Ajouts possibles

| Ajout | Fonction | Connexion |
|---|---|---|
| Application mobile | Affichage / historique | Bluetooth |
| Interface PC dédiée | Rapport de contrôle | Bluetooth / COM |
| Écran OLED | Affichage autonome (sans PC) | I²C / SPI (selon accès carte) |
| Buzzer | Signal conforme / non conforme | GPIO (selon accès carte) |
| Supports imprimés 3D | Adaptation à d'autres objets | Mécanique |
| Algorithme de vision | Mesure automatique du profil | Logiciel |

### 5.3 Limites

| Limite | Conséquence |
|---|---|
| Firmware propriétaire | Reprogrammation incertaine (contournée par l'approche vision) |
| Accès données caméra non garanti | Traitement direct difficile |
| Caméra calibrée pneus/disques | Recalibrage pour nouveaux usages |
| Dépendance logiciel SCANDIAG | Limite l'usage autonome |
| USB surtout dédié à la charge | Communication USB non garantie |
| Laser 3R | Cadre de sécurité strict |

---

## 6. Phase 3 — Idéation

| # | Concept | Description courte | Valeur | Difficulté | Réemploi | RSE |
|---|---|---|---:|---:|---:|---:|
| 1 | **ReScan** | Jauge optique portable multi-usages (vision) | 9/10 | 6/10 | 85 % | 9/10 |
| 2 | **ReBike** | Contrôle d'usure pneus vélo / trottinette | 8/10 | 5/10 | 80 % | 8/10 |
| 3 | SafeStep | Contrôle d'usure semelles EPI | 7/10 | 6/10 | 75 % | 8/10 |
| 4 | Kit pédagogique IoT | Support de TP rétro-ingénierie / vision | 7/10 | 4/10 | 90 % | 7/10 |
| 5 | Inspecteur caoutchouc | Bandes transporteuses / surfaces planes | 8/10 | 7/10 | 75 % | 8/10 |

ReScan est la **vision** (la plus ambitieuse), mais une vision n'est démontrable que par une **première verticale concrète**. La question décisive est donc : **ReScan (large) ou ReBike (focalisé) pour ce rendu et son POC ?**

---

## 7. Concept retenu — analyse ReScan vs ReBike

### 7.1 Matrice de décision

Pondération alignée sur les **critères de sélection FACOM** (idéation, faisabilité, aboutissement du POC, qualité/lisibilité du livrable).

| Critère (pondération) | ReScan (plateforme large) | ReBike (verticale focalisée) |
|---|---|---|
| **Faisabilité du POC en 7 h** (×3) | Faible — exige plusieurs profils de calibration et objets très différents → dispersion | **Forte** — un seul objet type, géométrie proche du pneu auto d'origine |
| **Fidélité à la techno d'origine** (×2) | Moyenne — usages parfois éloignés (semelles, bandes) | **Très forte** — même mesure de bande de roulement, plus petite |
| **Clarté du marché / pertinence RSE** (×2) | Diffuse — « un peu pour tout » | **Nette** — ateliers vélo/trottinette, sécurité mobilité douce |
| **Crédibilité industrielle** (×2) | Risque « couteau suisse » difficile à valider | **Produit identifiable**, argumentaire net |
| **Ambition / potentiel** (×1) | **Très élevée** — plateforme évolutive | Élevée, mais plus étroite |
| **Taux de réemploi** (×1) | 85 % | 80 % |

**Lecture :** ReScan gagne sur l'ambition, ReBike gagne sur **tout ce qui est noté le plus lourdement** : faisabilité, fidélité technique, clarté, crédibilité. Pour un livrable lu par un industriel et un POC à produire en temps contraint, le focus l'emporte.

### 7.2 Décision : **ReBike**, première verticale de la vision ReScan

On ne sacrifie pas l'ambition : **ReBike est le produit, ReScan est la feuille de route.** On démontre une chose, parfaitement, puis on montre comment elle s'étend (SafeStep, caoutchouc industriel, pédagogie). C'est la stratégie « land & expand », la plus convaincante face à un partenaire industriel.

### 7.3 ReBike — description

Réemploi du SCANDIAG® comme **contrôleur d'usure de pneus de mobilité douce** (vélo, vélo-cargo, trottinette, scooter). L'outil mesure la profondeur des rainures de la bande de roulement et classe l'état : **conforme / à surveiller / à remplacer**.

| Domaine | Objet contrôlé | Objectif |
|---|---|---|
| Mobilité douce | Pneu vélo / trottinette | Vérifier la profondeur des rainures |
| Sécurité | Usure critique | Détecter un pneu dangereux (adhérence) |
| Maintenance atelier | Suivi client | Historique et traçabilité des contrôles |

**Pourquoi c'est crédible :** mesurer la profondeur de bande de roulement est **déjà une fonction native** du SCANDIAG® ; on ne change que la taille de l'objet et les seuils. Le risque technique est minimal.

**Ajouts nécessaires :** gabarit/support imprimé 3D pour pneus fins, seuils adaptés (vélo/trottinette), interface de classement simple.

**Intérêt RSE (double) :** éviter la mise au rebut du SCANDIAG® **et** sécuriser/prolonger la vie des pneus de mobilité douce (secteur en plein essor, enjeu sécurité réel).

---

## 8. Phase 4 — Preuve de concept (ReBike)

### 8.1 Objectif

Démontrer qu'à partir d'une image de **ligne laser projetée sur une rainure de pneu**, on peut **mesurer une profondeur** et en **déduire un verdict d'usure** — c'est-à-dire reproduire, en réemploi, la chaîne de mesure du SCANDIAG®.

### 8.2 Trois niveaux de POC (selon l'accès matériel obtenu)

| Niveau | Pré-requis | Démonstration |
|---|---|---|
| **A — Vision (retenu, implémenté)** | Une image de la ligne laser | Traitement d'image → profil → profondeur → verdict |
| **B — Bluetooth** | Connexion logiciel SCANDIAG OK | Réutiliser la chaîne d'acquisition existante sur un pneu vélo |
| **C — Carte** | Ouverture + points de debug | UART/SWD identifiés, faisabilité firmware alternatif |

Le **niveau A est celui que nous avons développé et qui s'exécute** : il prouve le principe **sans dépendre du firmware propriétaire** ni ouvrir le produit. Les niveaux B et C sont des extensions documentées.

### 8.3 Principe du niveau A (triangulation appliquée)

1. Acquérir une image de la ligne laser projetée perpendiculairement à une rainure.
2. Isoler la ligne sur le **canal vert** (laser 510–530 nm) en retranchant rouge et bleu.
3. Pour chaque colonne, estimer la position du laser **au sous-pixel** (centroïde pondéré) → **profil** de la surface.
4. Mesurer la « chute » du profil dans la rainure et la convertir par un **facteur de calibration** (mm/pixel, obtenu via l'adaptateur de vérification) → **profondeur**.
5. Classer selon les seuils et générer un rapport.

Le code complet et exécutable se trouve dans [`rebike-poc/`](rebike-poc/) (`main.py`, ~150 lignes, dépendances : `numpy`, `pillow`). Extrait des fonctions clés :

```python
def extraire_profil_laser(img):
    """Position sous-pixel de la ligne laser par colonne (centroïde pondéré)."""
    img = img.astype(float)
    score = img[:, :, 1] - 0.5 * (img[:, :, 0] + img[:, :, 2])   # isole le vert
    score = score.clip(0)
    seuil = score.max() * 0.5
    lignes = np.arange(score.shape[0])[:, None]
    profil = np.full(score.shape[1], np.nan)
    for x in range(score.shape[1]):
        col = score[:, x]; m = col > seuil
        if m.any():
            profil[x] = (lignes[m, 0] * col[m]).sum() / col[m].sum()
    return profil

def mesurer_profondeur_mm(profil_px, mm_par_px):
    v = profil_px[~np.isnan(profil_px)]
    if v.size < 10:
        return None
    return max(np.percentile(v, 98) - np.median(v), 0.0) * mm_par_px  # fond - surface
```

### 8.4 Résultat d'exécution

Faute de photo réelle le jour de la rédaction, le POC génère des **images de test** (ligne laser + rainure de profondeur connue) pour valider la chaîne de bout en bout. Exemple d'image générée (cas « à surveiller ») :

![Ligne laser sur une rainure (image de test)](rebike-poc/images/synth_surveiller.png)

Sortie réelle de `python main.py` :

```text
[pneu de velo - rainure profonde]
  profondeur  : 3.50 mm   ->  CONFORME (Vert)
[pneu de velo - rainure moyenne]
  profondeur  : 2.40 mm   ->  A SURVEILLER (Orange)
[pneu de trottinette - rainure faible]
  profondeur  : 1.20 mm   ->  A REMPLACER (Rouge)
```

La chaîne complète **fonctionne et discrimine correctement** les trois états. Avec une vraie photo de ligne laser : `python main.py photo.jpg --calibration 0.05`.

### 8.5 Seuils de classement (mobilité douce, démonstration)

| Profondeur mesurée | État | Couleur |
|---:|---|---|
| ≥ 3 mm | Conforme | 🟢 Vert |
| 1,5 – 3 mm | À surveiller | 🟠 Orange |
| < 1,5 mm | À remplacer | 🔴 Rouge |

> Seuils à affiner avec des profils réels ; le facteur de calibration (mm/pixel) s'obtient via l'adaptateur de vérification (géométrie connue), qui est sa fonction d'origine.

---

## 9. Documentation des fonctions développées

| Fonction | Entrée | Sortie | Rôle |
|---|---|---|---|
| `profil_depuis_image()` | Image (BGR) | Profil (px) | Extrait la ligne laser par colonne |
| `profondeur_mm()` | Profil + calibration | Profondeur (mm) | Convertit le profil en profondeur réelle |
| `verdict()` | Profondeur (mm) | État + couleur + reco | Classe l'usure et formule une recommandation |

**Exemple de rapport généré :**

```text
Rapport FACOM ReBike
Objet contrôlé : pneu de vélo (rainure centrale)
Profondeur mesurée : 2,4 mm
État : À surveiller
Indicateur : Orange
Recommandation : effectuer un nouveau contrôle prochainement.
Opérateur : [Nom]    Date : [Date]
```

**Logique couleur** (reprise du SCANDIAG® d'origine) : 🟢 conforme · 🟠 proche de la limite · 🔴 non conforme · ⚫ en attente de mesure.

---

## 10. Apport RSE

**Réemploi du produit (~85 %)** : appareil, batterie, laser, caméra, Bluetooth, bouton, LED, adaptateurs, chargeur, câble, mallette sont tous conservés.

**Gain double :**
1. On évite la destruction d'un produit complet et de ses composants (dont une batterie Li-Ion).
2. On prolonge la vie d'autres objets (pneus de mobilité douce) en évitant leur remplacement prématuré **et** en retirant de la circulation les pneus dangereux.

C'est une réponse directe à l'objectif RSE de FACOM : éviter le gaspillage industriel **tout en créant une nouvelle valeur d'usage**.

---

## 11. Conclusion

Le SCANDIAG® DX.TSCANPB embarque déjà tout ce qu'il faut pour une jauge optique portable : laser, caméra, Bluetooth, batterie, IHM et mallette. Plutôt que de le démanteler pour quelques pièces, nous conservons son architecture et **détournons sa fonction de mesure par triangulation**.

**ReBike** — contrôle d'usure des pneus de mobilité douce — est le concept retenu : techniquement fidèle, démontrable en temps contraint, à marché clair et à fort sens RSE. Il constitue la **première verticale** d'une vision plus large, **ReScan**, dont l'extension (EPI, caoutchouc industriel, pédagogie) est déjà cartographiée. Une solution de réemploi crédible, faisable et industrialisable.

---

## 12. Annexes

### Annexe 1 — Archive du POC (fournie)

Le POC est livré et fonctionnel dans le dossier [`rebike-poc/`](rebike-poc/) :

```text
rebike-poc/
├── main.py              # pipeline complet (extraction → profondeur → verdict) + mode démo
├── README.md            # objectif, usage, seuils, limites
├── rapport_exemple.txt  # rapports générés par le mode démo
└── images/              # images de test générées (ligne laser + rainure)
    ├── synth_conforme.png
    ├── synth_surveiller.png
    └── synth_remplacer.png
```

Lancement : `pip install numpy pillow` puis `python main.py` (mode démo) ou
`python main.py photo.jpg --calibration 0.05` (vraie photo). Voir §8.4 pour la sortie.

### Annexe 2 — Datasheets (piste d'extension, non incluses)

Nous avons fait le choix de **ne pas ouvrir le produit** ; les références physiques des
composants ne sont donc pas relevées et aucune datasheet n'est jointe. Ce serait l'objet
d'une extension (niveau C) : relever les références sur la carte, puis récupérer les
datasheets du MCU/SoC, du module Bluetooth, du capteur CMOS, du driver laser et du circuit
de charge. La rétro-ingénierie **fonctionnelle** (§3.2) suffit au concept retenu.
