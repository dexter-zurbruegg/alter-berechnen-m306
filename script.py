import sys
from datetime import datetime, date, timedelta

def calculate_age(birthdate_str: str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%d.%m.%Y").date()
    except ValueError:
        print(f"Fehler: Ungültiges Datumsformat '{birthdate_str}'. Erwartet wird dd.mm.yyyy oder ein falsches Datum wurde eingegeben. Bitte versuche es erneut.")
        sys.exit(1)

    today = date.today()

    if birthdate > today:
        print("Fehler: Das Geburtsdatum liegt in der Zukunft.")
        sys.exit(1)

    # calculate total days
    total_days = (today - birthdate).days

    # split into years, months, days
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    # handling exceptions (leap years)
    if days < 0:
        months -= 1
        first_of_this_month = date(today.year, today.month, 1)
        last_of_prev_month = first_of_this_month - timedelta(days=1)
        days_in_prev_month = last_of_prev_month.day
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    print(f"Das Alter ist {years} Jahre, {months} Monate und {days} Tage, das sind {total_days} Tage")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kein Argument gegeben. Erwartetes Format: dd.mm.yyyy")
        sys.exit(1)

    calculate_age(sys.argv[1])
