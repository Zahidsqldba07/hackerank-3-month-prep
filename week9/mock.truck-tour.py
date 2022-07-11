#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

# check if valid 
# count the total diff = gas - cost 
# if < 0 : return -1

# start with starting, tank = 0 ,0
# loop for i until len() - 1 
# for start -> len(-1), tank += gas - distance
# if tank < 0 : starting = starting+ 1 
# 

def truckTour(petrolpumps: list[list[int]]) -> int:
    # check valid
    sumdiff = 0
    for petrol in petrolpumps:
        sumdiff += petrol[0] - petrol[1]
    if sumdiff < 0 :
        return -1
    starting, tank = 0, 0
    for i in range(len(petrolpumps)):
        tank += petrolpumps[i][0] - petrolpumps[i][1]
        if tank < 0 :
            starting = i +1 
            tank = 0
    return starting
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
