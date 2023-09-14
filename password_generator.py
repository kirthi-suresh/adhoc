"""
Password Generator
Input: number of letters, numbers, and symbols
Output: random combination of input
Version 1.0.0
"""

import random
from common_utils import print_header

header = f"Password Generator"
print_header(header)

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


total_letters = int(input("How many letters would you like in your password?\n"))
total_symbols = int(input(f"How many symbols would you like?\n"))
total_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for position in range(0, total_letters):
    password += random.choice(letters)
for position in range(0, total_numbers):
    password += random.choice(numbers)
for position in range(0, total_symbols):
    password += random.choice(symbols)

password = list(password)
random.shuffle(password)
password = "".join(password)

print(f"Password: {password}")
