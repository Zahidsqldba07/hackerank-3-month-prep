#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

# sort, then loop one pass O(nlogn)

# use set to track occurence


def sockMerchant(n :int, ar : list[int])-> int:
    sets = set()
    count = 0
    for item in ar:
        if item not in sets:
            sets.add(item)
        else:
            count += 1  
            sets.remove(item)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
