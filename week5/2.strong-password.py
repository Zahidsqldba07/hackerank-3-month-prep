import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

# check upper_remaining, 1 if not upper, else 0
# check lower_remaining, 1 if not have lower, else 0
# check special_remainig, 1 if not have spec, else 0
# check length_remaining
# return max(length_remaining, upper+lower+special)
LIST_SPECIAL = ['!', 'A', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']


def minimumNumber(n: int, password: str) -> int:
    length_remaining = 6 - len(password) if len(password) < 6 else 0
    count = 4
    is_upper, is_lower, is_special, is_digit = False, False, False, False
    for char in password:
        if char.isdigit():
            count = count - 1 if not is_digit else count
            is_digit = True
        elif char.isupper():
            count = count - 1 if not is_upper else count
            is_upper = True
        elif char.islower():
            count = count - 1 if not is_lower else count
            is_lower = True
        elif char in LIST_SPECIAL:
            count = count - 1 if not is_special else count
            is_special = True
    return max(count, length_remaining)


if __name__ == '__main__':
    # print(minimumNumber(5, '2bbbb'))
    # exit()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
