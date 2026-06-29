# Concours National Informatique — FACOM

## Réemploi RSE du produit FACOM SCANDIAG® DX.TSCANPB

---

## 1. Présentation de l’équipe

Campus : [Ville Ynov Campus]
Classe : [B3 / M1 / M2]

Membres de l’équipe :

| Nom / Prénom | Classe   | Rôle dans le projet                 |
| ------------ | -------- | ----------------------------------- |
| [Nom Prénom] | [Classe] | Chef de projet / coordination       |
| [Nom Prénom] | [Classe] | Rétro-ingénierie matérielle         |
| [Nom Prénom] | [Classe] | Recherche documentaire / datasheets |
| [Nom Prénom] | [Classe] | Développement POC                   |
| [Nom Prénom] | [Classe] | Documentation / rendu final         |

---

# 2. Introduction

Le produit étudié est le **FACOM SCANDIAG® DX.TSCANPB**. Il s’agit d’un analyseur professionnel de disques de frein et de pneus. Son objectif initial est de mesurer l’usure des disques de frein et la profondeur de la bande de roulement des pneus, sans démontage systématique des roues.

Ce produit n’étant plus commercialisé, FACOM souhaite éviter la mise au rebut d’un stock existant. La problématique du challenge est donc de proposer une seconde vie au SCANDIAG®, en réutilisant au maximum ses composants et son architecture existante.

Notre démarche repose sur quatre étapes :

1. comprendre le fonctionnement du produit ;
2. identifier les fonctions matérielles réutilisables ;
3. imaginer plusieurs usages de réemploi ;
4. choisir une idée et proposer une preuve de concept.

Le concept retenu par notre équipe est :

## FACOM ReScan — Jauge optique portable multi-usages

L’objectif est de transformer le SCANDIAG® en outil portable de contrôle d’usure ou de profondeur, utilisable sur d’autres objets que les pneus et les disques de frein automobiles.

Exemples d’applications :

* pneus de vélos ;
* pneus de trottinettes électriques ;
* semelles de chaussures de sécurité ;
* pièces en caoutchouc ;
* bandes transporteuses ;
* rainures ou reliefs de petites pièces industrielles.

---

# 3. Analyse du produit d’origine

## 3.1 Fonction initiale

Le SCANDIAG® est un outil de mesure optique. Il projette un faisceau laser sur une surface à contrôler, comme un disque de frein ou un pneu. L’image générée par le laser est ensuite captée par une micro-caméra. Les données sont transmises à un ordinateur ou à une unité d’affichage équipée du logiciel SCANDIAG, qui traite les données et affiche un résultat graphique.

Le fonctionnement global peut être résumé ainsi :

Positionnement de l’outil
→ activation du laser
→ capture par micro-caméra
→ transmission des données
→ traitement logiciel
→ affichage du résultat
→ génération d’un rapport

## 3.2 Observation du produit physique

À partir des photos et de l’observation du kit, le produit se présente sous la forme d’une mallette rigide FACOM contenant :

* l’appareil SCANDIAG® ;
* une base ou un adaptateur circulaire de vérification ;
* un adaptateur pour l’analyse de pneus ;
* un chargeur secteur ;
* un câble USB ;
* une mousse de protection ;
* des accessoires de positionnement.

La référence visible est **DX.TSCANPB**. L’étiquette indique un usage lié au scanning des disques et des pneus.

L’appareil principal est un outil portable, allongé et ergonomique. On observe :

* un marquage FACOM DX.TSCAN ;
* un bouton de commande ;
* une zone optique à l’extrémité ;
* un pictogramme de danger laser ;
* un boîtier robuste adapté à un environnement d’atelier.

Cette première observation confirme que le produit est conçu pour être transportable, robuste et utilisable rapidement par un professionnel.

---

# 4. Caractéristiques techniques vérifiées

