"""
Check Prime Numbers.

Version 1.0.0
"""
from common_utils import print_header
import sys


list_of_primes = []


def prime_checker(number):
    for num in range(2, number):
        if number % num == 0:
            return False

    return True


try:
    number = int(input("Input an integer?\n"))
    print(f"Is {number} a Prime? {prime_checker(number)}")
except Exception as e:
    print("Incorrect input. Must be an integer.")
    sys.exit()
