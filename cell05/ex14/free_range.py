#!/usr/bin/env python3
import sys

if len(sys.argv) == 3:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])

        # range ปกติจะไม่เอาตัวสุดท้าย
        result_list = list(range(start, end + 1))

        print(result_list)

    except ValueError:
        print("none")
else:
    print("none")