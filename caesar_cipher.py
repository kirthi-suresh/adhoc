"""
Caesar Cipher

Version 1.0.0
"""
from common_utils import print_header
import os

alphabet = [
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
]


def encoder_decoder(option=1):
    try:
        msg = input("Message: ")
        shift = int(input("Shift: "))
        msg = msg.lower()
        encrypted_word = []
        for letter in msg:
            location = alphabet.index(letter)
            if option == 1:
                pointer = location + shift
                while pointer > 26:
                    pointer = abs(26 - pointer)
            else:
                pointer = location - shift
                while pointer < -26:
                    pointer = abs(26 - pointer)

            new_letter = alphabet[pointer]
            encrypted_word.append(new_letter)
        return "".join(encrypted_word)

    except Exception as e:
        print("Invalid input.\n")
        return None


header = f"Caesar Cipher"

switch = True

os.system("clear")
print_header(header)

while switch:
    try:
        choice = int(input("Choose an option: [1.Encode 2.Decode 0. Exit]\nChoice: "))
        if choice == 0:
            switch = False
        elif choice == 1:
            print("Encode")
            print(f"Encoded message: {encoder_decoder(1)}.\n")
        elif choice == 2:
            print("Decode")
            print(f"Decoded message: {encoder_decoder(2)}.\n")
        else:
            print("Not an option.\n")
    except Exception as e:
        print("Not an option.\n")
