#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

alpha_occurences = [0] * 26

# ascci a=97 z=122
# count occurence 
# loop for array occurence
# if found value <= 1, continue
# if found value > 2, return NO
# if found value == 2,
# check can_subtract == yes, then value -=1 and continue
# else if value == 2 and cannot subtract, return NO
# return YES in the end

# count min_occurence, max_occurence
# if min() and max() the same, then YES
# else: there 2 case
# if min_occurence == 1 and min() -1 == 0 or min() -1 == max():
# return YES
# elif max_occurence == 1 and max()-1 == min()
# return YES 

def isValid(s : str) -> str:
    can_subtract = True
    biggest, smallest = float('-inf') , float('inf')
    max_freq, min_freq, non_zero_freq = 0,0, 0
    
    for char in s:
        alpha_occurences[ord(char) - 97] +=1

    # max min counting
    for element in alpha_occurences:
        biggest = max(biggest, element)
        if element > 0:
            smallest = min(smallest, element)
            non_zero_freq +=1
    print(alpha_occurences)
    # maxmin freq counting
    for element in alpha_occurences:
        if element == biggest:
            max_freq+=1
        if element == smallest: 
            min_freq+=1
    # check cond
    if biggest == smallest:
        return 'YES'
    elif biggest!= smallest and max_freq+min_freq != non_zero_freq : 
        return 'NO'
    else:
        if min_freq == 1 and (smallest - 1 == 0 or smallest - 1 == biggest):
            return 'YES'
        elif max_freq == 1 and biggest-1 == smallest:
            return 'YES'
        else:
            return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
