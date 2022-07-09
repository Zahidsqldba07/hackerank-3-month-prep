#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

# t1 : 0
# t2 : 1
# n = 6
# T(3) = T(1) + (T2)^2
# i = i - 2
# T(i) = T(i-2) + T(i-1)^2
# i >= 3

# base case : T == 1 -> return 0
# T == 2 -> return 1
# return F(n-2) + F(n-1)**2

def fibonacciModified(t1, t2, n):
    if n == 1:
        return t1
    elif n == 2:
        return t2
    return fibonacciModified(t1, t2, n-2) + fibonacciModified(t1, t2, n-1)**2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
