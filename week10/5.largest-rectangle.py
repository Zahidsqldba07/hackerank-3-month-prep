#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

# using stacks to track ascending tower that is lower than current tower
# loop for each tower 
# assign start_idx as i
# empty all the tower in stack that is greater than current tower
# when emptying, pop stack, count the max, then move back start idx (start = idx) 
# push (start, height) to stack 

# if stack is not empty, empty the stack while calculating the area and compare
# with the max area 

def largestRectangle(h : list[int]) -> int:
    max_area = 0 
    stack = []
    for i in range(len(h)):
        start = i 
        while len(stack) > 0 and stack[-1][1] > h[i]:
            idx, height = stack.pop()
            max_area = max(max_area , height * (i - idx))
            start = idx
        stack.append((start, h[i]))
    # if stacks not empty
    for (idx, height ) in stack:
        max_area = max(max_area , height * (len(h) - idx))
        
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
