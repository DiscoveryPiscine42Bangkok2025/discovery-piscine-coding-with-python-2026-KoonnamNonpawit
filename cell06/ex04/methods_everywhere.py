#!/usr/bin/env python3
import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    padding = 8 - len(s)
    print(s + 'Z' * padding)

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)