| Élément                               | Donnée technique                          |
| ------------------------------------- | ----------------------------------------- |
| Produit                               | FACOM SCANDIAG® DX.TSCANPB                |
| Fonction d’origine                    | Analyseur de disques de frein et de pneus |
| Alimentation externe                  | 100 / 240 V AC                            |
| Sortie du chargeur                    | 5 V / 1,2 A                               |
| Type de connexion                     | USB Mini-B                                |
| Entrée de l’outil                     | 5 V / 0,5 A                               |
| Batterie interne                      | Li-Ion                                    |
| Capacité batterie                     | 0,620 Ah                                  |
| Tension batterie                      | 3,7 V                                     |
| Classe laser                          | 3R                                        |
| Puissance laser                       | > 5 mW                                    |
| Longueur d’onde laser                 | 510 à 530 nm                              |
| Durée d’impulsion                     | 10 ms                                     |
| Micro-caméra                          | CMOS WXGA, 1 mégapixel, 30 fps            |
| Communication                         | Module Bluetooth® intégré                 |
| Bande de fréquence Bluetooth          | 2400 à 2483,5 MHz                         |
| Puissance radio maximale              | 0 dBm                                     |
| Interface utilisateur                 | Bouton poussoir + LED RVB                 |
| Température de fonctionnement         | 0 à 40 °C                                 |
| Température de stockage               | -20 à 60 °C                               |
| Humidité de fonctionnement / stockage | 10 % à 80 %, sans condensation            |
| Poids                                 | 90 g pour l’outil, 10 g pour l’adaptateur |

---

# 5. Contenu du kit

| Élément                                           | Référence / numéro | Fonction                 |
| ------------------------------------------------- | -----------------: | ------------------------ |
| Analyseur de disques de frein et de pneus         |         DX.TSCAN-1 | Appareil principal       |
| Adaptateur pour vérification du système de mesure |         DX.TSCAN-2 | Calibration / contrôle   |
| Adaptateur pour analyse d’usure des pneus         |         DX.TSCAN-3 | Positionnement sur pneu  |
| Câble USB                                         |         DX.TSCAN-4 | Recharge                 |
| Adaptateur secteur                                |         DX.TSCAN-4 | Alimentation / recharge  |
| Clé USB                                           |        DX.TSCANUSB | Logiciel / documentation |
| Mallette FACOM                                    |        Non indiqué | Transport et protection  |

---

# 6. Phase 1 — Rétro-ingénierie

## 6.1 Composants identifiés grâce à la notice

| Numéro notice | Élément                                              | Fonction                                                  |
| ------------: | ---------------------------------------------------- | --------------------------------------------------------- |
|             1 | Bouton multifonction avec LED multicolore intégrée   | Allumer, éteindre, déclencher une mesure, afficher l’état |
|             2 | Connecteur USB                                       | Recharge de la batterie interne                           |
|             3 | Diode laser                                          | Projection du faisceau de mesure                          |
|             4 | Micro-caméra                                         | Capture de l’image générée par le laser                   |
|             5 | Aimant                                               | Maintien ou positionnement de l’appareil                  |
|             6 | Adaptateur pour l’analyse de l’usure des pneus       | Positionnement sur pneu                                   |
|             7 | Adaptateur pour la vérification du système de mesure | Calibration / contrôle                                    |
|             8 | Câble USB                                            | Recharge                                                  |
|             9 | Chargeur USB                                         | Alimentation secteur                                      |
|            14 | Code date                                            | Identification de l’année de fabrication                  |

## 6.2 Composants internes à identifier après ouverture

La notice donne les fonctions principales, mais ne donne pas les références exactes du microcontrôleur, du module Bluetooth, du capteur caméra ou des circuits de puissance. Ces références doivent être relevées directement sur la carte électronique après ouverture.

| Composant interne          | Référence relevée sur la carte | Fonction                          | Datasheet à rechercher | Statut             |
| -------------------------- | ------------------------------ | --------------------------------- | ---------------------- | ------------------ |
| Microcontrôleur / SoC      | À compléter                    | Pilotage de l’ensemble du système | Oui                    | À identifier       |
| Module Bluetooth           | À compléter                    | Communication avec le PC          | Oui                    | À identifier       |
| Capteur caméra CMOS        | À compléter                    | Acquisition image                 | Oui                    | À identifier       |
| Diode laser                | À compléter                    | Projection du faisceau            | Oui                    | Fonction confirmée |
| Driver laser               | À compléter                    | Commande électrique du laser      | Oui                    | À identifier       |
| Circuit de charge batterie | À compléter                    | Recharge Li-Ion                   | Oui                    | À identifier       |
| Régulateurs de tension     | À compléter                    | Conversion d’alimentation         | Oui                    | À identifier       |
| Mémoire flash éventuelle   | À compléter                    | Stockage firmware / paramètres    | Oui                    | À vérifier         |
| Connecteurs de debug       | À compléter                    | Programmation / diagnostic        | Oui                    | À vérifier         |
| Batterie Li-Ion            | À compléter                    | Alimentation autonome             | Oui                    | Fonction confirmée |

