#!/usr/bin/env python3
"""
scandiag_client.py — Client / explorateur série pour FACOM SCANDIAG (= TEXA Laser Examiner).

POC Palier 1 (sans reflash) : l'outil expose sa liaison Bluetooth comme un PORT SÉRIE
(profil SPP côté Windows : port COM ; côté Linux : /dev/rfcomm0). Le protocole applicatif
est PROPRIÉTAIRE et inconnu au départ : cet outil sert donc d'abord à le RÉTRO-CONCEVOIR
(observer, journaliser, rejouer), puis à le piloter une fois décodé.

Modes :
  ports     : lister les ports série disponibles
  monitor   : écouter et journaliser tout ce que l'outil envoie (hex + ASCII)
  repl      : console interactive pour envoyer des trames (hex ou texte) et voir les réponses
  replay    : rejouer une trame capturée (octets en hex) et afficher la réponse

Dépendances : pip install pyserial
Usage rapide :
  python scandiag_client.py ports
  python scandiag_client.py monitor --port /dev/rfcomm0 --baud 115200 --log capture.log
  python scandiag_client.py repl    --port COM5        --baud 115200
  python scandiag_client.py replay  --port COM5 --hex "AA 01 02 55"

⚠️ Le baudrate (115200 par défaut) est une HYPOTHÈSE : à confirmer (essayer 9600, 38400,
57600, 115200, 230400). Sur un lien SPP/BLE « transparent », le baudrate côté PC est souvent
ignoré, mais on le fixe par convention.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import sys
import time

try:
    import serial               # pyserial
    from serial.tools import list_ports
    _HAS_SERIAL = True
except ImportError:                 # autorise --help / parsing sans la dépendance
    serial = None                   # type: ignore
    list_ports = None               # type: ignore
    _HAS_SERIAL = False


def _require_serial() -> None:
    if not _HAS_SERIAL:
        sys.exit("pyserial manquant. Installez-le :  pip install pyserial")


# --------------------------------------------------------------------------- #
# Utilitaires d'affichage / journalisation
# --------------------------------------------------------------------------- #
def _ts() -> str:
    return _dt.datetime.now().strftime("%H:%M:%S.%f")[:-3]


def hexdump(data: bytes, width: int = 16) -> str:
    """Rendu type `hexdump -C` : offset, octets en hex, et colonne ASCII."""
    lines = []
    for off in range(0, len(data), width):
        chunk = data[off:off + width]
        hexs = " ".join(f"{b:02X}" for b in chunk).ljust(width * 3 - 1)
        ascii_ = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        lines.append(f"{off:08X}  {hexs}  |{ascii_}|")
    return "\n".join(lines) if lines else "(vide)"


def parse_payload(text: str) -> bytes:
    """Interprète une saisie utilisateur.

    - Préfixe 'hex:' ou suite d'octets hex ("AA 01 55", "AA0155")  -> octets bruts.
    - Préfixe 'txt:'                                               -> texte ASCII + \\r\\n.
    - Sinon : tente hex, à défaut traite comme texte.
    """
    s = text.strip()
    if s.lower().startswith("txt:"):
        return (s[4:] + "\r\n").encode("latin-1")
    if s.lower().startswith("hex:"):
        s = s[4:]
    cleaned = s.replace(" ", "").replace(",", "").replace("0x", "")
    try:
        return bytes.fromhex(cleaned)
    except ValueError:
        return (s + "\r\n").encode("latin-1")


class Logger:
    """Journalise à l'écran et, en option, dans un fichier."""
    def __init__(self, path: str | None):
        self._fh = open(path, "a", encoding="utf-8") if path else None
        if self._fh:
            self._fh.write(f"\n===== Session {_dt.datetime.now().isoformat()} =====\n")

    def line(self, msg: str) -> None:
        print(msg)
        if self._fh:
            self._fh.write(msg + "\n")
            self._fh.flush()

    def close(self) -> None:
        if self._fh:
            self._fh.close()


# --------------------------------------------------------------------------- #
# Connexion série
# --------------------------------------------------------------------------- #
def open_serial(port: str, baud: int, timeout: float = 0.2):
    _require_serial()
    try:
        ser = serial.Serial(port=port, baudrate=baud, timeout=timeout)
    except serial.SerialException as exc:
        sys.exit(f"Impossible d'ouvrir {port} @ {baud} : {exc}")
    print(f"[+] Ouvert {port} @ {baud} bauds (timeout {timeout}s). Ctrl-C pour quitter.")
    return ser


# --------------------------------------------------------------------------- #
# Modes
# --------------------------------------------------------------------------- #
def cmd_ports(_args) -> None:
    _require_serial()
    ports = list(list_ports.comports())
    if not ports:
        print("Aucun port série détecté. Appairez l'outil en Bluetooth, "
              "puis (Linux) :  sudo rfcomm bind 0 <MAC_BT> 1")
        return
    print("Ports série disponibles :")
    for p in ports:
        print(f"  {p.device:20} {p.description}  [{p.hwid}]")


