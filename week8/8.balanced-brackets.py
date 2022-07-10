#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# create pair map
# loop for each char in string 
# check if left side -> push to stack
# if right side (use pair map to check) -> check if can close 
# if complement of bracket == stack[-1] -> pop stack, else return NO
# return YES if len(stack) == 0 else NO

pair_map = {
    ')' : '(',
    ']' : '[',
    '}' : '{'
}

def isBalanced(s :str) -> str:
    stack = []
    for char in list(s) :
        if char not in pair_map:
            stack.append(char)
        else: # s is a complement
            # check if can close 
            if len(stack) > 0 and pair_map[char] == stack[-1]:
                stack.pop()
            else:
                return 'NO'
    return 'YES' if len(stack) == 0 else 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
