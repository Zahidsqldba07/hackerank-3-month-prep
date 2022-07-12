#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

# This strategy only get 60 on submission because of the time limit

# using 1D DP Bottom-Up Approach with LCS (Longest Common Subsequence) method
# create DP 0 with length L2 
# loop for number s1, loop i for number s2
# store prev = 0 
# for each j(1, len(s2) + 1) : 
# store temp for current element before modification
# check if char the same, if yes then DP[j] = prev + 1
# else then DP[j] = max(DP[j], DP[j-1])
# prev = temp

def commonChild(s1 : str, s2 : str) -> int:
    DP = [0] * (len(s2) + 1)
    max_val = 0
    for i in range(1, len(s1)+1):
        prev = 0
        for j in range(1, len(s2)+1):
            temp = DP[j]
            if s1[i-1] == s2[j-1]:
                DP[j] = 1  + prev
            else:
                DP[j] = max(DP[j] , DP[j-1])
            max_val = max(max_val, DP[j])
            prev = temp 
    return max_val
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
