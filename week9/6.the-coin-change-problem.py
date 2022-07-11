#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

# Create array DP with val 0 with length n+1
# loop for c times, loop amount for 1 - len() + 1
# DP[amount] = DP[amount] + (DP[amount - coin] if amount >= coin else 0)
# return DP[len(c)-1]

def getWays(n : int, c: list[int]) -> int:
    DP = [1] + [0] * (n)
    for coin in c:
        for amount in range(1, n + 1):
            DP[amount] = DP[amount] + (DP[amount - coin] if amount - coin >= 0  else 0)
    return DP[-1]
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
