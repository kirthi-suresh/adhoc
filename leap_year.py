"""
Check if a year is leap year

Version 1.0.0
"""
from common_utils import print_header


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():
    program = f"Leap Year"
    print_header(program)

    try:
        year = int(input("What is the year?\n"))
        print(f"Is {year} a leap year? {leap_year(year)}")
    except Exception as e:
        print("Invalid input!")


if __name__ == "__main__":
    main()
