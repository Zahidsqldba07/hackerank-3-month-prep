import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

# only proper if a+b > c, a+c > b, b+c> a
# Sort first

# time O(nlogn)

def is_proper_triangle(a : int, b: int, c : int):
    return (a+b>c) and (a+c>b) and(b+c)>a


def maximumPerimeterTriangle(sticks: list[int]):
    sticks.sort()
    max_stick = [-1]
    for i in range(len(sticks)-3 +1):
        a,b,c = sticks[i:i+3]
        if is_proper_triangle(a,b,c):
            max_stick = [a,b,c] 
    return max_stick

if __name__ == '__main__':
    # print(maximumPerimeterTriangle([3,9,2,15,3]))
    # exit()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
