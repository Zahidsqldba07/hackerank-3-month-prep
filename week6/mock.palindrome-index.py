#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# adbcba

def palindromeIndex(s : str) -> int:
    # check if already a palindrome
    if s == s[::-1]:
        return -1
    # if not, then loop check mirror 
    for i in range(len(s)//2):
        q = len(s) - 1 - i
        # check if char the same
        if s[i] != s[q]:
            # check if left is ignored, 
            if s[i+1:q+1] == s[i+1:q+1][::-1]:
                return i
            # check if right is ignored
            elif s[i:q] == s[i:q][::-1]:
                return q
    return -1
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
