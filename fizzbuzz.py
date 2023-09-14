"""
Fizz Buzz
Print from 1 to 100
Number disible by 3 should show Fizz
Number disible by 5 should show Buzz

Version 1.0.0
"""


from common_utils import print_header

header = f"Fizz Buzz"
print_header(header)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
