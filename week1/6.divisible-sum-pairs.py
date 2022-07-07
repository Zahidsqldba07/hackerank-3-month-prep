
import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

# brute force O(n^2)
# loop for each number, then nest loop until end of arr to check


# def divisibleSumPairs(n: int, k: int, ar: int) -> int:
#     count = 0
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if (ar[i] + ar[j]) % k == 0:
#                 count += 1
#     return count

# hashmap O(n) time with O(n) space
# for each number, find if the complement that make it divisible


def divisibleSumPairs(n: int, k: int, ar: list[int]) -> int:
    count = 0
    hash_map = {}
    for num in ar:
        if (num%k) in hash_map:
            count += hash_map[num%k]
        complement = k - (num % k) if (num % k != 0) else 0
        hash_map[complement] = hash_map.get(complement, 0) + 1
    return count


if __name__ == '__main__':
    # print(divisibleSumPairs(6, 3, [1,3,2,6,1,2]))
    # print(divisibleSumPairs(2, 2, [8,10]))
    # exit()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


