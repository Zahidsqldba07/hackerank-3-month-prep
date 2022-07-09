import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# var left_sum, right_sum = 0, sum(arr) -- O(n)
# var center = 0
# loop while left_sum != right_sum and center < len(arr):
# check left_sum == right_sum, if yes return 'YES'
# else : center++


def balancedSums(arr: list[int]) -> str:
    if len(arr) <= 1 :
        return 'YES'
    left_sum, right_sum, center = 0, sum(arr) - arr[0], 0
    
    while center < len(arr) - 1:
        if left_sum == right_sum:
            return 'YES'
        left_sum += arr[center]
        center += 1
        right_sum -= arr[center]
    return 'NO'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
