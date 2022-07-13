#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

# use solution from discussion 

def contacts(queries : list[list[str]]) -> list[int]:
    # Write your code here
    # prefix tree
    res=[]
    dic={}
    for i, [cmd,name] in enumerate(queries):
        if cmd=="add":
            curr=dic
            for ltt in name:
                if ltt in curr: # already  add this
                    curr=curr[ltt]
                    curr['#'] += 1
                else:
                    curr[ltt]={}
                    curr=curr[ltt]
                    curr['#'] = 1
        elif cmd=="find":
            partial=name
            curr=dic
            find=True
            for ltt in partial:
                if ltt in curr:
                    curr=curr[ltt]
                else:
                    find=False
                    break
            if find:
                res.append(curr['#'])
            else:
                res.append(0)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
