import sys
from datetime import datetime, date

def calculate_age(birthdate_str: str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%d.%m.%Y").date()
    except ValueError:
        print(f"Fehler: Ungültiges Datumsformat '{birthdate_str}'. Erwartet wird dd.mm.yyyy")
        sys.exit(1)

    today = date.today()

    if birthdate > today:
        print("Fehler: Das Geburtsdatum liegt in der Zukunft.")
        sys.exit(1)

    # Calculate total days
    total_days = (today - birthdate).days

    # Split into years, months, days
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    # Corrections if negative
    if days < 0:
        months -= 1
        previous_month = (today.month - 1) if today.month > 1 else 12
        previous_month_year = today.year if today.month > 1 else today.year - 1
        days_in_prev_month = (date(previous_month_year, previous_month + 1, 1) - date(previous_month_year, previous_month, 1)).days
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    print(f"Das Alter ist {years} Jahre, {months} Monate und {days} Tage, das sind {total_days} Tage")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Aufruf: python3 alter.py dd.mm.yyyy")
        sys.exit(1)

    calculate_age(sys.argv[1])
