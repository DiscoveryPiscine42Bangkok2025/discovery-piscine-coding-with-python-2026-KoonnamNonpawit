#!/usr/bin/env python3

try:
    print("Enter a number")
    number = int(input())

    for i in range(10):
        result = i * number
        print(str(i) + " x " + str(number) + " = " + str(result))

except ValueError:
    print("Please enter a valid number.")