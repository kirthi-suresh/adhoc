"""
Banker Roulette

Randomly pick who buys meals
"""

import random
from common_utils import print_header

header = f"Banker Roulette"
print_header(header)

people = (input("List all people separated by comma:\n")).split(",")

select = random.choice(people)

print(f"Bill will be payed by {select}.")
