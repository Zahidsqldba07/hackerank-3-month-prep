#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

# create function(matrix, x, y) that counts the number of cells covered
# and change the cell into 0
# base case : cannot go horizontal, vertical, and diagonal


# loop over the matrix, if found ==1 , then call the function to remove + count the max
# compare it with max_val
# return max_val


def can_go(matrix: list[list[int]], x: int, y: int):
    row_max = len(matrix)
    col_max = len(matrix[0])
    # check if outside the boundary
    # check if the targeted cell value is 1
    if 0 <= x < row_max and 0 <= y < col_max and matrix[x][y] == 1:
        return True
    return False


def connectedCell(matrix: list[list[int]]) -> int:

    def count_area(matrix: list[list[int]], x: int, y: int):
        # base case : cannot go up down, cannot go left right, cannot go diag up_left up_right down_left down_right
        # print(x,y)
        # return 0
        is_one = matrix[x][y] == 1
        matrix[x][y] = 0

        is_can_move = can_go(matrix, x+1, y) or can_go(matrix, x-1, y) or can_go(matrix, x, y+1) or can_go(matrix, x, y -
                                                                                                           1) or can_go(matrix, x-1, y-1) or can_go(matrix, x-1, y+1) or can_go(matrix, x+1, y-1) or can_go(matrix, x+1, y+1)
        # print(is_can_move)
        if not is_can_move:
            # print("base", x,y, matrix[x][y])
            return 1 if is_one else 0
        # mark the cell to 0
        count = 1
        # check if can go vertical
        if can_go(matrix, x+1, y):
            count += count_area(matrix, x+1, y)
        if can_go(matrix, x-1, y):
            count += count_area(matrix, x-1, y)
        # check if can go horizontal
        if can_go(matrix, x, y+1):
            count += count_area(matrix, x, y+1)
        if can_go(matrix, x, y-1):
            count += count_area(matrix, x, y-1)
        # check if can go diagonal
        if can_go(matrix, x - 1, y - 1):
            count += count_area(matrix, x - 1, y - 1)
        if can_go(matrix, x - 1, y + 1):
            count += count_area(matrix, x - 1, y + 1)
        if can_go(matrix, x + 1, y - 1):
            count += count_area(matrix, x + 1, y - 1)
        if can_go(matrix, x + 1, y + 1):
            count += count_area(matrix, x + 1, y + 1)
        return count

    max_val = float('-inf')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # print("matrix val:", matrix[i][j])
            area = count_area(matrix, i, j) if matrix[i][j] == 1 else 0
            max_val = max(max_val, area)
            # if area > 0:
            #     print('area: ', area)
    return max_val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
