#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

# loop while is_swap true
# check the whole array like a buble sort
# if item > item in the right, swap it,
# but keep the swapping number for each person in hashmap
# if loop the array and no swap happen, is_swap = false and exit loop
# print the number of swap


def minimumBribes(q: list[int]) -> None:
    hash_map = {}
    swap_count = 0
    is_swap = True
    while is_swap:
        is_swap = False
        for i in range(len(q) - 1):
            if q[i] > q[i+1]:
                # count
                swap_count += 1
                if q[i] in hash_map:
                    hash_map[q[i]] += 1
                    if hash_map[q[i]] > 2:
                        print("Too chaotic")
                        return
                else:
                    hash_map[q[i]] = 1
                # swap
                q[i], q[i+1] = q[i+1], q[i]
                is_swap = True
    print(swap_count)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