## 6.3 Schéma fonctionnel du produit

Le schéma fonctionnel du SCANDIAG® peut être représenté ainsi :

Batterie Li-Ion 3,7 V
→ circuit de charge USB Mini-B
→ alimentation interne
→ microcontrôleur principal
→ bouton multifonction
→ LED RVB
→ diode laser
→ micro-caméra CMOS
→ module Bluetooth
→ logiciel SCANDIAG sur PC
→ affichage graphique / rapport

## 6.4 Hypothèse de fonctionnement technique

Le fonctionnement probable est le suivant :

1. L’utilisateur allume l’appareil avec le bouton multifonction.
2. L’appareil se connecte au PC par Bluetooth.
3. L’utilisateur positionne l’outil sur un disque de frein ou un pneu.
4. Le laser est activé.
5. La micro-caméra capture l’image produite par le faisceau laser.
6. Les données captées sont envoyées au logiciel SCANDIAG.
7. Le logiciel traite l’image.
8. Le résultat est affiché en couleur.
9. Un rapport peut être sauvegardé ou imprimé.

---

# 7. Sécurité

## 7.1 Risques identifiés

Le produit contient :

* une diode laser classe 3R ;
* une batterie Li-Ion ;
* une alimentation secteur ;
* des composants électroniques sensibles ;
* une liaison radio Bluetooth.

Les principaux risques sont :

* exposition au faisceau laser ;
* blessure oculaire ;
* court-circuit batterie ;
* échauffement ;
* choc électrique lors de la recharge ;
* endommagement de la caméra ou des lentilles ;
* mauvaise manipulation lors de l’ouverture.

## 7.2 Règles de sécurité à respecter

Pendant le TP :

* ne jamais regarder directement le faisceau laser ;
* ne jamais pointer le laser vers une personne ;
* ne pas utiliser d’instrument optique pour observer le faisceau ;
* ne pas activer le laser tant que l’outil n’est pas correctement positionné ;
* ne pas court-circuiter la batterie ;
* ne pas utiliser l’appareil dans un environnement humide ;
* ne pas utiliser l’appareil près de liquides ou gaz inflammables ;
* ne pas charger la batterie sous 4 °C ou au-dessus de 40 °C ;
* ne pas exposer la batterie à une température supérieure à 130 °C ;
* conserver toutes les pièces démontées dans la zone de travail.

---

# 8. Phase 2 — Champ des possibles

## 8.1 Fonctions matérielles réutilisables

| Fonction                   | Réemploi possible                                      | Intérêt    |
| -------------------------- | ------------------------------------------------------ | ---------- |
| Laser 510–530 nm           | Mesure optique, repère, détection de profil            | Très élevé |
| Micro-caméra CMOS 1 MP     | Capture d’image, analyse visuelle, détection de relief | Très élevé |
| Bluetooth intégré          | Transmission vers PC ou application                    | Élevé      |
| Batterie Li-Ion            | Autonomie portable                                     | Élevé      |
| Bouton multifonction       | Déclenchement utilisateur                              | Élevé      |
| LED RVB                    | Retour d’état visuel                                   | Élevé      |
| Boîtier ergonomique        | Réemploi direct en outil portable                      | Très élevé |
| Adaptateur pneu            | Support de mesure ou base de repositionnement          | Élevé      |
| Adaptateur de vérification | Calibration ou contrôle périodique                     | Élevé      |
| Mallette                   | Kit de transport professionnel ou pédagogique          | Très élevé |
| Chargeur et câble USB      | Recharge                                               | Élevé      |

