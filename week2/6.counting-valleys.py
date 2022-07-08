#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# valley only counts if currently in below sea level, then rise up above or equal sea level


def countingValleys(steps: int, path: list[str]) -> int:
    is_currently_in_valley = False
    level = 0
    count_valley = 0
    for i in range(steps):
        if path[i] == 'U':
            level += 1
        else:
            level -= 1
        if not is_currently_in_valley and level < 0:
            is_currently_in_valley = True
        if is_currently_in_valley and level >= 0:
            is_currently_in_valley = False
            count_valley += 1
    return count_valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
