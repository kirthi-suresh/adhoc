"""
Calculate Body Mass Index

Version 1.0.1
"""
from common_utils import print_header


program = f"Calculate Body Mass Index"
print_header(program)

height = float(input("What is the height in m?\n"))
weight = float(input("What is the weight in kg?\n"))

bmi = weight / (height**2)

print(f"BMI is {bmi:.1f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Clinically obese")
