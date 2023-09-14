"""
Hang_an
The game

Version 1.0.0
"""

import common_utils
import requests
import os
import sys


def print_header():
    header = f"Hangman"
    os.system("clear")
    common_utils.print_header(header)
    print(f"Test: {word}")  # Comment line for game
    print(f"Lives left: {lives}")
    print(display_word)


# Get random word
data = requests.get("https://random-word-api.herokuapp.com/word")
if data.status_code == 200:
    word = data.text[2:-2]


length = len(word)
display_word = "_ " * length
word_list = list(display_word)
lives = 6

while lives:
    print_header()

    letter = input("\nGuess one letter: ")
    if len(letter) > 1 and letter.isalpha():
        print("Program terminated due to invalid input.")
        sys.exit()

    if letter in word:
        for location, chrctr in enumerate(word):
            if chrctr == letter:
                location = location * 2
                word_list[location] = letter
                display_word = "".join(word_list)
                length -= 1
        if length == 0:
            print_header()
            print("\nYou won!")
            break
    else:
        lives -= 1
else:
    print("\nYou lost!")
