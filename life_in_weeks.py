"""
Life in Days, Weeks and Months

Version 1.0.0
"""

from common_utils import print_header

program = f"Life in Days, Weeks and Months"
print_header(program)

max_age = 90

age = int(input("What is your age?\n"))
remaining_age = max_age - age

remaining_age_in_days = remaining_age * 365
remaining_age_in_weeks = remaining_age * 52
remaining_age_in_months = remaining_age * 12

print(
    f"""
If maximum age is {max_age} then you have 
{remaining_age_in_days} days,
{remaining_age_in_weeks} weeks and 
{remaining_age_in_months} months remaining.
    """
)
