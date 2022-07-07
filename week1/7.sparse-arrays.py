#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

# hashmap time: O(m+n) space O(n)
# store all queries in hashmap with counter 0 
# loop through strings, count if match 
# return array containing count

def matchingStrings(strings, queries):
    hash_map = {}
    for query in queries:
        hash_map[query] = 0
    for string in strings:
        if string in hash_map:
            hash_map[string] = hash_map.get(string,0) + 1 
    return [hash_map[x] for x in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
