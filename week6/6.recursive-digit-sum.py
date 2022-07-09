#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(string: str, k: int):
    numArray = string.split()
    if len(numArray) == 1:
        superDigitValue = int(string)
    else:
        sum_val = 0
        for i in range(numArray):
            sum_val += int(numArray[i])
        superDigitValue = sum_val
    superDigitTotal = str(superDigitValue*k)
    while len(superDigitTotal) > 1:
        # sum the digit
        sum_val = 0
        for digit in superDigitTotal:
            sum_val += int(digit)
        superDigitTotal = str(sum_val)
    return int(superDigitTotal)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
