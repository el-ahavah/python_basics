#!/usr/bin/env python3
"""CLI Calculator Suite"""


def get_numbers():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b


def power(a, b):
    return a ** b


MENU = """
========== CLI Calculator Suite ==========
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Exit
===========================================
"""

OPERATIONS = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("Modulus", modulus),
    "6": ("Power", power),
}


def main():
    while True:
        print(MENU)
        choice = input("Select an option (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid option. Please choose a number between 1 and 7.\n")
            continue

        name, func = OPERATIONS[choice]
        a, b = get_numbers()
        result = func(a, b)
        print(f"\n{name} Result: {result}\n")


if __name__ == "__main__":
    main()