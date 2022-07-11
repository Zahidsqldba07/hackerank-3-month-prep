#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# kadane algorithm to subarray
# track min_negative
# if <0, ++ for max_subseq


def maxSubarray(arr : list[int]) -> list[int]:
    max_negative = arr[0]
    max_global, current_sum = arr[0] , 0
    max_subseq = 0
    for i in range(len(arr)):
        if current_sum < 0 :
            current_sum = 0 
        current_sum += arr[i]
        max_global = max(max_global, current_sum)
        if arr[i] > 0 :
            if max_subseq < 0 :
                max_subseq = 0 
            max_subseq += arr[i]
        if arr[i] <= 0 :
            max_negative = max(max_negative, arr[i])
    return [max_global, max_subseq if max_subseq != 0 else max_negative ]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
