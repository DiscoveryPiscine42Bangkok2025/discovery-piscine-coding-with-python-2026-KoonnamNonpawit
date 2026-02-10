#!/usr/bin/env python3

try:
    print("Enter a number less than 25")
    user_input = int(input())

    if user_input > 25:
        print("Error")
    else:
        while user_input <= 25:
            print("Inside the loop, my variable is", user_input)
            user_input += 1

except ValueError:
    print("That is not a valid number.")