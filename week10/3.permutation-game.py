#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# DP memoizaton 
# findWinner -> true if array is sorted -> alice can't move -> bob win 
# findWinner -> False if array is 1 way off from sorted -> then sorted -> then Bob can't move -> Alice win 
# findWinner -> True if array is 2 way off sorted -> alice move-> bob move-> alice can't move 
# check if already in cache, if yes then return cache value
# check if already sorted, if yes then cached it, then return True, 

# if not, check for n combination inside arr, arr_new = arr without the number
# if if bob pick that number and findWinner True -> then alice win, (return False)

# if no moves anymore, bob still win 
# 

def is_sorted(arr: list[int]) -> bool:
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def permutationGame(arr : list[int]) -> str:
    cache = {}
    def findWinner(arr : list[int]) -> bool:
        key = tuple(arr)
        if key in cache:
            return cache[key]
        if is_sorted(arr):
            cache[key] = True
            return True
        for i in range(len(arr)):
            if findWinner(arr[:i] + arr[i+1:]) : 
                cache[key] = False
                return False
        # no move
        cache[key] = True
        return True
    return 'Bob' if findWinner(arr) else 'Alice'
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = permutationGame(arr)

        fptr.write(result + '\n')

    fptr.close()
