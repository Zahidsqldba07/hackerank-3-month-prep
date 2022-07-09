#!/bin/python3

import math
from operator import indexOf
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# find right = indexof.max() for the first move
# track the counter = 0
# while center >= 0
# right_boundary -=1
# count +=1
# right = indefofmax(arr)


# def gamingArray(arr: list[int]) -> str:
#     right_boundary = len(arr)
#     count = 0
#     while right_boundary > 0:
#         current_max_idx = arr.index(max(arr[:right_boundary]))
#         count += 1
#         right_boundary = current_max_idx
#     return 'BOB' if count % 2 != 0 else 'ANDY'

# track max value from left-right
def gamingArray(arr: list[int]) -> str:
    count = 0
    curr_max = float('-inf')
    for num in arr:
        if num > curr_max:
            curr_max = num
            count += 1
    return 'BOB' if count % 2 != 0 else 'ANDY'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
