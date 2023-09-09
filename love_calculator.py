"""
Love calculator

Tests the compatibility between two people.

Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number and show it as percent.

Version 1.0.0
"""
from common_utils import print_header


program = f"Love Calculator"
print_header(program)

person1 = input("What is your name?\n").lower()
person2 = input("Whom do you love?\n").lower()

true_count = 0
love_count = 0

true_count += person1.count("t") + person2.count("t")
true_count += person1.count("r") + person2.count("r")
true_count += person1.count("u") + person2.count("u")
true_count += person1.count("e") + person2.count("e")

love_count += person1.count("l") + person2.count("l")
love_count += person1.count("o") + person2.count("o")
love_count += person1.count("v") + person2.count("v")
love_count += person1.count("e") + person2.count("e")

print(f"Your score is {true_count}{love_count}%.")
