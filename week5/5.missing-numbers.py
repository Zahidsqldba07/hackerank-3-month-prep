#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

# count occurence of brr char in hashmap
# loop arr, subtract count if found
# remove from hashmap if count == 0
# 

def missingNumbers(arr : list[list[int]], brr : list[list[int]]) -> list[int]:
    hashmap = {}
    for item in brr:
        hashmap[item] = hashmap.get(item,0) + 1 
    for number in arr:
        if number in hashmap:
            hashmap[number] -=1
            if hashmap[number] == 0:
                hashmap.pop(number)
    return sorted(hashmap.keys())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
