import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def append_zero_if_single(s:str)->str:
    if len(s)==1:
        return '0'+s
    else:
        return s

def timeConversion(s):
    # Write your code here
    # if AM, then return val%12 
    # if PM 12 + val%12 
    code = s[8:10]
    hour= int(s[0:2])
    if code == 'PM':
        return append_zero_if_single(str(12+(hour%12)))+s[2:8]
    else:
        return append_zero_if_single(str(hour%12))+s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
