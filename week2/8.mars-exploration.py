#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# if x % 3 ==0 or x %3 == 2 , check S
# if x % 3 == 1, check if O 
# if not correct, add counter

def marsExploration(s : str) -> int:
    count = 0 
    for i in range(len(s)):
        if i % 3 == 0 or i % 3 == 2: 
            if s[i] != 'S':
                count +=1
        else:
            if s[i] != 'O':
                count +=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
