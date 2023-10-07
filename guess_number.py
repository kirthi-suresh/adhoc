"""
Guess the Number

Version 1.0.0
"""

import common_utils
from random import randint

header = f"Guess the number"
common_utils.print_header(header)

checkpoint = True
while checkpoint:
    try:
        mode = int(input("Select game mode\n1. easy\n2. hard\n> "))
        if mode == 1 or mode == 2:
            checkpoint = False
        else:
            print("Invalid input!")
    except Exception as e:
        print("Invalid input!")

if mode == 2:
    attempts = 5
    print("Hard Mode")
else:
    attempts = 10
    print("Easy Mode")

winning_number = randint(1, 100)

won = False
while attempts != 0 and not won:
    checkpoint = True
    while checkpoint:
        try:
            guess = int(input("Guess the winning number (1-100) "))
            if guess > 0 and guess < 101:
                checkpoint = False
            else:
                print("Invalid input!")
        except Exception as e:
            print("Invalid input!")

    if guess == winning_number:
        won = True
        print("You won!")
    elif guess > winning_number:
        print("Too high!")
    else:
        print("Too low!")

    attempts -= 1
    print(f"Attempts left: {attempts}")

if attempts == 0:
    print("You lost!")
