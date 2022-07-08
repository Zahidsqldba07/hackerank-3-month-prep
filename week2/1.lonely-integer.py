#!/bin/python3

from functools import reduce
import itertools
import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

# find the unique element
# using reduce to xor all
# 0 ^ X = X
# X ^ X = 0
# A ^ A ^ B ^ C ^ C = B


def lonelyinteger(a: list[int]) -> int:
    return reduce(lambda x, y: x ^ y, a, 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
