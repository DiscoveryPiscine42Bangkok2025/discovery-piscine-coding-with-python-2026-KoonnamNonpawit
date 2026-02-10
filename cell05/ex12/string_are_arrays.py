#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    input_str = sys.argv[1]

    result = ""
    for char in input_str:
        if char == 'z':
            result += "z"

    if len(result) > 0:
        print(result)
    else:
        print("none")

else:
    print("none")