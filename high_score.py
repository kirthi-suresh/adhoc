"""
High Score Display

Version 1.0.0
"""

import random
from common_utils import print_header


header = f"High Score Display"
print_header(header)

student = ['Lily','Jason','Mike','Sarah']
score = [94,76,83,80]

subject = zip(student,score)

highest_score = 0
lowest_score = 100
top_student = ''
last_student = ''

print("Marks:")
for student, score in subject:
    if score > highest_score:
        highest_score = score
        top_student = student
    if score < lowest_score:
        lowest_score = score
        last_student = student
    print(f"{student:10} - {score}")

print(f"{top_student} scores the highest with {highest_score} marks")
print(f"{last_student} scores the last with {lowest_score} marks")