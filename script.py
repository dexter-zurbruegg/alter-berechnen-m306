import sys
from datetime import datetime, date

def berechne_alter(geburtstag_str: str):
    try:
        geburtstag = datetime.strptime(geburtstag_str, "%d.%m.%Y").date()
    except ValueError:
        print(f"Fehler: Ungültiges Datumsformat '{geburtstag_str}'. Erwartet wird dd.mm.yyyy")
        sys.exit(1)

    heute = date.today()

    if geburtstag > heute:
        print("Fehler: Das Geburtsdatum liegt in der Zukunft.")
        sys.exit(1)

    # Gesamttage berechnen
    differenz_tage = (heute - geburtstag).days

    # Jahre, Monate, Tage zerlegen
    jahre = heute.year - geburtstag.year
    monate = heute.month - geburtstag.month
    tage = heute.day - geburtstag.day

    # Korrekturen falls negativ
    if tage < 0:
        monate -= 1
        letzter_monat = (heute.month - 1) if heute.month > 1 else 12
        jahr_letzter_monat = heute.year if heute.month > 1 else heute.year - 1
        tage_im_monat = (date(jahr_letzter_monat, letzter_monat + 1, 1) - date(jahr_letzter_monat, letzter_monat, 1)).days
        tage += tage_im_monat

    if monate < 0:
        jahre -= 1
        monate += 12

    print(f"Das Alter ist {jahre} Jahre, {monate} Monate und {tage} Tage, das sind {differenz_tage} Tage")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Aufruf: python3 alter.py dd.mm.yyyy")
        sys.exit(1)

    berechne_alter(sys.argv[1])