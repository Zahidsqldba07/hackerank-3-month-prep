import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

# for each item in player (start from the end)
# set rank = 1
# while j ==


def climbingLeaderboard(ranked: list[int], player: list[int]) -> list[int]:
    ranked = list(set(ranked))
    ranked.sort()
    n = len(ranked)
    i = 0
    res = []

    for score in player:
        while i < n and ranked[i] <= score:
            i += 1
        res.append(n-i + 1)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
