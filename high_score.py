"""
High Score Display

Version 1.0.0
"""

import random
from common_utils import print_header


header = f"High Score Display"
print_header(header)

students = ['Lily','Jason','Mike','Sarah']
scores = [94,76,83,80]

for i,student in enumerate(students):
    print(f"{student:6} - {scores[i]}")


highest_score = max(scores)
top_student = students[scores.index(highest_score)]

lowest_score = min(scores)
last_student = students[scores.index(lowest_score)]

print(f"{top_student} scores the highest with {highest_score} marks")
print(f"{last_student} scores the last with {lowest_score} marks")