"""
Hang_an
The game

Version 1.0.0
"""


from common_utils import print_header
import requests
import os

header = f"Hangman"

# Get random word
data = requests.get("https://random-word-api.herokuapp.com/word")
if data.status_code == 200:
    word = data.text[2:-2]


length = len(word)
display_word = "_ " * length
word_list = list(display_word)
lives = 6

while lives:
    os.system("clear")
    print_header(header)
    print(word)
    print(lives)
    print(display_word)

    letter = input("\nGuess: ")
    if letter in word:
        for loc, l in enumerate(word):
            if l == letter:
                loc = loc * 2
                word_list[loc] = letter
                display_word = "".join(word_list)
                length -= 1
        if length == 0:
            print("\nYou won!")
            break
    else:
        lives -= 1
else:
    print("\nYou lost!")
