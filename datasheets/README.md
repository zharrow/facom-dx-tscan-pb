# Datasheets des composants clés

Composants **identifiés au teardown** (photos `../images_facom/interieur/`, nomenclature
au §3.2 du dossier). Ci-dessous les **liens officiels** vers les fiches techniques.

> Pour archiver les PDF en local, télécharger chaque fichier depuis le lien et l'enregistrer
> ici en respectant le nommage `FONCTION_REFERENCE.pdf`.

| Composant | Référence | Datasheet officielle |
|---|---|---|
| **MCU** | STMicroelectronics STM32F429 | <https://www.st.com/resource/en/datasheet/stm32f429zi.pdf> |
| **SDRAM** | ISSI IS42S16400J-6BLI (64 Mbit) | <https://www.issi.com/WW/pdf/42-45S16400J.pdf> |
| **Caméra** | OmniVision OV9712 (module `JAL-KM1-OV9712`) | <https://www.ovt.com/products/ov09712/> |
| **Bluetooth** | Silicon Labs / Bluegiga WT12 | <https://www.silabs.com/documents/public/data-sheets/WT12-DataSheet.pdf> |
| **Bluetooth (firmware)** | iWRAP (commandes AT) | <https://www.silabs.com/documents/public/user-guides/UG215-iWRAP-User-Guide.pdf> |
| **USB↔série** | FTDI FT232RQ | <https://ftdichip.com/wp-content/uploads/2020/08/DS_FT232R.pdf> |
| **Batterie** | EEMB LP602248 (LiPo 3,7 V / 620 mAh) | <https://www.eemb.com/battery/lithium-polymer-battery/LP602248.html> |
| **Laser (sécurité)** | classe 3R, 510–530 nm | IEC 60825-1:2014 (norme sécurité laser) |

## À identifier à la loupe (puis ajouter)

- Mémoire externe `9CA15 / RB151` (logo en vague) — probable flash NAND/NOR.
- `ON RM R934` (ON Semiconductor) — régulateur / load-switch / driver.
- Régulateurs / LDO secondaires (rails caméra 2,8 / 1,8 / 1,5 V).

## Note OEM

Le SCANDIAG® est une version **rebrandée du TEXA *Laser Examiner*** (TEXA S.p.A., Italie).
La documentation TEXA est une source complémentaire utile :
<https://www.texa.com/products/laser-examiner-2/>
