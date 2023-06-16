import sys
from itertools import *
from collections import *

read = sys.stdin.readline

dr=[1,-1,0,0]
dc=[0,0,-1,1]

n,m = map(int, read().rstrip().split())

info = []
blank = []
virus = []
for i in range(n):
    info.append( list (map(int, read().rstrip().split())))


for i in range(n):
    for j in range(m):
        if info[i][j] == 0:
            blank.append((i,j))
        if info[i][j] == 2:
            virus.append((i,j))
            

com = list(combinations(blank,3))

visited = []



def bfs(r,c):
    Q = deque()
    Q.append((r,c))
    visited[r][c] = 1
    count = 0

    while Q:
        r,c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if visited[nr][nc] == 1:
                continue
            if visited[nr][nc] == 0 and info[nr][nc] == 0:
                Q.append((nr,nc))
                visited[nr][nc] = 1
                count += 1
    return count
                
            
result = 0
#sample = [ ( (1,0),(0,1),(3,5) )]
for c in com:
    visited = [ [0 for i in range(m)] for i in range(n) ]
    info[c[0][0]][c[0][1]]=1
    info[c[1][0]][c[1][1]]=1
    info[c[2][0]][c[2][1]]=1
    
    temp = 0
    for v in virus :
        vr,vc=v[0],v[1]
        temp += bfs(vr,vc)
    result = max(result, len(blank)-3-temp)

    info[c[0][0]][c[0][1]]=0
    info[c[1][0]][c[1][1]]=0
    info[c[2][0]][c[2][1]]=0
        
print(result)

'''
for i in range(n):
    for j in range(m):
        print("%2d"%visited[i][j],end=' ')
    print()

'''


