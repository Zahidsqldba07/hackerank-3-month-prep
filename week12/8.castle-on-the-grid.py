#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid : list[str], startX: int , startY: int, goalX: int, goalY: int):
    c= 0
    visit= set()
    q = deque([[startX, startY, c]])
    # create array of moves
    moves = [[1,0], [-1,0], [0,1], [0,-1]]
    
    while q:
        path_x, path_y, c = q.popleft()
        c += 1 
        
        for xi, yi in moves:
            x,y = path_x, path_y
            while True:
                x,y = x+xi, y+yi
                # check condition 
                if 0<=x< len(grid) and 0<= y < len(grid[0]) and grid[x][y] == '.':
                    if x== goalX and y == goalY:
                        return c
                    elif (x,y) not in visit:
                        visit.add((x,y))
                        q.append([x,y,c])
                else:
                    break
    return -1
                    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
