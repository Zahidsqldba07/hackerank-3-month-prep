#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Strat 1 
# sort arr, then min diff is adjadent pair, because 
# if a <= b <= c, then |a-b| <= |a-c|

def minimumAbsoluteDifference(arr : list[int]) -> int:
    arr.sort()
    smallest = float('inf')
    for i in range(len(arr)-1):
        smallest = min(smallest, abs(arr[i+1] - arr[i]))
    return smallest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
