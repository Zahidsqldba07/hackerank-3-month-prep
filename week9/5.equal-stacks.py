#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

# reverse h1, h2, h3
# create sum1, sum2, sum3 
# while sum of three not equal:
# get the min_sum
# if each of stack sum < min_sum, pop(), then decrease the sum

def equalStacks(h1 : list[int], h2 : list[int], h3 : list[int]) -> int:
    h1, h2, h3 = list(reversed(h1)), list(reversed(h2)), list(reversed(h3))
    sum1, sum2, sum3 = sum(h1), sum(h2), sum(h3)
    while not sum1 == sum2 == sum3:
        min_sum = min(sum1,sum2,sum3)
        if min_sum < sum1 : 
            sum1 -= h1.pop()
        if min_sum < sum2 : 
            sum2 -= h2.pop()
        if min_sum < sum3 : 
            sum3 -= h3.pop()

    return sum1
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
