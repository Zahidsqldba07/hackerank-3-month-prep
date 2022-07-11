#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# curently, we have bot_energy for height, the new energy is...
# now :  we have the new energy that used for climbing height, the old energy is .. 
# for maximum, we need to have end_energy = 0 

# reverse the arr
# new_energy = 2bot_energy - height
# the energy need for botenergy 
# end_energy = ceil((start_energy + height)/2)

def chiefHopper(arr : list[int]) -> int:
    energy = 0
    for height in arr[::-1]:
        energy = math.ceil((energy + height)/2)
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
