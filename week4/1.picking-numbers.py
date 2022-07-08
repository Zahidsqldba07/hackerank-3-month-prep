import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(A: list[int]) -> int:
    hash_map = {}
    for item in A:
        hash_map[item] = hash_map.get(item, 0)+1
    vals = sorted(hash_map.keys())

    last_val = vals[0]
    max_length = hash_map[vals[0]]

    for i in range(1,len(vals)):
        # compare for 1 element only 
        max_length = max(max_length , hash_map[vals[i]])
        # compare for this element vs last element if the diff is <=1  
        if abs(last_val - vals[i]) <= 1:
            max_length = max(max_length , hash_map[vals[i]] + hash_map[last_val])
        # make last element = this element
        last_val = vals[i]
    return max_length

if __name__ == '__main__':
    # print(pickingNumbers([1,1,2,2,4,4,5,5,5]))
    # exit()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
