#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Create array size MAX_RANGE
# loop, count every number in array 
# return the array

MAX_RANGE = 100 

def countingSort(arr : list[int]) -> list[int]:
    counts = [0] * MAX_RANGE
    for i in range(len(arr)):
        counts[arr[i]] += 1
    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
