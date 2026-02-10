#!/usr/bin/env python3

try:
    num = float(input("Give me a number: "))

    if num % 1 == 0:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

except ValueError:
    print("This is not a valid number.")