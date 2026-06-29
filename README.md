# Concours National Informatique — Ynov × FACOM

## Réemploi RSE du FACOM SCANDIAG® (DX.TSCANPB) — Projet **ReBike**

Dossier de proposition à la Direction RSE de FACOM, réalisé dans le cadre du Concours
National Informatique Ynov.

**Équipe (M1 Dev Fullstack — Toulouse Ynov Campus) :** Stoffelbach Théo · Remery Lucas ·
Detres Florent · Breton Swann · Abadie Thomas · Bernard Julien.

---

### En deux lignes

Le SCANDIAG® (analyseur d'usure de disques/pneus, arrêté) mesure une profondeur par
**triangulation laser**. Nous le réemployons en **ReBike**, un contrôleur d'usure de pneus de
**mobilité douce** (vélo / trottinette) — sans démanteler l'outil, avec un POC logiciel qui
fonctionne.

### Contenu du dépôt

| Élément | Chemin | Description |
|---|---|---|
| 📄 **Dossier de rendu** | [`Dossier-Rendu-FACOM.md`](Dossier-Rendu-FACOM.md) | Le document principal (à lire en priorité) |
| 📄 **Version PDF** | [`Dossier-Rendu-FACOM.pdf`](Dossier-Rendu-FACOM.pdf) | Export imprimable du dossier |
| 💻 **POC** | [`rebike-poc/`](rebike-poc/) | Preuve de concept exécutable (Python) |
| 📐 **Datasheets** | [`datasheets/`](datasheets/) | Composants identifiés au teardown + liens officiels |
| 🖼️ **Photos** | [`images_facom/`](images_facom/) | Boîtier (`boitier/`), intérieur (`interieur/`), mise en situation |
| 📚 **Sources & annexes** | [`docs/`](docs/) | Consigne, notice, archives des pistes non retenues |

### Lancer le POC

```bash
pip install numpy pillow
cd rebike-poc
python main.py            # mode démo : 3 cas + rapport
```

Sortie attendue : 3,50 mm → CONFORME · 2,40 mm → À SURVEILLER · 1,20 mm → À REMPLACER.
Détails : [`rebike-poc/README.md`](rebike-poc/README.md).

---

*Groupe Stanley Black & Decker — marque FACOM. Document à usage du partenariat Ynov × FACOM.*
