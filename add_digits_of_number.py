"""
Add the digits of a number.

Version 1.0.0
"""

program = f"Add digits of a number"
print(program)
print("+" * len(program))
number = input("Enter the number:\n")
digits = [int(i) for i in number]
sum_of_digits = 0
for i in digits:
    sum_of_digits += i

print(f"Sum of digits is {sum_of_digits}")
