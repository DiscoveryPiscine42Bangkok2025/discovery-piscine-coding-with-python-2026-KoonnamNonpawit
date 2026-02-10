#!/usr/bin/env python3

try:
    first_num = int(input("Give me the first number: "))
    second_num = int(input("Give me the second number: "))

    print("Thank you!")

    print(str(first_num) + " + " + str(second_num) + " = " + str(first_num + second_num))

    print(str(first_num) + " - " + str(second_num) + " = " + str(first_num - second_num))

    if second_num != 0:
        print(str(first_num) + " / " + str(second_num) + " = " + str(int(first_num / second_num)))
    else:
        print(str(first_num) + " / " + str(second_num) + " = Error (Division by zero)")

    print(str(first_num) + " * " + str(second_num) + " = " + str(first_num * second_num))

except ValueError:
    print("Please enter valid numbers.")