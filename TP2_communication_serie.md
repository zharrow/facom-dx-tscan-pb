# TP2 — Liaison série / Bluetooth avec le SCANDIAG

**Plateforme SCANDIAG·LAB — Module de TP n°2**
*Public : B3 / M1 Informatique · Durée : 2–3 h · Binômes*

> Ce TP fait partie du réemploi pédagogique du FACOM SCANDIAG (= TEXA Laser Examiner).
> Il s'appuie sur le fait que l'outil expose sa liaison **Bluetooth comme un port série**
> (SPP → port COM sous Windows, `/dev/rfcomm0` sous Linux). Le protocole applicatif est
> **propriétaire** : l'objectif du TP est de l'**observer et de commencer à le rétro-concevoir**.

---

## 1. Objectifs pédagogiques

À l'issue du TP, l'étudiant sait :
- appairer un périphérique **Bluetooth SPP** et l'exposer comme **port série** ;
- ouvrir et configurer un port série en Python (`pyserial`) ;
- **capturer et journaliser** un flux d'octets, et le lire en **hexadécimal/ASCII** ;
- formuler des **hypothèses sur un protocole inconnu** (en-tête, longueur, checksum, fin de trame) ;
- adopter une démarche de **rétro-ingénierie** méthodique et documentée.

## 2. Prérequis
- Un outil SCANDIAG chargé (LED verte ≥ 95 %).
- Un PC avec **Python 3.9+** et `pip install pyserial`.
- Le script fourni : [`poc/scandiag_client.py`](poc/scandiag_client.py).
- *(Référence)* Un PC Windows avec le logiciel officiel SCANDIAG (clé USB de la mallette) pour comparer.

## 3. Rappel sécurité ⚠️
- **Laser classe 3R** : ne jamais regarder le faisceau ni le diriger vers les yeux. Pointer une surface mate.
- **Batterie Li-ion** : pas de court-circuit, pas de chaleur. Travailler sur alimentation USB si la batterie est faible.

---

## 4. Étape A — Appairer l'outil et trouver le port

1. Allumer l'outil (appui **1 s** sur le bouton ; LED **bleue clignotante** = en attente de connexion Bluetooth).
2. Appairer en Bluetooth depuis l'OS :
   - **Windows** : Paramètres → Bluetooth → ajouter l'appareil → noter le **port COM sortant** créé (Gestionnaire de périphériques → Ports COM & LPT).
   - **Linux** :
     ```bash
     bluetoothctl            # scan on ; pair <MAC> ; trust <MAC>
     sudo rfcomm bind 0 <MAC_BT> 1    # crée /dev/rfcomm0
     ```
3. Lister les ports vus par Python :
   ```bash
   python poc/scandiag_client.py ports
   ```
   > 📝 **Q1.** Quel port correspond à l'outil ? Quelle est son adresse MAC / sa description ?

## 5. Étape B — Écouter l'outil (capture passive)

1. Lancer le moniteur (adapter le port) :
   ```bash
   python poc/scandiag_client.py monitor --port /dev/rfcomm0 --baud 115200 --log capture.log
   ```
2. **Déclencher une mesure** sur l'outil : poser l'aimant sur une surface métallique, appuyer une fois (laser ON), appuyer une 2ᵉ fois (capture). Un **bip** confirme l'envoi.
3. Observer le hexdump qui défile et le fichier `capture.log`.

   > 📝 **Q2.** L'outil envoie-t-il des octets de lui-même (sans qu'on lui parle) ? Combien à chaque appui ?
   > 📝 **Q3.** Repérez-vous un **motif récurrent** en début/fin de trame (octet de synchro, ex. `0xAA`/`0x55`) ?
   > 📝 **Q4.** La taille des trames est-elle **constante** ou **variable** ? (indice : champ de longueur ?)

   > 💡 Si rien n'arrive : essayer d'autres **baudrates** (`--baud 9600 / 38400 / 57600 / 230400`).
   > Sur un lien SPP « transparent », le baud côté PC peut être ignoré — tester quand même.

## 6. Étape C — Comparer avec le logiciel officiel (référence)

1. Sur le PC Windows de référence, lancer le logiciel SCANDIAG et faire une mesure **pendant** que le moniteur tourne sur un 2ᵉ PC appairé (ou via interposition `socat`).
2. Comparer les trames échangées : **commande PC → outil** puis **réponse outil → PC**.

   > 📝 **Q5.** Quelles trames le **logiciel** envoie-t-il à l'outil (initialisation, demande de mesure) ?
   > 📝 **Q6.** Proposez une **structure de trame** : `[SYNC][TYPE][LONGUEUR][DONNÉES…][CHECKSUM]` ? Justifiez.

## 7. Étape D — Dialoguer (rejeu / interactif)

1. Console interactive :
   ```bash
   python poc/scandiag_client.py repl --port /dev/rfcomm0 --baud 115200 --log repl.log
   ```
2. Rejouer une trame de commande capturée à l'étape C :
   ```
   scandiag> AA 01 02 55        # exemple : remplacez par votre trame réelle
   ```
3. Observer la réponse.

   > 📝 **Q7.** En rejouant la commande du logiciel, obtenez-vous la **même réponse** ? L'outil est-il *stateless* ou attend-il une séquence d'initialisation ?

## 8. Livrables attendus
- `capture.log` + `repl.log` (vos captures brutes).
- Une **fiche de protocole** (1 page) : structure de trame proposée, commandes identifiées, champs non compris.
- Réponses **Q1 → Q7**.
- *(Bonus)* Compléter la fonction `trigger_measurement()` du script avec la **vraie trame de mesure** et démontrer un déclenchement piloté depuis Python.

## 9. Critères d'évaluation
| Critère | Points |
|---|---|
| Appairage + identification du port réussis | 3 |
| Captures propres et journalisées | 3 |
| Qualité des hypothèses de protocole (méthode, justification) | 6 |
| Fiche de protocole claire et exploitable | 4 |
| Bonus : déclenchement piloté depuis Python | +4 |

---

## Pour l'enseignant (corrigé / notes)
- L'objectif n'est **pas** d'obtenir le protocole complet (il est propriétaire) mais d'**enseigner la démarche** : observer → hypothèse → test → documentation.
- Points d'attention typiques : confusion baudrate vs débit SPP, oubli de `reset_input_buffer()`, trames lues en plusieurs morceaux (bufferisation TCP-like du SPP).
- Prolongements : **TP3** (image caméra + OpenCV), **TP4** (triangulation/mesure), **TP5** (firmware/reflash).
- ⚠️ Rappeler que toute publication d'un protocole rétro-conçu doit respecter le cadre légal (interopérabilité) — bon sujet de discussion M2.
