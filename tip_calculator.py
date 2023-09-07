"""
Tip Calculator
Version 1.0.0

Get total bill
Get total people
Get percent of tip
Give how much each person should pay
"""

print("Tip Calculator")
print("+" * 14)

total_bill = float(input("What was the total bill?\n$"))
people_count = float(input("How many people to split the bill?\n"))
tip_percent = float(
    input("What percent tip would you like to give? 10, 12, 15 or 18?\n")
)

bill_per_person = total_bill / people_count
tip_per_person = bill_per_person * (tip_percent / 100)
each_pay = bill_per_person + tip_per_person

print(f"Each person should pay ${each_pay:.2f}")
