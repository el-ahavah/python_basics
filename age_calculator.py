"""
Age Calculator
Calculates exact age in years, months, and days from a birth date,
along with total days lived and days until the next birthday.
"""

from datetime import date


def calculate_age(birth_date: date, on_date: date = None) -> dict:
    """
    Calculate age given a birth date.

    Args:
        birth_date: The date of birth.
        on_date: The date to calculate age on (defaults to today).

    Returns:
        A dictionary with years, months, days, total_days, and
        days_until_next_birthday.
    """
    if on_date is None:
        on_date = date.today()

    if birth_date > on_date:
        raise ValueError("Birth date cannot be in the future.")

    years = on_date.year - birth_date.year
    months = on_date.month - birth_date.month
    days = on_date.day - birth_date.day

    if days < 0:
        months -= 1
        # Get number of days in the previous month
        if on_date.month == 1:
            prev_month = 12
            prev_year = on_date.year - 1
        else:
            prev_month = on_date.month - 1
            prev_year = on_date.year

        if prev_month == 2 and (prev_year % 4 == 0 and (prev_year % 100 != 0 or prev_year % 400 == 0)):
            days_in_prev_month = 29
        else:
            days_in_prev_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][prev_month - 1]

        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    total_days = (on_date - birth_date).days

    # Calculate days until next birthday
    try:
        next_birthday = birth_date.replace(year=on_date.year)
    except ValueError:
        # Handles Feb 29 birthdays on non-leap years
        next_birthday = birth_date.replace(year=on_date.year, day=28)

    if next_birthday < on_date:
        try:
            next_birthday = birth_date.replace(year=on_date.year + 1)
        except ValueError:
            next_birthday = birth_date.replace(year=on_date.year + 1, day=28)

    days_until_next_birthday = (next_birthday - on_date).days

    return {
        "years": years,
        "months": months,
        "days": days,
        "total_days": total_days,
        "days_until_next_birthday": days_until_next_birthday,
        "next_birthday": next_birthday,
    }


def parse_date_input(prompt: str) -> date:
    """Prompt the user for a date in YYYY-MM-DD format and return a date object."""
    while True:
        raw = input(prompt).strip()
        try:
            year, month, day = (int(part) for part in raw.split("-"))
            return date(year, month, day)
        except (ValueError, TypeError):
            print("Please enter the date in YYYY-MM-DD format, e.g. 1995-08-23.")


def main():
    print("=== Age Calculator ===\n")
    birth_date = parse_date_input("Enter your birth date (YYYY-MM-DD): ")

    try:
        result = calculate_age(birth_date)
    except ValueError as e:
        print(f"\nError: {e}")
        return

    print(f"\nYou are {result['years']} years, {result['months']} months, "
          f"and {result['days']} days old.")
    print(f"Total days lived: {result['total_days']:,}")
    print(f"Next birthday: {result['next_birthday'].strftime('%B %d, %Y')} "
          f"({result['days_until_next_birthday']} days away)")


if __name__ == "__main__":
    main()