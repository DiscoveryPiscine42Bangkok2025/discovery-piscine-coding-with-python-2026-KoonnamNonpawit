#!/usr/bin/env python3

user_input = input()

try:
    number = int(user_input)

    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("This is not a valid number.")