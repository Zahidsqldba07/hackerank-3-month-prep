#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    most_point, least_point = 0, 0
    min_val, max_val = scores[0], scores[0]
    for i in range(len(scores)):
        if scores[i]>max_val: 
            max_val=scores[i]
            most_point += 1 
        if scores[i]<min_val: 
            min_val=scores[i]
            least_point +=1
    return [most_point,least_point]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
