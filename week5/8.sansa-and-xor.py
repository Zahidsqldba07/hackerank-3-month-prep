#!/bin/python3

from functools import reduce
import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# 1 2 3 4
# 1, 2, 3, 4
# (1,2) , (2,3), (3,4)
# (1,2,3), (2,3,4)
# (1,2,3,4)
# 1 : 4, 2: 6, 3: 4, 4:4
#
# [1,2]
# 1, 2 , 1,2 = 0
#
# [1,2,3,4,5]
# 1 2 3 4 5
# (1,2) (2,3) (3,4) (4,5)
# (1,2,3) (2,3,4) (3,4,5)
# (1,2,3,4) (2,3,4,5)
# (1,2,3,4,5)
# 1: 5, 2: 8, 3:9 , 4: 8, 5: 5

# len() == even : return 0
# len() == odd, or the odd indices only
# loop for range(0,len(),2)


def sansaXor(arr: list[int]) -> int:
    if len(arr) % 2 == 0:
        return 0
    else:
        sum_xor = 0
        for i in range(0, len(arr), 2):
            sum_xor ^= arr[i]
        return sum_xor


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
