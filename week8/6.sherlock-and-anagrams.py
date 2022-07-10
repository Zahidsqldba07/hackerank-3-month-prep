#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# example 1: anagram abcba
# (a,a) (ab, ba) 

# example 2 : 

#  0 1 2 3  2 = 4 - 2 + 1  

# Strategy
# Loop over all possible subset 
# loop i from 1 -> len()//2 + 1 -> max substring pair 
# for each number, loop j from 0 -> len() - i + 1 
# inside loop, check if sorted substring is in hashmap, is yes then count++ then hashmap[key] ++
# else: hashmap[key] = 1 

def sherlockAndAnagrams(s : str) -> int:
    hashmap = {}
    count = 0
    for i in range(1,len(s) + 1):
        for j in range(len(s) - i + 1):
            substring = str(''.join(sorted(s[j : j + i])))
            if substring in hashmap:
                count += hashmap[substring]
                hashmap[substring] += 1
            else:
                hashmap[substring] = 1
    return count
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
