import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

# ex length 5 (0 - 4) with m=2 means max loop is 3 (length-m)
# For for 0 - length-m
# if sum equals d, count++

# operation: looping (n-m +1) time, with m loop sum = (n-m+1)(m)
# Time  O(nm) - O(m^2) - O(m), since n > m , nm > m^2 > m, time O(nm)


def birthday(s: list[int], d: int, m: int, count=0):
    for i in range(0, len(s)-m +1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count


if __name__ == '__main__':
    # print(birthday([1,2,1,3,2], 3, 2))
    # exit()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
