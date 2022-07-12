#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# the minimum is only when the order is ascending or descending
# create function that counts the number of swaps (min) needed to reach 
# the sorted order 

# function num_of_swaps(arr)
# keep all the original index in hashmap
# loop for i in sorted_arr
# if not the same : 
# extract the swap_array 
# update the arr[i] index to swap_array
# swap the array 
# count everytime it swaps, return the count

# return minimum of num_swaps if arr in normal and in reversed order

def lilysHomework(arr : list[int]) -> int:
    def num_swaps(arr : list[int]) -> int:
        hashmap = {}
        for i in range(len(arr)):
            hashmap[arr[i]] = i
        count = 0
        sorted_arr=  sorted(arr)
        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                # get the destination_idx of sorted_arr in arr by using hashmap
                swap_idx = hashmap[sorted_arr[i]]
                hashmap[arr[i]] = swap_idx
                count +=1
                arr[i] , arr[swap_idx] = arr[swap_idx] , arr[i]
        return count
    return min(num_swaps(arr[::]), num_swaps(arr[::-1]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
