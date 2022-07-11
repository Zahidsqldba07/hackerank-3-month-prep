#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

# use hashmap, key= complement, value = appereance
# loop for element in arr
# check if in hashmap, if yes, count += hashmap[key]
# store that item's complement (arr[i] +- k) in hashmap with ++ 

def pairs(k : int, arr : list[int]) -> int:
    hashmap = {}
    count = 0 
    for num in arr:
        if num in hashmap:
            count += hashmap[num]
        hashmap[num + k] = hashmap.get(num + k, 0) + 1
        hashmap[num - k] = hashmap.get(num - k, 0) + 1
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
