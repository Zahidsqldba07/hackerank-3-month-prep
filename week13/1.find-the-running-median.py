#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import *

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

# use max_heap for left_half
# use min_heap for right_half
# if max_heap empty or number < maximum left_half then push to left half
# else, push to right half

# balance, to make sure the heap balance, or only up 1 element 
# append the result based on length of heap


def runningMedian(a : list[int]) -> list[float]:
    left_half = []
    right_half =[]
    res = []
    
    for i, number in enumerate(a):
        if not left_half or number < -left_half[0]:
            heappush(left_half, -number)
        else:
            heappush(right_half, number)
        # balancing
        if len(left_half) - len(right_half) >= 2:
            heappush(right_half, -heappop(left_half))
        if len(right_half) - len(left_half) >= 2:
            heappush(left_half, -heappop(right_half)) 
        
        if len(left_half) == len(right_half):
            res.append(float(- left_half[0] + right_half[0])/2)
        elif len(left_half) > len(right_half):
            res.append(float(-left_half[0]))
        else:
            res.append(float(right_half[0]))
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
