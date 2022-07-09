import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

# n = 0, does notghing
# n = 1, does nothing
# n = 2, place bomb in non-bomb
# n = 3, remove all bomb adjacent to bomb in 0
# n = 4, does nothing
# n = 5, place bomb in non -bomb
# n = 6  remove all bomb adjacent to bomb in 4

# n = n%5 because its pattern
# n <=1 , return the same array
# n ==2 or n == 5, return array with all bomb
# n ==3 or n == 4,
# place bomb except:
# the place of previous bomb
# the place of place adjacent to previous bomb

# loop n times
# loop for row, loop for col
# if found bombs


def bomberMan(n: int, grid: list[str]) -> list[str]:
    def check_cell(grid: list[str], i: int, j: int) -> bool:
        max_row, max_col = len(grid), len(grid[0])
        if ((grid[i][j] == 'O') or
            (0 <= i+1 < max_row and grid[i+1][j] == 'O') or
            (0 <= i-1 < max_row and grid[i-1][j] == 'O') or
            (0 <= j-1 < max_col and grid[i][j-1] == 'O') or
                (0 <= j+1 < max_col and grid[i][j+1] == 'O')):
            return True
        return False

    def fill_grid(grid, row, col):
        res = [['.']*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                # check if cell contain 'O' or adjacent contain 'O'
                if check_cell(grid, i, j):
                    res[i][j] = '.'
                else:
                    res[i][j] = 'O'
        return [''.join(x) for x in res]

    row, col = len(grid), len(grid[0])
    if n <= 1:
        return grid
    elif n % 2 == 0:
        return ['O'*col for _ in range(row)]
    if (n-3) % 4 == 0:
        return fill_grid(grid, row, col)
    else:
        return fill_grid(fill_grid(grid, row, col), row, col)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
    print('')
    print('\n'.join(result))

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
