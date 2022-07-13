#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#



def journeyToMoon(n : int, astronaut :list[list[int]]) -> int:
    # create adjacency list 
    graph = [[] for i in range(n)]
    
    for x,y in astronaut:
        graph[x].append(y)
        graph[y].append(x)
        
    visited = [False] * n
    # calculate total pairs
    pairs = n * (n-1) // 2 
    
    # dfs function to find no. person in one country
    def dfs(u : int, graph : list[list[int]], visited : list[bool]):
        visited[u] = True
        vertices = 1 
        for v in graph[u]:
            if visited[v] == False:
                vertices += dfs(v, graph, visited)
        return vertices
    
    # main logic
    
    for v in range(n):
        if visited[v] == False:
            n_persons = dfs(v, graph, visited)
            pairs -= n_persons * (n_persons - 1) //2
    return pairs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
