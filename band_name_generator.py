"""
Generate band name by combining city and pet
Version 1.0.0

"""

print("Band Name Generator")
print("+++++++++++++++++++")

city = input("Where do you live?\n")
pet = input("What is the name of your pet?\n")

print("-" * (28 + len(city) + len(pet)))
print(f" Your band name could be {city} {pet}. ")
print("-" * (28 + len(city) + len(pet)))
