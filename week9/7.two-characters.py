#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# create list of set of string
# loop for every pair of combination
# first, second 
# loop until find first or second
# then swap 
# if already meet, then loop until finish 
# if found candidates, must alternate,
# if loop and not alternate, dont check max

def alternate(s : str) -> int:
    combinations = list(set(s))
    max_length = 0
    for i in range(len(combinations)):
        for j in range(i+1, len(combinations)):
            first, second = combinations[i], combinations[j]
            # loop until find first occurence
            k = 0
            while s[k] != first and s[k] != second:
                k+=1
            count = 1    
            if s[k] == second:
                first, second = combinations[j], combinations[i] 
            prev = first 
            is_valid = True
            for z in range(k+1, len(s)):
                if s[z] == first or s[z] == second:
                    if s[z] == prev:
                        is_valid = False
                        break
                    prev = s[z]
                    count +=1
            if is_valid:
                max_length = max(max_length, count)
    
    return max_length
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
