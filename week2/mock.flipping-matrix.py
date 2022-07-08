import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

# for each element in 2x2 matrix, check the mirror (all the possible position)
# count all the maximum potential from every element in that upper left quadrant 

def flippingMatrix(matrix: list[list[int]]) -> int:
    n = len(matrix) -1
    count = 0
    for i in range(len(matrix)//2):
        for j in range(len(matrix)//2):
            count += max(matrix[i][j], matrix[n-i][ j], matrix[i][ n-j], matrix[n-i][n-j])

    return count


if __name__ == '__main__':
    # print(flippingMatrix([[112, 42, 83, 119], [56, 125, 56, 49], [
    #       15, 78, 101, 43], [62, 98, 114, 108]]))
    # exit()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