def cmd_monitor(args) -> None:
    """Écoute passive : idéal pour capturer ce que l'outil émet quand on appuie sur le bouton."""
    log = Logger(args.log)
    ser = open_serial(args.port, args.baud)
    log.line(f"[monitor] {args.port} @ {args.baud} — appuyez sur le bouton de l'outil "
             f"pour déclencher une mesure...")
    buf = bytearray()
    try:
        while True:
            data = ser.read(4096)
            if data:
                buf.extend(data)
                log.line(f"\n[{_ts()}] +{len(data)} octets (total {len(buf)}) :")
                log.line(hexdump(data))
            else:
                time.sleep(0.02)
    except KeyboardInterrupt:
        log.line(f"\n[monitor] arrêt. {len(buf)} octets capturés au total.")
    finally:
        ser.close()
        log.close()


def cmd_repl(args) -> None:
    """Console interactive : on tape une trame, on lit la réponse."""
    log = Logger(args.log)
    ser = open_serial(args.port, args.baud)
    print("REPL — saisissez des octets hex ('AA 01 55'), 'txt:UNE_COMMANDE', "
          "ou 'q' pour quitter.")
    try:
        while True:
            try:
                raw = input("scandiag> ").strip()
            except EOFError:
                break
            if raw.lower() in ("q", "quit", "exit"):
                break
            if not raw:
                continue
            payload = parse_payload(raw)
            ser.reset_input_buffer()
            ser.write(payload)
            log.line(f"[{_ts()}] TX {len(payload)} octets :\n{hexdump(payload)}")
            time.sleep(0.3)                      # laisse l'outil répondre
            resp = ser.read(8192)
            if resp:
                log.line(f"[{_ts()}] RX {len(resp)} octets :\n{hexdump(resp)}")
            else:
                log.line(f"[{_ts()}] RX (aucune réponse)")
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()
        log.close()


def cmd_replay(args) -> None:
    log = Logger(args.log)
    ser = open_serial(args.port, args.baud)
    payload = parse_payload("hex:" + args.hex)
    ser.reset_input_buffer()
    ser.write(payload)
    log.line(f"[{_ts()}] TX {len(payload)} octets :\n{hexdump(payload)}")
    time.sleep(0.5)
    resp = ser.read(16384)
    log.line(f"[{_ts()}] RX {len(resp)} octets :\n{hexdump(resp)}")
    ser.close()
    log.close()


# --------------------------------------------------------------------------- #
# TODO (à compléter une fois le protocole décodé — TP3/TP4)
# --------------------------------------------------------------------------- #
def trigger_measurement(ser) -> bytes:
    """Déclenche une mesure et renvoie la réponse brute.

    À IMPLÉMENTER après rétro-ingénierie du protocole (mode 'monitor' + capture du
    logiciel officiel). Remplacer CMD_MEASURE par la vraie trame observée.
    """
    CMD_MEASURE = b""        # TODO: trame réelle, ex. b"\xAA\x01...\x55"
    if not CMD_MEASURE:
        raise NotImplementedError(
            "Protocole non encore décodé : utilisez d'abord 'monitor' pour capturer "
            "la trame de mesure, puis renseignez CMD_MEASURE.")
    ser.reset_input_buffer()
    ser.write(CMD_MEASURE)
    time.sleep(0.5)
    return ser.read(16384)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main() -> None:
    parser = argparse.ArgumentParser(description="Client/explorateur série SCANDIAG (POC Palier 1).")
    sub = parser.add_subparsers(dest="mode", required=True)

    sub.add_parser("ports", help="lister les ports série").set_defaults(func=cmd_ports)

    def add_serial_args(p):
        p.add_argument("--port", required=True, help="ex. /dev/rfcomm0 ou COM5")
        p.add_argument("--baud", type=int, default=115200, help="défaut 115200 (HYPOTHÈSE)")
        p.add_argument("--log", default=None, help="fichier de journalisation (optionnel)")

    p_mon = sub.add_parser("monitor", help="écouter/journaliser les émissions de l'outil")
    add_serial_args(p_mon); p_mon.set_defaults(func=cmd_monitor)

    p_repl = sub.add_parser("repl", help="console interactive d'envoi de trames")
    add_serial_args(p_repl); p_repl.set_defaults(func=cmd_repl)

    p_rep = sub.add_parser("replay", help="rejouer une trame hex et lire la réponse")
    add_serial_args(p_rep)
    p_rep.add_argument("--hex", required=True, help='trame hex, ex. "AA 01 02 55"')
    p_rep.set_defaults(func=cmd_replay)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
