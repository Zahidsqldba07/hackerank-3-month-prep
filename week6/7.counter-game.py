#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#


# Create function that find neast power of two
# track counter = 0
# while n != 0,
#   count +=1
#   n = n - nearestPowerTwo(n)
# count odd -> louise win


def counterGame(n: int) -> str:
    if n == 1:
        return 'Richard'

    def nearestPowerTwo(n):
        num = 1
        while num*2 < n:
            num *= 2
        return num

    count = 0
    while n != 1:
        count += 1
        n -= nearestPowerTwo(n)
    return 'Louise' if count % 2 != 0 else 'Richard'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