## 8.2 Fonctions pouvant être ajoutées

| Ajout possible             | Fonction                              | Connexion envisagée      |
| -------------------------- | ------------------------------------- | ------------------------ |
| Application mobile simple  | Affichage des mesures                 | Bluetooth                |
| Interface PC personnalisée | Rapport de contrôle                   | Bluetooth / COM          |
| Écran OLED                 | Affichage direct sans PC              | I2C / SPI si accès carte |
| Buzzer                     | Signal sonore conforme / non conforme | GPIO                     |
| Support imprimé 3D         | Adaptation à d’autres objets          | Fixation mécanique       |
| Base de calibration        | Mesure plus fiable                    | Accessoire externe       |
| Algorithme de vision       | Analyse automatique d’image           | Logiciel                 |
| Base de données de mesures | Historique et traçabilité             | Logiciel                 |

## 8.3 Limites fonctionnelles

| Limite                                          | Conséquence                                   |
| ----------------------------------------------- | --------------------------------------------- |
| Firmware propriétaire                           | Reprogrammation incertaine                    |
| Accès bootloader inconnu                        | Difficulté à modifier le comportement interne |
| Références internes non visibles sans ouverture | Datasheets à compléter après démontage        |
| Laser classe 3R                                 | Contraintes de sécurité fortes                |
| Caméra calibrée pour pneus/disques              | Recalibrage nécessaire pour nouveaux usages   |
| Dépendance au logiciel SCANDIAG                 | Limite l’usage autonome                       |
| USB prévu principalement pour la charge         | Communication USB non garantie                |
| Mesure sensible au positionnement               | Besoin de supports mécaniques adaptés         |

---

# 9. Phase 3 — Idéation

## Concept 1 — FACOM ReScan

### Description

FACOM ReScan est une jauge optique portable multi-usages. Elle permet de mesurer ou qualifier l’usure de différents objets en utilisant le laser, la micro-caméra, la batterie, le Bluetooth et le boîtier existant du SCANDIAG®.

### Problématique adressée

Beaucoup d’objets sont remplacés trop tôt par manque d’outil de contrôle simple. À l’inverse, certains objets usés restent en circulation alors qu’ils présentent un risque. FACOM ReScan permet de contrôler rapidement l’état d’usure et de prendre une décision : conserver, surveiller ou remplacer.

### Fonctions utilisées

* laser ;
* micro-caméra ;
* Bluetooth ;
* batterie ;
* bouton ;
* LED ;
* boîtier ;
* adaptateurs.

### Ajouts nécessaires

* logiciel ou application de classification ;
* seuils de mesure adaptés ;
* support mécanique selon l’objet contrôlé.

Valeur perçue : 9/10
Difficulté technique : 6/10
Taux de réemploi estimé : 85 %

---

## Concept 2 — ReBike Control

### Description

Réemploi du SCANDIAG® comme outil de contrôle des pneus de vélos, vélos cargo, scooters et trottinettes électriques.

### Problématique adressée

Avec le développement de la mobilité douce, les ateliers vélo et trottinette ont besoin d’outils rapides pour contrôler l’usure des pneus. Un pneu trop usé peut réduire l’adhérence et augmenter le risque d’accident.

### Fonctions utilisées

* laser ;
* micro-caméra ;
* batterie ;
* Bluetooth ;
* adaptateur de positionnement.

### Ajouts nécessaires

* gabarit pour pneus fins ;
* seuils adaptés aux pneus vélo / trottinette ;
* interface simple.

Valeur perçue : 8/10
Difficulté technique : 5/10
Taux de réemploi estimé : 80 %

---

## Concept 3 — SafeStep

### Description

SafeStep transforme le SCANDIAG® en outil de contrôle des semelles de chaussures de sécurité.

### Problématique adressée

Dans les ateliers, entrepôts ou zones industrielles, les chaussures de sécurité usées peuvent présenter un risque : perte d’adhérence, glissade, non-conformité. Un outil de contrôle permettrait de vérifier si la semelle reste utilisable.

### Fonctions utilisées

* laser ;
* micro-caméra ;
* LED ;
* bouton ;
* batterie ;
* Bluetooth.

