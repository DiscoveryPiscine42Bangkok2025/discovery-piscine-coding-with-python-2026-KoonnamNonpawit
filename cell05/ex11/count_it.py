#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("parameters: " + str(len(sys.argv) - 1))

    for param in sys.argv[1:]:
        print(param + ": " + str(len(param)))

else:
    print("none")