#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    #  Create dist graph
    dist_graph = [[math.inf for i in range(n+1)] for j in range(n+1)]
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        # update weights
        dist_graph[u][v] = w
        
    # update diagonal of distance matrix to 0 
    for i in range(1, n+1):
        dist_graph[i][i] = 0
    
    # floyd warshall algorithm
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                # update minimum distance
                dist_graph[i][j] = min(dist_graph[i][j], dist_graph[i][k] + dist_graph[k][j])
                
    q = int(input())
    for _ in range(q):
        x,y = map(int, input().split())
        if dist_graph[x][y] == math.inf:
            print(-1)
        else:
            print(dist_graph[x][y])

    # timeout :(