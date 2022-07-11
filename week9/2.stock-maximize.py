#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

# one pass O(n)
# loop backwards 
# find max_val, calculate profit  max_val - prices[i]
# total += profit


def stockmax(prices : list[int]) -> int:
    max_val = prices[len(prices) -1]
    total_profit = 0
    for i in reversed(range(len(prices)-1)):
        max_val = max(max_val, prices[i])
        profit = max_val - prices[i]
        total_profit += profit
    return total_profit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
