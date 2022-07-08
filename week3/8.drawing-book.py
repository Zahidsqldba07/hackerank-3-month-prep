import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

# odd
# 1 -> 2 3 -> 4 5 -> 6 7 -> 8 9 -> 10 11
# to page 8, then 11-8 =3
# to page 9, then 11-9 = 2
# to page 4, need (11-4) = 7
# to page 5, need (11-5) = 6 (n-p)//2

# even
# 1 -> 2 3 -> 4 5 -> 6 7 -> 8 9 -> 10
# 10 to 5 -> 5//2 = 2 (X)
# 10 to 5 -> (10 -5 +1) // 2 = 3 (V)
# 10 to 3 -> (8//2) = 4
# 10 to 2 -> (9//2) = 4


# if odd, placement of last page will be on right, if even, left
# if went to front, will need p//2 turn
# if went from back will need  (n-p)//2 if n odd, (n-p+1)//2 if n even
# if even, p >= n-1 will result in 0

def pageCount(n: int, p: int) -> int:
    if n % 2 == 0:
        from_last = (n-p+1)//2
    else:
        if (p >= n-1):
            from_last = 0
        else:
            from_last = (n-p)//2
    if (p == 1):
        from_front = 0
    else:
        from_front = p//2
    return min(from_last, from_front)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
