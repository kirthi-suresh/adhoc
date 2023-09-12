"""
Coin Toss using Random library

Version 1.0.0
"""

import random
from common_utils import print_header


header = f"Coin Toss"
print_header(header)

toss = random.randint(0, 1)
if toss:
    print("Heads")
else:
    print("Tails")
