import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# use list of size 5 to track occurent
# loop, count
# track the max_id = 0
# O(n) with O(1)


def migratoryBirds(arr: list[int]) -> int:
    tracker = [0]*5
    for i in range(len(arr)):
        tracker[arr[i]-1] += 1
    max_frequent, max_id = float('-inf'), 0
    for i in range(5):
        if max_frequent < tracker[i]:
            max_frequent = tracker[i]
            max_id = i+1
    return max_id


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
