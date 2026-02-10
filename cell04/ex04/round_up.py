#!/usr/bin/env python3
import math

try:
    user_input = float(input("Give me a number: "))

    print(math.ceil(user_input))

except ValueError:
    print("Please enter a valid number.")