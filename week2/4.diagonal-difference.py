#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# left-right diagonal = 0,0 -> 1,1 -> 2,2 for 3x3 matrix (i,i)
# right - left diagronal = 0,2 -> 1,1 -> 2,0 (i, len() - 1 - i)
# time complexity O(n) for nxn matrix

def diagonalDifference(arr : list[int]) -> int:
    left_right, right_left = 0, 0
    for i in range(len(arr)):
        left_right += arr[i][i]
        right_left += arr[i][len(arr) - 1 - i]
    return abs(left_right - right_left)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