### Ajouts nécessaires

* support de pose pour chaussure ;
* seuils d’usure selon type de semelle ;
* rapport simple pour suivi EPI.

Valeur perçue : 7/10
Difficulté technique : 6/10
Taux de réemploi estimé : 75 %

---

## Concept 4 — Kit pédagogique IoT / rétro-ingénierie

### Description

Le SCANDIAG® est réemployé comme kit pédagogique pour apprendre l’IoT, l’embarqué, la rétro-ingénierie, la vision, le Bluetooth, la gestion batterie et la sécurité laser.

### Problématique adressée

Les formations informatiques et électroniques manquent souvent de supports industriels réels. Ce produit permettrait aux étudiants de travailler sur un objet concret.

### Fonctions utilisées

* carte électronique ;
* batterie ;
* Bluetooth ;
* laser ;
* caméra ;
* bouton ;
* LED ;
* boîtier.

### Ajouts nécessaires

* documentation pédagogique ;
* exercices guidés ;
* exemple de logiciel de traitement ;
* consignes de sécurité.

Valeur perçue : 7/10
Difficulté technique : 4/10
Taux de réemploi estimé : 90 %

---

## Concept 5 — Inspecteur de bandes caoutchouc

### Description

Réemploi du SCANDIAG® pour contrôler l’usure ou les défauts de bandes transporteuses, tapis industriels ou surfaces en caoutchouc.

### Problématique adressée

Dans l’industrie, les bandes transporteuses sont souvent remplacées par sécurité ou à la suite d’une panne. Un contrôle portable permettrait de mieux planifier la maintenance.

### Fonctions utilisées

* laser ;
* micro-caméra ;
* batterie ;
* Bluetooth ;
* mallette de transport.

### Ajouts nécessaires

* support mécanique adapté aux surfaces planes ;
* seuils spécifiques ;
* procédure de calibration.

Valeur perçue : 8/10
Difficulté technique : 7/10
Taux de réemploi estimé : 75 %

---

# 10. Comparaison des concepts

| Concept               | Valeur | Difficulté | Réemploi | Pertinence RSE | Commentaire                     |
| --------------------- | -----: | ---------: | -------: | -------------: | ------------------------------- |
| FACOM ReScan          |   9/10 |       6/10 |     85 % |           9/10 | Meilleur équilibre global       |
| ReBike Control        |   8/10 |       5/10 |     80 % |           8/10 | Très faisable                   |
| SafeStep              |   7/10 |       6/10 |     75 % |           8/10 | Bon angle sécurité / EPI        |
| Kit pédagogique IoT   |   7/10 |       4/10 |     90 % |           7/10 | Très faisable, moins industriel |
| Inspecteur caoutchouc |   8/10 |       7/10 |     75 % |           8/10 | Pertinent mais plus complexe    |

---

# 11. Concept retenu

## FACOM ReScan — Jauge optique portable multi-usages

Le concept retenu est **FACOM ReScan**.

Ce concept consiste à réutiliser le SCANDIAG® comme outil de contrôle d’usure sur plusieurs familles d’objets. Le produit conserve son principe technique d’origine : une mesure optique basée sur un faisceau laser et une micro-caméra.

Au lieu de limiter l’appareil aux disques de frein et aux pneus automobiles, nous proposons de l’adapter à d’autres usages professionnels ou semi-professionnels.

## 11.1 Usages visés

| Domaine        | Objet contrôlé           | Objectif                              |
| -------------- | ------------------------ | ------------------------------------- |
| Mobilité douce | Pneu vélo / trottinette  | Vérifier la profondeur des rainures   |
| Industrie      | Bande transporteuse      | Détecter une usure ou une déformation |
| Sécurité       | Semelle de chaussure EPI | Vérifier l’adhérence restante         |
| Maintenance    | Pièces caoutchouc        | Mesurer un relief ou une rainure      |
| Pédagogie      | Support de TP            | Apprendre l’IoT et la mesure optique  |

## 11.2 Justification du choix

FACOM ReScan est le concept le plus pertinent car il conserve l’identité technique du SCANDIAG®. L’appareil est déjà un outil portable de mesure optique. Il possède déjà :

