import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

# recursive(before : int , idx: int)
# base : idx == len, return True
# X = False
# loop offset from idx+1 until len()+1:
# if int(s[idx:offset]) - int(before) ==1:
# call X = X OR recursive(s[idx:offset], offset)
# return X


def separateNumbers(s: str) -> None:
    def recursive(arr: int, before: int, idx: int) -> bool:
        if idx == len(s):
            if before == int(s):
                return
            res.append(arr)
            return
        for offset in range(idx+1, len(s) + 1):
            substring = int(s[idx:offset])
            if (substring - before == 1 or before == -1) and (len(str(substring)) == len(s[idx:offset])):
                recursive(arr + [substring], substring, offset)
    res = []
    recursive([],-1, 0)
    if len(res) > 0:
        smallest = float('inf')
        for item in res:
            smallest = min(smallest, item[0]) 
        print('YES'+' '+str(smallest))
    else:
        print('NO')


if __name__ == '__main__':
    # print(separateNumbers('91011'))
    # exit()
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
