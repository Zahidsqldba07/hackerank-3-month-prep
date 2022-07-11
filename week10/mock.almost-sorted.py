import math
import os
import random
import re
import sys


#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# sort the arr, store in sorted_arr
# if arr == sorted_arr, return yes
# for checking swap :
# use counter to count if element is different in the same location, if count == 2: print swap
# for checking reverse
# loop until there's difference, then
# start= idx
# loop while item is still different
# get the end idx
# if arr[:start] + sorted arr[start: end+1] + arr[min(end+1, len -1) :]
# print yes, then

def almostSorted(arr: list[int]):
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        print('yes')
        return
    # check for swap
    count_diff = 0
    start_swap, end_swap = -1, -1
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            count_diff += 1
            if start_swap != -1:
                end_swap = i
            else:
                start_swap = i
    if count_diff == 2:
        print("yes")
        print("swap", start_swap+1, end_swap+1)
        return
    # check for reverse
    # strike from front end back
    start_reverse, end_reverse = -1, -1
    for i in range(math.ceil(len(arr)/2)):
        if arr[i] != sorted_arr[i]:
            if start_reverse == -1:
                start_reverse = i
        if arr[~i] != sorted_arr[~i]:
            if end_reverse == -1:
                end_reverse = len(arr) - 1 - i
    # print(start_reverse, end_reverse)
    # print(arr[:start_reverse] + sorted(arr[start_reverse : end_reverse +1]) + arr[min(len(arr)-1, end_reverse + 1): ])
    # print(sorted_arr)
    is_reverse = True
    new_arr = arr[:start_reverse] + \
        list(reversed(arr[start_reverse: end_reverse + 1])) + \
        arr[end_reverse + 1:]
    for i in range(len(arr)):
        if new_arr[i] != sorted_arr[i]:
            is_reverse = False
    if is_reverse:
        print('yes')
        # print(new_arr)
        print("reverse", start_reverse+1, end_reverse+1)
        return

    print('no')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
