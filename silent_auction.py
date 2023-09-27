"""
Silent auction

Version 1.0.0
"""

import common_utils
import os
import sys
import time


def print_header(item, price):
    os.system("cls")
    header = f"Silent Auction - {item}. Bidding starts at ${price:.0f}"
    common_utils.print_header(header)


try:
    item = input("What is the item?\n")
    price = float(input("What is the bid starting price?\n"))
except Exception as e:
    print("Invalid input")
    sys.exit()

bids = True
stats = {}

while bids:
    print_header(item, price)

    key = input("Bidder's name?\n")
    try:
        value = float(input("Bidding amount?\n"))
    except Exception as e:
        print("Invalid bid.")
        time.sleep(2)
        continue

    if value < price:
        print("Invalid bid.")
        time.sleep(2)
        continue

    stats[key] = value

    check_bids = input("Any bids? (Y/N)\n")
    if check_bids.lower() == "n":
        bids = False


sold_to = max(stats, key=stats.get)
os.system("cls")
header = f"Bidding Auction"
common_utils.print_header(header)
print(f"{item} sold to {sold_to} for ${stats[sold_to]:.0f}.")
print(stats)
