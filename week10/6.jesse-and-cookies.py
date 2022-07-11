#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import *

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#


def cookies(k : int, A : list[int]) -> int:
    # heapify A
    # while smallest element is < k:
    # check if len() < 2, if yes return -1
    # pop 2 times to get first and second
    # pushheap the computed value
    heapify(A)
    count = 0
    while A[0] < k:
        if len(A) < 2 : return -1
        first = heappop(A)
        second = heappop(A)
        heappush(A, first + 2*second)
        count +=1
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
