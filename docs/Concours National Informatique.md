# Concours National Informatique — FACOM

**Réemploi RSE du produit FACOM SCANDIAG®**

## Contexte et enjeu

Le produit FACOM SCANDIAG® (référence DX.TSCANPB) n'est plus commercialisé. Un stock conséquent reste néanmoins immobilisé, et FACOM refuse, pour des raisons RSE, de mettre ces produits au rebut. La Direction RSE de l'entreprise lance officiellement un défi à Ynov : trouver une seconde vie aux composants de ce produit, afin de revaloriser les pièces et éviter le gaspillage industriel.

Ce concours national mobilise simultanément l'ensemble des campus Ynov, sur les niveaux B3, M1 et M2 Informatique. Les meilleures propositions feront l'objet d'un dossier remis directement à la Direction RSE de FACOM dans le cadre d'un partenariat industriel concret.

## Pourquoi ce challenge ?

Au-delà de la dimension RSE, ce concours national est une opportunité unique pour les étudiants Informatique de :

- Découvrir le monde physique : composants électroniques, capteurs, modules de communication, batteries, drivers
- Pratiquer la rétro-ingénierie : ouvrir un produit, identifier ses entrailles, comprendre son fonctionnement
- Apprendre à lire et exploiter une documentation technique (datasheets, schémas)
- Hacker un produit propriétaire pour lui donner une nouvelle utilité
- Travailler en équipe sous contrainte de temps sur un sujet ouvert et non balisé

C'est une porte d'entrée concrète vers l'IoT, l'embarqué, la cybersécurité matérielle, le développement rapide et itératif de POC et plus largement vers la culture du making qui irrigue l'industrie tech moderne.

## Format

- **Durée :** 7h
- **Équipes :** mixage des niveaux possible B3/M1/M2 selon l'organisation campus
- **Multi-campus :** tous les campus Ynov participants travaillent en parallèle sur le même sujet

## Mission

Votre équipe doit :

- Comprendre et tester le produit
- Comprendre les fonctionnalités exploitables des composants du SCANDIAG®
- Imaginer plusieurs usages plausibles de réemploi
- Sélectionner une idée parmi celles proposées
- Réaliser une preuve de concept fonctionnelle

## Ressources initiales

Vous devez chercher des informations en ligne sur le SCANDIAG® pour avoir une idée du contexte d'origine. Vous repartirez ensuite des composants, pour entamer une démarche d'ingénierie inverse.

### Phase 1 : Rétro-ingénierie

**Objectif :** identifier les composants clés et produire une synthèse fonctionnelle qui servira de base à toute la suite.

Étapes conseillées :

- Ouvrir le produit
- Identifier les composants clés : MCU ou SoC, module Bluetooth, capteur caméra (module caméra / capteur CMOS), diode/laser + driver, batterie (type/voltage), régulateurs de puissance, convertisseur DC-DC, connecteurs, switches, boutons, LED, convertisseur USB/TTL si présent, mémoire flash, éventuels capteurs supplémentaires (IMU, capteurs optiques)
- Pour chaque composant clé : relever la référence imprimée, télécharger la datasheet officielle, l'archiver dans le dossier de rendu, et rédiger une description synthétique de ses fonctionnalités exploitables
- Identifier où et comment se connecter pour charger le bootloader et le firmware, et documenter cette partie.
- Produire un schéma de principe fonctionnel du système : alimentations, MCU, interfaces caméra, laser driver, BT module, UI (boutons / LED / possibilité de raccorder un écran ou une IHM), connecteurs externes. Caractéristiques clés (tension batterie, consommations, interfaces UART/I2C/SPI/CAM, niveaux logiques)

### Phase 2 : Identifier le champ des possibles

**Objectif :** à partir de la rétro-ingénierie, dresser la cartographie complète de ce qui peut être réutilisé et de ce qui peut être ajouté.

- Lister les fonctions matérielles réutilisables
- Identifier les fonctionnalités qui pourraient être ajoutées : bus pour raccorder d'autres modules, I/O disponibles non utilisées, points d'extension
- Documenter les limites fonctionnelles
- Soyez exhaustifs, c'est sur cette base que la phase d'idéation tiendra debout

Produire un schéma fonctionnel de la carte électronique permettant de comprendre facilement :

- Les possibilités du produit en l'état
- Ce qui pourrait y être ajouté
- Où les éléments ajoutables pourraient être connectés

### Phase 3 : Idéation

Imaginer des concepts de réemploi, en explorant largement avant de converger.

Format attendu pour chaque concept :

- Titre du concept
- Description
- Problématique / enjeux RSE ou métiers adressés
- Fonctionnalités majeures utilisées et ajouts éventuellement nécessaires
- Notation de la valeur perçue de la solution (1 à 10)
- Estimation de la difficulté technique (1 à 10)
- Taux de réemploi du produit (estimatif de 0 à 100%)

### Phase 4 : POC

Faire une preuve de concept de l'application choisie implémentée ou non.

## Livrable final à FACOM

L'ensemble du travail des équipes est consolidé en un dossier unique transmis à la Direction RSE de FACOM comme proposition officielle de seconde vie pour le produit SCANDIAG®.

Contenu du dossier équipe :

- Membres de l'équipe (noms, classe, campus (préciser Ville Ynov Campus))
- Datasheets des composants clés
- Schéma fonctionnel du produit
- Descriptifs des idées de réemploi avec notation
- Concept retenu et justification
- Archive du ou des programmes développés (firmware)
- Documentation des fonctions développées

## Critères de sélection des meilleures équipes

Les dossiers seront évalués collectivement par l'équipe pédagogique nationale Informatique et par FACOM, sur :

- **Richesse de l'idéation :** diversité, créativité, pertinence RSE
- **Faisabilité du concept retenu :** cohérence entre l'idée et les composants disponibles
- **Niveau d'aboutissement du POC :** preuve fonctionnelle, robustesse, qualité du code
- **Qualité du livrable final :** c'est un document qui sera lu par un industriel, donc soigné, professionnel, lisible

Les équipes dont les concepts seront retenus par FACOM verront leur travail valorisé publiquement et potentiellement industrialisé.

## Règles et bonnes pratiques

- **Sécurité avant tout :** attention aux batteries (court-circuit, échauffement), aux lasers
- **Pas de jet de composants :** tout ce qui sort du produit reste dans la zone de travail. RSE oblige
- **Documentation au fil de l'eau :** ne gardez pas tout pour la dernière heure, prenez des photos et des notes en continu

## Ce que vous gagnerez

- Une expérience concrète de rétro-ingénierie matérielle
- Une compétence transférable directement en stage et en entreprise
- Une visibilité auprès d'un industriel de premier plan (FACOM, groupe Stanley Black & Decker)
- Avoir contribué à une démarche RSE réelle, pas un exercice théorique

Bon challenge à toutes et à tous.