* une diode laser ;
* une micro-caméra ;
* une batterie ;
* une liaison Bluetooth ;
* une LED de retour d’état ;
* un bouton multifonction ;
* une mallette ;
* des adaptateurs de positionnement.

Le réemploi proposé ne nécessite donc pas de reconstruire totalement un nouveau produit. Il s’agit plutôt de détourner son usage initial vers d’autres contrôles d’usure.

## 11.3 Intérêt RSE

Le projet présente un double intérêt RSE :

1. éviter la mise au rebut du SCANDIAG® ;
2. utiliser le SCANDIAG® pour prolonger la durée de vie d’autres objets.

Cette approche permet :

* de limiter les déchets électroniques ;
* de réutiliser une batterie, une caméra, un laser et un boîtier existants ;
* de réduire le remplacement prématuré de pièces encore utilisables ;
* de favoriser la maintenance préventive ;
* de créer une solution professionnelle à partir d’un stock immobilisé.

---

# 12. Phase 4 — Preuve de concept

## 12.1 Objectif du POC

L’objectif du POC est de démontrer que le SCANDIAG® peut être réemployé comme jauge optique de contrôle d’usure.

Pour le TP, nous proposons un POC réalisable même si le firmware propriétaire n’est pas totalement accessible.

## 12.2 Objet de test choisi

Objet de test : **semelle de chaussure ou pneu de vélo**.

Ces objets sont adaptés au POC car ils possèdent des rainures ou reliefs proches de ceux d’un pneu automobile, mais dans un contexte de réemploi différent.

## 12.3 Principe du POC

Le POC fonctionne ainsi :

1. L’utilisateur positionne l’appareil sur l’objet à contrôler.
2. Le laser sert de repère visuel.
3. La micro-caméra ou une valeur simulée fournit une mesure.
4. Le programme interprète la mesure.
5. Le résultat est classé en trois niveaux :

   * conforme ;
   * à surveiller ;
   * à remplacer.
6. Une couleur est associée à l’état :

   * vert ;
   * orange ;
   * rouge.
7. Un rapport simple est généré.

## 12.4 Seuils utilisés pour la démonstration

Les seuils ci-dessous sont utilisés pour le POC. Ils sont volontairement simplifiés.

|             Valeur mesurée | État         | Couleur |
| -------------------------: | ------------ | ------- |
| Supérieure ou égale à 3 mm | Conforme     | Vert    |
|       Entre 1,5 mm et 3 mm | À surveiller | Orange  |
|        Inférieure à 1,5 mm | À remplacer  | Rouge   |

## 12.5 Algorithme du POC

```python
def analyser_usure(valeur_mm):
    if valeur_mm >= 3:
        return "CONFORME", "Vert", "L'objet peut continuer à être utilisé."
    elif valeur_mm >= 1.5:
        return "A SURVEILLER", "Orange", "L'objet reste utilisable mais doit être contrôlé prochainement."
    else:
        return "A REMPLACER", "Rouge", "L'objet présente une usure trop importante."

mesures = [4.2, 2.4, 0.9]

for mesure in mesures:
    etat, couleur, recommandation = analyser_usure(mesure)
    print("Mesure :", mesure, "mm")
    print("État :", etat)
    print("Indicateur :", couleur)
    print("Recommandation :", recommandation)
    print("---")
```

## 12.6 Exemple de résultat

Mesure relevée : 2,4 mm
État : à surveiller
Indicateur : orange
Recommandation : l’objet reste utilisable, mais un nouveau contrôle doit être réalisé prochainement.

## 12.7 Version POC sans accès firmware

Si le firmware du SCANDIAG® est verrouillé, le POC peut être présenté sous forme de démonstrateur logiciel :

* l’appareil réel est utilisé comme support physique ;
* le principe de mesure laser + caméra est documenté ;
* les valeurs de mesure sont simulées ;
* le programme classe l’état d’usure ;
* une interface simple affiche le résultat.

Cette version reste pertinente car le challenge évalue aussi la faisabilité, la cohérence du concept, l’idéation et la documentation.

## 12.8 Version POC avec accès Bluetooth / logiciel

