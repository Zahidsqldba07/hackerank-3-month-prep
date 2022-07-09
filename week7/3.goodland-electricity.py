import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

# create array of size len() of False
# start from left -> right
# if coverage[i] is True: continue
# else:
# greedy : check from i (i+ k -1) to i to check if arr[i] == 1:
# if not found, return -1
# if found, cover all power plant in i - k < i < i + k range in coverage to True


def pylons(k: int, arr: list[int]) -> None:
    coverage = [False] * len(arr)
    count = 0
    for i in range(len(arr)):
        # print("idx", i, "start")
        if coverage[i]:
            continue
        # else
        idx_cover = -1
        start = i + k - 1 if i + k - 1 <= len(arr) - 1 else len(arr) - 1
        for j in range(start, i-1, -1):
            # print('finding at idx', j)
            if arr[j] == 1:
                idx_cover = j
                break
        if idx_cover == -1:
            return -1
        # update coverage
        # print("put plant at idx", idx_cover)
        left_bound = idx_cover-k+1 if idx_cover-k+1 >= 0 else 0
        right_bound = idx_cover+k-1 if idx_cover + \
            k-1 <= len(arr) - 1 else len(arr) - 1
        for k in range(left_bound, right_bound+1):
            # print("coverage", k)
            coverage[k] = True
        # count++
        count += 1
        # print(coverage)

    # print(coverage)
    return count


if __name__ == '__main__':
    # print(pylons(2, [0, 1, 1, 1, 1, 0]))
    # exit()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
