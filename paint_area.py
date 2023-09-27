"""
Calculate paint required for an area.

Version 1.0.0
"""
from common_utils import print_header
import math


def paint_area_calc(height, width, coverage):
    if coverage:
        return (height * width) / coverage
    else:
        return None


program = f"Paint Area"
print_header(program)

height_of_wall = float(input("Height of the wall?\n"))
width_of_wall = float(input("Width of the wall?\n"))
paint_can_coverage = 5

paint_cans = paint_area_calc(height_of_wall, width_of_wall, paint_can_coverage)
paint_cans = math.ceil(paint_cans)

print(f"{paint_cans} cans of paint are required.")