Si la connexion Bluetooth avec le logiciel SCANDIAG fonctionne, le POC peut aller plus loin :

* connexion de l’appareil au PC ;
* récupération ou observation des acquisitions ;
* utilisation d’un rapport existant ;
* adaptation du scénario de mesure à un objet non automobile ;
* démonstration de la réutilisation de la chaîne de mesure.

## 12.9 Version POC avec accès carte électronique

Si la carte est ouverte et que des points de debug sont identifiés :

* recherche d’un port UART, SWD ou JTAG ;
* identification du microcontrôleur ;
* lecture des niveaux logiques ;
* test de communication ;
* tentative de compréhension du firmware ;
* documentation de la faisabilité d’un firmware alternatif.

---

# 13. Documentation des fonctions développées

## 13.1 Fonction d’analyse d’usure

Nom : `analyser_usure()`
Entrée : valeur en millimètres
Sortie : état, couleur, recommandation

La fonction compare une valeur mesurée à des seuils prédéfinis. Elle permet de transformer une mesure brute en décision utilisateur.

## 13.2 Fonction de génération de rapport

Le rapport peut contenir :

* date du contrôle ;
* objet contrôlé ;
* mesure relevée ;
* état ;
* recommandation ;
* nom de l’opérateur ;
* commentaire.

Exemple de rapport :

```text
Rapport FACOM ReScan

Objet contrôlé : pneu de vélo
Mesure relevée : 2,4 mm
État : à surveiller
Indicateur : orange
Recommandation : effectuer un nouveau contrôle prochainement.
Opérateur : [Nom]
Date : [Date]
```

## 13.3 Fonction d’affichage utilisateur

L’affichage peut reprendre la logique couleur du SCANDIAG® d’origine :

| Couleur        | Signification        |
| -------------- | -------------------- |
| Vert           | Conforme             |
| Orange / jaune | Proche de la limite  |
| Rouge          | Non conforme         |
| Noir / gris    | En attente de mesure |

---

# 14. Schéma fonctionnel du concept FACOM ReScan

Le concept FACOM ReScan peut être résumé ainsi :

Utilisateur
→ positionne l’appareil
→ déclenche la mesure
→ laser projeté sur l’objet
→ image captée par micro-caméra
→ donnée transmise en Bluetooth
→ traitement logiciel
→ classification de l’état
→ rapport ou affichage couleur

## Schéma technique simplifié

Batterie Li-Ion
→ alimentation interne
→ bouton multifonction
→ laser + micro-caméra
→ acquisition optique
→ Bluetooth
→ logiciel FACOM ReScan
→ résultat : conforme / à surveiller / à remplacer

---

# 15. Limites du projet

Le projet présente plusieurs limites :

| Limite                                      | Impact                                       |
| ------------------------------------------- | -------------------------------------------- |
| Firmware propriétaire                       | Reprogrammation incertaine                   |
| Accès aux données caméra non garanti        | Traitement direct difficile                  |
| Calibration nécessaire                      | Mesures à valider expérimentalement          |
| Laser classe 3R                             | Usage encadré obligatoire                    |
| Batterie Li-Ion                             | Manipulation prudente                        |
| Objet initial conçu pour pneus/disques auto | Adaptateurs nécessaires pour nouveaux objets |
| Seuils de mesure variables                  | Besoin de profils selon usage                |
| Logiciel SCANDIAG propriétaire              | Dépendance possible à l’écosystème FACOM     |

---

# 16. Perspectives d’amélioration

Pour industrialiser ou améliorer le concept, plusieurs pistes sont possibles :

* développer une application mobile FACOM ReScan ;
* créer plusieurs profils de mesure :

  * vélo ;
  * trottinette ;
  * semelle EPI ;
  * caoutchouc industriel ;
  * bande transporteuse ;
* concevoir des adaptateurs imprimés en 3D ;
* développer un firmware alternatif si le matériel le permet ;
* ajouter une base de données de rapports ;
* intégrer un export PDF ;
* créer une procédure de calibration ;
* proposer un kit pédagogique pour les écoles ;
* créer une documentation de reconditionnement FACOM ;
* mettre en place un protocole de sécurité laser.

