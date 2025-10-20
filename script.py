import sys
from datetime import datetime, date, timedelta

def calculate_age(birthdate_str: str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%d.%m.%Y").date()
    except ValueError:
        print(f"Fehler: Ungültiges Datumsformat '{birthdate_str}'. Erwartet wird dd.mm.yyyy oder ein falsches Datum wurde eingegeben. Bitte versuche es erneut.")
        return

    # today's date is saved in the variable "today" and used for later calculations
    today = date.today()

    if birthdate > today:
        print(f"Fehler: Das Geburtsdatum '{birthdate_str}' liegt in der Zukunft.")
        return

    # calculate total days
    total_days = (today - birthdate).days

    # split into years, months, days
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    # handling negative days, if the birthday hasn't occurred yet in that month
    # example: today is March 5, Birthday is February 20, 5-20 equals a negative 15
    if days < 0:
        # reducing the month due to borrowing days from the previous month
        months -= 1
        first_of_this_month = date(today.year, today.month, 1)
        last_of_prev_month = first_of_this_month - timedelta(days=1)
        days_in_prev_month = last_of_prev_month.day
        days += days_in_prev_month

    # handling negative months
    if months < 0:
        years -= 1
        months += 12

    print(f"{birthdate_str}: Das Alter ist {years} Jahre, {months} Monate und {days} Tage, das sind {total_days} Tage")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kein Argument gegeben. Erwartetes Format: python3 alter.py dd.mm.yyyy [dd.mm.yyyy ...]")
        sys.exit(1)

    # process each birthday argument in batch
    for birth_arg in sys.argv[1:]:
        calculate_age(birth_arg)
