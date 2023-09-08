"""
Calculate Body Mass Index

Version 1.0.0
"""

program = f"Calculate Body Mass Index"
print(program)
print("+" * len(program))

height = float(input("What is the height in m?\n"))
weight = float(input("What is the weight in kg?\n"))

bmi = weight / (height**2)

print(f"BMI is {round(bmi,1)}")
