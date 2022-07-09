#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

# loop for each string in grid, split to get n char
# sort ascending
# join again
# loop for i in len(grid)
# check for each column order, if any of the column not ascending, return 'NO'
# return 'YES'
# time O(n) space O(1)


def gridChallenge(grid: list[str]):
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    for col in range(len(grid[0])):
        for row in range(len(grid)-1):
            is_sorted = True
            if grid[row][col] > grid[row+1][col]:
                is_sorted = False
            if not is_sorted:
                return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
