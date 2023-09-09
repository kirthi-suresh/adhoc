"""
Number is even or odd

Version 1.0.0
"""

from common_utils import print_header


program = f"Even or Odd"
print_header(program)

number = int(input("Enter an integer:\n"))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
