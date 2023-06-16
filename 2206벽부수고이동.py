import sys
from itertools import *
from collections import *


read = sys.stdin.readline


n, m = map(int, read().rstrip().split())
arr = []
dr = [1,-1,0,0]
dc = [0,0,-1,1]

for i in range(n):
    arr.append( [int(x) for x in input()])
    


blank = []
wall = []


visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs(r,c,z):

    visited[r][c][z] = 1
    Q = deque()

    Q.append((r,c,z))
    while Q:
        r , c , z = Q.popleft()
        if r == n-1 and c == m-1:
            
            return visited[r][c][z]
        
        for index in range(4):
            nr = r + dr[index]
            nc = c + dc[index]
            

            if nr < 0 or nr >= n or nc < 0 or nc >= m :
                continue
            if visited[nr][nc][z] == 1:
                continue
            
            if arr[nr][nc] == 1 and z == 0 :
                Q.append((nr,nc,1))
                visited[nr][nc][1] = visited[r][c][z] + 1
                
            elif visited[nr][nc][z] == 0 and arr[nr][nc] == 0:
                Q.append((nr,nc,z))
                visited[nr][nc][z] = visited[r][c][z] + 1

    
    
    
    return 0
    
            
            
    
    
result = bfs(0,0,0)

        
if result == 0:
    print(-1)
else:
    print(result)
        
    
    
