#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

# sort
# create hashmap of all false
# use the greedy approach
# loop the element,
# for each element, check in hashmap, if yes then continue
# if not, then loop from i+k to i+1 for any item in hashmap
# for that hashmap, loop for k times to set i - k < x < i + k to True


def hackerlandRadioTransmitters(x: list[int], k: int):
    x.sort()
    count = 0
    hashmap = {}
    for item in x:
        hashmap[item] = False
    for i in range(len(x)):
        if x[i] in hashmap and hashmap[x[i]]:
            continue
        for j in range(x[i]+k, max(x[i]-1, 0), -1):
            if j in hashmap:
                for l in range(j-k, j+k+1):
                    hashmap[l] = True
                break
        count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
