#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

# n + n = 2n
# n ^ n = 0

# create binary representation
# count num of 0 in the right of MSB

# 10 = 1010

# converting to binary ...
# count num of zero, return power 2 of numzero


def sumXor(n: int):
    if n == 0:
        return 1
    binary = '{:b}'.format(n)
    count_zero = 0
    for char in binary:
        if char == '0':
            count_zero += 1
    return 2**count_zero


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
