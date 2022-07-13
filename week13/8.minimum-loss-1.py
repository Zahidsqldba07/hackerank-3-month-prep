#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#


# 3 1 2 
# 1 2 3 
# current : 2 , next : 3 , idx_current > idx_next (original array)

# use hashmap to keep index 
# sort list
# we only care about the 2 pair if current idx < prev _idx 
# if i

def minimumLoss(price : list[int]) -> int:
    hashmap = {}
    for i in range(len(price)):
        hashmap[price[i]] = i
    price.sort()
    min_val = sys.maxsize
    for i in range(len(price)-1):
        current_price = price[i]
        next_price = price[i+1]
        diff = next_price - current_price
        if hashmap[current_price] > hashmap[next_price]:
            min_val = min(min_val, diff)
    return min_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
