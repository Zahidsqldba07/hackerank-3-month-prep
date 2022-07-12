#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

# O(q*n) -> Not fast enough
# create zeroes for length n 
# for each query, loop for range(a, b+1) adding the number
# for return max of arr

# O(q+n) -> prefix sum 
# create array of 0 with extra 1 pad in left and right 
# for each query, arr[a] = k; arr[b+1] = -k
# loop for n, calculate the current number, then compare to the max

def arrayManipulation(n : int, queries : list[list[int]]) -> int:
    max_val = float('-inf')
    arr = [0] * (n + 2)
    for a,b,k in queries: 
        arr[a] += k
        arr[b+1] -= k 
    temp = 0
    for i in range(0, n+2):
        temp = temp+arr[i]
        max_val = max(max_val, temp)
    return max_val
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
