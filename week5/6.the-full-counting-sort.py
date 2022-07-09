import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

# Strategy
# Create arr_count with size len(arr)
# loop item in arr :
# idx < len(arr)//2 + 1 -> insert into arr_count but change the char into -
# else -> insert like usual

# loop row in arr_count, loop col, print left to right
# time O(n) , space O(n)


def countSort(arr: list[list[str]]) -> None:
    arr_count = []
    for i in range(len(arr)):
        arr_count.append([])
    for i in range(len(arr)):
        order, string = arr[i]
        if i < len(arr)//2:
            arr_count[int(order)].append('-')
        else:
            arr_count[int(order)].append(string)

    for row in range(len(arr_count)):
        for i in range(len(arr_count[row])):
            print(arr_count[row][i], end=(' ' if row == len(
                arr_count)-1 and i == len(arr_count[row]) else ' '))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
