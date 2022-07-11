#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def legoBlocks(height: int, width : int)->int:
    mod = 10 ** 9 + 7
    all = [0] * (width + 1)
    all[0] = 1
    for w in range(1, width + 1):
        all[w] = sum(all[max(0, w - 4):w])
        all[w] %= mod
    for w in range(width + 1):
        all[w] = all[w] ** height
        all[w] %= mod
    valid = all[:]
    for w in range(len(valid)):
        for separator in range(1, w):
            valid[w] -= valid[separator] * all[w-separator]
        valid[w] %= mod
    return valid[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
