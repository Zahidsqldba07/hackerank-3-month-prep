#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# 1. elemnts of a are all factors of integer X, X%A[i] == 0 for 0<i<len(A)
# 2. Integer X is a factor of all Element B, B[i]%X == 0 for 0<i<len(B)
# it means that X cannot be bigger than max(B) 

# Strategy 1
# from B, find a factor X that suits factor of all ement,
# if loop done and OK, check if X can be factored by A 


def getTotalX(a, b):
    count = 0
    for x in range(1, max(b)+1):
        # check if x is factor of all emenet B
        is_ok_b = True
        for i in range(len(b)):
            if b[i] % x != 0:
                is_ok_b = False
        # check if x are all factors of integer X
        is_ok_a = True
        for i in range(len(a)):
            if x % a[i] != 0:
                is_ok_a = False
        if is_ok_a and is_ok_b:
            count +=1
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
