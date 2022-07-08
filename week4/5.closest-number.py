import math
import os
import random
import re
import sys
from this import d

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# sort number
# loop 1<=i<=len()-1
# diff = arr[i] - arr[i-1]
# hashmap[diff] = hashmap[diff].append((arr[i-1], arr[i]))
# find min diff
# print that array


def closestNumbers(arr: list[int]) -> list[int]:
    hashmap = {}
    arr.sort()
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i+1])
        if diff in hashmap:
            hashmap[diff] += [arr[i], arr[i+1]]
        else:
            hashmap[diff] = [arr[i], arr[i+1]]
    min_diff = min(hashmap.keys())
    return hashmap[min_diff]


if __name__ == '__main__':
    # print(closestNumbers([5, 2, 3, 4, 1]))
    # exit()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
