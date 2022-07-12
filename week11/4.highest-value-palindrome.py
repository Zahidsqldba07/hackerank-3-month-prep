#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

# mark to mark changes in each index
# 2 step :
# step 1 : making it palindrom first 
# check from left right to the middle, if different, make it the same
# change the lower number to the higher number, mark it to 1, then k-- 

# check if k<0 then no palindrome possible, return -1

# step2 : changing middle or outermost to 9 if its not nine
# check if it middle and k >= 1, change to 9 and k-- 
# if not middle, check if the numer pair <9, if yes, check if its already in mark,
# if not in mark and k>= 2, then change both to 9 and k -= 2
# if one of the is in mark and k>=1, change both to 9 and k--

def highestValuePalindrome(s : str, n : int, k : int) -> str:
    mark = [0] * n
    s = list(s)
    # step 1 
    left, right = 0, n-1
    while left <= right:
        if s[left] != s[right]:
            if s[left] < s[right]:
                s[left] = s[right]
                mark[left] = 1 
            else:
                s[right] = s[left]
                mark[right] = 1
            k -=1 
        left, right = left +1 , right -1
    if k < 0 :
        return '-1'
    left, right = 0, n-1
    # step 2
    while left <= right: 
        if left == right and k >= 1: 
            s[left] = '9'
            k -= 1
            break
        if s[left] < '9':
            if mark[left] == 0 and mark[right] == 0 and k>=2 :
                s[left] = s[right] = '9'
                k-=2
            if (mark[left] == 1 or mark[right] == 1) and k>=1 : 
                s[left] = s[right] = '9'
                k-=1
        left, right = left +1 , right -1
    return ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
