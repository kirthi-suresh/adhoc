"""
Calculator

Version 1.0.0
"""

import os
import time
import common_utils


def print_header():
    os.system("cls")
    header = f"Calculator"
    common_utils.print_header(header)
    print("Operations supported are [ / *  -  + ]")


def add(n1: float, n2: float):
    return n1 + n2


def subtract(n1: float, n2: float):
    return n1 - n2


def multiply(n1: float, n2: float):
    return n1 * n2


def divide(n1: float, n2: float):
    if n2 != 0:
        return n1 / n2
    else:
        return None


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def main():
    run = True
    while run:
        print_header()

        print("Pick an operation:\n/\n*\n+\n-")
        select_operation = input("> ")

        while select_operation not in operations:
            print("Invalid input!")
            select_operation = input("> ")

        n1 = int(input("What' the first numbers? "))
        n2 = int(input("What' the second numbers? "))

        result = operations[select_operation](n1, n2)
        if result is None:
            print("Cannot divide by 0.")

        print(f"{n1} {select_operation} {n2} = {result}")

        if input("Press 'y' for another operation.\n").lower() != "y":
            run = False


if __name__ == "__main__":
    main()
