import math
import os
import random
import re
import sys


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# if len odd return -1
# split into 2
# loop first half, use hashmap to count occurence
# loop second half, use hashmap to subtract the occurence
# count number of remaining occurence that the second half doesnt covered
# return count
# O(n) time O(n) space

def anagram(s: str) -> int:
    hashmap = {}
    count = 0
    if len(s) % 2 != 0:
        return -1
    for char in s[:len(s)//2]:
        hashmap[char] = hashmap.get(char, 0) + 1
    for char in s[len(s)//2:]:
        if char in hashmap:
            hashmap[char] -= 1 
            if hashmap[char] <= 0:
                hashmap.pop(char)
    for remaining in hashmap.values():
        count += remaining
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