---

# 17. Apport RSE

Le projet FACOM ReScan répond directement à la problématique RSE du concours.

## 17.1 Réemploi du produit FACOM

Le projet permet de réutiliser :

* l’appareil principal ;
* la batterie ;
* le laser ;
* la micro-caméra ;
* le Bluetooth ;
* le bouton ;
* la LED ;
* les adaptateurs ;
* le chargeur ;
* le câble USB ;
* la mallette.

Le taux de réemploi estimé est d’environ **85 %**.

## 17.2 Réduction des déchets

En donnant une seconde vie au SCANDIAG®, FACOM évite :

* la destruction d’un produit complet ;
* le gaspillage de composants électroniques ;
* la mise au rebut de batteries ;
* la production d’un nouvel outil équivalent.

## 17.3 Utilité du nouveau produit

Le nouveau produit aide aussi à prolonger la durée de vie d’autres objets. Il peut éviter le remplacement trop précoce de pneus, semelles, pièces caoutchouc ou équipements industriels.

Le gain RSE est donc double :

1. réemploi du SCANDIAG® ;
2. meilleure maintenance des objets contrôlés.

---

# 18. Conclusion

Le SCANDIAG® DX.TSCANPB est un produit professionnel complet, intégrant déjà les éléments nécessaires à une solution de mesure portable : laser, micro-caméra, Bluetooth, batterie, bouton multifonction, LED RVB, chargeur, adaptateurs et mallette.

Notre projet **FACOM ReScan** propose une seconde vie réaliste et cohérente avec la fonction initiale du produit. Plutôt que de démonter le SCANDIAG® pour récupérer seulement quelques composants, nous proposons de conserver son architecture globale et de l’adapter à de nouveaux usages.

Le concept retenu permet de transformer un produit non commercialisé en outil utile pour la maintenance, la sécurité, la mobilité douce, l’industrie et la pédagogie. Il répond directement à l’objectif RSE de FACOM : éviter le gaspillage industriel tout en créant une nouvelle valeur d’usage.

FACOM ReScan est donc une solution de réemploi crédible, faisable et potentiellement industrialisable.

---

# 19. Annexes

## Annexe 1 — Photos du produit

Photos à intégrer :

1. mallette FACOM ouverte ;
2. étiquette avec référence DX.TSCANPB ;
3. appareil SCANDIAG® dans sa mousse ;
4. chargeur et câble USB ;
5. adaptateur circulaire de vérification ;
6. pictogramme laser ;
7. bouton multifonction ;
8. zone optique ;
9. carte électronique après ouverture ;
10. batterie après ouverture.

## Annexe 2 — Datasheets à ajouter après ouverture

| Élément                    | Datasheet à ajouter                        |
| -------------------------- | ------------------------------------------ |
| Microcontrôleur / SoC      | À rechercher après lecture de la référence |
| Module Bluetooth           | À rechercher après lecture de la référence |
| Capteur caméra CMOS        | À rechercher après lecture de la référence |
| Driver laser               | À rechercher après lecture de la référence |
| Circuit de charge batterie | À rechercher après lecture de la référence |
| Régulateurs de tension     | À rechercher après lecture de la référence |
| Mémoire flash éventuelle   | À rechercher si présente                   |

## Annexe 3 — Archive de code à fournir

L’archive du POC peut contenir :

* `main.py` ;
* `README.md` ;
* captures d’écran du terminal ;
* exemple de rapport ;
* photos du montage ;
* schéma fonctionnel.

## Annexe 4 — README du POC

```text
FACOM ReScan — POC

Objectif :
Démontrer la réutilisation du SCANDIAG® comme jauge optique portable de contrôle d’usure.

Fonctionnement :
Le programme prend une valeur de profondeur en millimètres et classe l’objet selon trois états :
- conforme ;
- à surveiller ;
- à remplacer.

Fichiers :
- main.py : algorithme de classification
- rapport_exemple.txt : exemple de rapport
- schema_fonctionnel.png : schéma de principe
- photos/ : photos du produit et du montage

Limites :
Les mesures sont simulées si l’accès direct au firmware ou aux données caméra n’est pas disponible.
```
