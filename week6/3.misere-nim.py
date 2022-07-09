#!/bin/python3

from functools import reduce
import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

# if number stones all the same:
# if len() is odd, FIRST else SECOND (if even, seco)


def misereNim(s: list[int]) -> str:
    xor = reduce((lambda x, y: x ^ y), s)
    if(max(s) == 1):
        return "First" if xor == 0 else "Second"
    else:
        return "Second" if xor == 0 else "First"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
