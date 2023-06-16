#2583_영역구하기

import sys
from collections import deque

read = sys.stdin.readline

def bfs(a,b):

    q= deque()
    
    q.append((a,b))
    graph[a][b]=1
    cnt = 1
    while q :
        dx = [1,-1,0,0]
        dy = [0,0,-1,1]
        y,x = q.popleft()

        
        for u in range(4):
            n_y = dy[u] + y
            n_x = dx[u] + x

            if n_y >= m or n_x >= n or n_y <0 or n_x <0 or graph[n_y][n_x] != 0:
                continue
            
            q.append((n_y,n_x))
            graph[n_y][n_x] = 1
            cnt += 1
            
            
    return cnt
            

            
m,n,k = map(int,read().rstrip().split())



graph = [[0 for i in range(n)] for j in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1
            


result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(bfs(i,j))
print(len(result))
result.sort()
print(*result)
        
