"""
Days in month

Depends on leap_year

Version 1.0.0
"""

from common_utils import print_header
from leap_year import leap_year


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year) and month == 2:
        return 29
    return month_days[month - 1]


def main():
    program = f"Days in a month"
    print_header(program)

    try:
        year = int(input("Enter a year: "))
        month = int(input("Enter a month (number only): "))
        if month < 1 and month > 12:
            0 / 0
        days = days_in_month(year, month)
        print(f"{year} has {days} in that month.")
    except Exception as e:
        print("Invalid input!")


if __name__ == "__main__":
    main()
