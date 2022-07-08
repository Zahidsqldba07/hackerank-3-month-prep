#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# create of set from a-z
# lower the string, loop for each char, if found in set, remove from set
# if set is empty, return pangram, if not, return not pangram


def pangrams(s: str) -> str:
    sets = set()
    for i in range(97, 123):
        sets.add(chr(i))
    for char in s.lower():
        if char in sets:
            sets.remove(char)
    if len(sets) == 0:
        return 'pangram'
    else:
        return 'not pangram'

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
