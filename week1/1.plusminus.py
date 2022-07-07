import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Loop through the array, count the number of positive, negative, zero


def plusMinus(arr: list[int]) -> None:
    num_zero, num_pos, num_neg = 0, 0, 0
    for number in arr:
        if number > 0:
            num_pos += 1
        elif number == 0:
            num_zero += 1
        else:
            num_neg += 1
    print('{:6f}\n{:6f}\n{:6f}'.format(
        num_pos/len(arr), num_neg/len(arr), num_zero/len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
