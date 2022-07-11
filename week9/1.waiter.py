#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(numbers: list[int], q: int) -> list[int]:
    stackA = list(numbers)
    res = []
    is_prime = [1] * 10000
    primes = []
    for i in range(2, 10000):
        if is_prime[i] == 1:
            primes.append(i)
            for j in range(i, 10000, i):
                is_prime[j] = 0

    for query in range(q):
        prime = primes[query]
        new_stackA, new_stackB = [], []
        for i in range(len(stackA)):
            number = stackA.pop()
            if number % prime == 0:
                new_stackB.append(number)
            else:
                new_stackA.append(number)
        stackA = new_stackA
        res += new_stackB[::-1]
    return res + stackA[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
