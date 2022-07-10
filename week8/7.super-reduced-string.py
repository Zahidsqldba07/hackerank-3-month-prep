#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# for for each char in string
# use stack to check adjacent char, if found, pop()

def superReducedString(s : str) -> str:
    string_array = list(s)
    stack = []
    for char in s:
        # check if peek() stack the same as char, if same pop() then skip 
        # else: push char into stack 
        if len(stack) > 0 and char == stack[-1]:
            stack.pop()
            continue
        else: 
            stack.append(char)
    return ''.join(stack) if len(stack)>0 else 'Empty String'
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
