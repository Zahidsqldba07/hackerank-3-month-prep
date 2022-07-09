import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


# Strategy 3
# sort
# use sliding window,
# while right - left > k
# if arr[right] > arr[left], right -=1
# else: left +=1
# O(n)

def maxMin(k: int, arr: list[int]) -> int:
    arr.sort()
    min_dif = arr[k-1] - arr[0]
    for i in range(k, len(arr)):
        min_dif = min(min_dif, arr[i] -arr[i - (k-1)])
    return min_dif


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
