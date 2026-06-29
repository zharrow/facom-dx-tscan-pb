# Datasheets des composants clés

Déposer ici les **datasheets officielles** (PDF) des composants relevés à l'ouverture du SCANDIAG.
Nommage conseillé : `FONCTION_REFERENCE.pdf` (ex. `MCU_STM32F407VGT6.pdf`).

## À collecter le jour J (après relevé des sérigraphies)

- [ ] **MCU principal** — réf. réelle (hypothèse : STM32F4 + interface caméra DCMI)
- [ ] **Capteur caméra CMOS** — réf. réelle (hypothèse : OmniVision OV9712 / OV9281 / AR0144)
- [ ] **Module Bluetooth** — réf. réelle (hypothèse : Microchip RN4678 / u-blox / BlueGiga)
- [ ] **Diode laser** verte 510–530 nm + **driver laser**
- [ ] **Chargeur Li-ion** (hypothèse : MCP73831 / BQ2407x / TP4056)
- [ ] **Régulateurs / LDO** (rails 3,3 V + rails caméra 2,8 / 1,8 / 1,5 V)
- [ ] **Mémoire flash SPI** (hypothèse : Winbond W25Qxx)
- [ ] **Buzzer**, **LED RGB**, autres composants notables (IMU éventuel)

> Procédure : relever la sérigraphie (loupe/macro) → chercher la datasheet sur le site
> du fabricant → enregistrer ici → mettre à jour le tableau §4 du `DOSSIER_FINAL_FACOM.md`.
