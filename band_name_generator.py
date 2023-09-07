"""
Program to generate band name based on location and pet
"""
print("Band Name Generator")
print("+++++++++++++++++++")

location = input("Where do you live?\n")
pet = input("What is the name of your pet?\n")

print("-" * (28 + len(location) + len(pet)))
print(f" Your band name could be {location} {pet}. ")
print("-" * (28 + len(location) + len(pet)))