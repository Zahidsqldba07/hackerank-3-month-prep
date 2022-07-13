#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#


def prims(n : int, edges : list[list[int]], start :int) -> int:
    def findMinVertex(weights : list[int], visited : list[int])-> int :
        min_weight = sys.maxsize
        for i in range(1, len(weights)):
            if weights[i] < min_weight and not visited[i]:
                min_weight = weights[i]
                min_idx = i 
        return min_idx
    # convert to graph
    graph = [[-1 for i in range(n+1)] for j in range(n+1)]
    
    for a,b,w in edges:
        graph[a][b]  = w
        graph[b][a] = w
    # set weights and visited for nodes 1 - n
    weights = [sys.maxsize] * (n+1)
    visited = [False] * (n+1)
    weights[start] = 0
    
    # loop n times,
    # for each loop, find the min_idx in weights that is not 
    # visited
    # then loop for n times, find graph[u][X] where x 
    # have the minimum weight 
    for i in range(1, n+1):
        min_v = findMinVertex(weights, visited)
        visited[min_v] = True
        for x in range(1, n+1):
            if graph[min_v][x] >= 0 and not visited[x] and weights[x] > graph[min_v][x]:
                weights[x] = graph[min_v][x]
    return sum(weights[1:])
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
