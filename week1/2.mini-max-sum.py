import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_val,max_val,sum_val = float("inf"),-float("inf"),0
    for i in arr:
        if i>max_val: max_val = i 
        if i<min_val: min_val = i
        sum_val+=i
    print(f'{sum_val-max_val} {sum_val-min_val}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
