import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

# brute force, create all permutation, O((n!)^2)

# still brute force, write_idx pointer at A, loop at B, if found >=, swap it into write_idx
# sort B so that we can find number that are closest to K and >= K
# O(n^2)

# sort A, sort B(reverse=true), 
# [A0, A1, A2] Ai < Ai+1 
# [B0, B1, B2] B0 > Bi+1
# Let's say we pair A0 and B0, if its still A0 +B0 < K,
# then there's nothing we can do, because B0 is the biggest, if we say 
# we choose A1, then A0 will never find a pair (A0 smallest, 
# and moving B to right will only diminishing the size)

def twoArrays(k : int, A : list[int], B :list[int]) -> bool:
    A.sort()
    B.sort()
    B.reverse()
    print(A)
    print(B)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"

if __name__ == '__main__':
    # print(twoArrays(10, [2,1,3], [7,8,9]))
    # exit()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
