#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beadOrnaments' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY b as parameter.
#

def beadOrnaments(b : int) -> int:
    # Uses cayley's formula
    ans = 1
    summ = 0
    for bead in b:  
        ans = ans * (bead **(bead-1))
        summ = summ + bead
    if (len(b) - 2 >= 0):
        ans *= summ ** (len(b) - 2)
    else:
        ans = ans // summ
    return ans %  1000000007
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        b_count = int(input().strip())

        b = list(map(int, input().rstrip().split()))

        result = beadOrnaments(b)

        fptr.write(str(result) + '\n')

    fptr.close()
