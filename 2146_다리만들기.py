import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

n = int(read().rstrip())
info = []
for i in range(n):
    info.append( list( map(int, read().rstrip().split())))

visited = [ [ 0 for i in range(n)] for i in range(n)]
check = [ [ 0 for i in range(n)] for i in range(n)]
island = 1
dr = [-1,1,0,0]
dc = [0,0,-1,1]

global result
result = 1e9

def dfs(r,c):

    visited[r][c] = 1
    check[r][c] = island

    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]

        if nr < 0 or nr >= n or nc < 0 or nc >= n or visited[nr][nc] == 1 or info[nr][nc] != 1:
            continue
        dfs(nr,nc)
            
    
def bfs(color):

    qu = deque()
    
    
    for i in range(n):
        for j in range(n):
            if check[i][j] == color:
                qu.append((i,j))
                visited[i][j] = 0
                
                
    
    
    while qu:
        r, c = qu.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >=n or nc < 0 or nc >= n:
                continue
            if info[nr][nc] > 0 and check[nr][nc] != color:
                #다른 땅을 만나면
                
                return visited[r][c]
            elif info[nr][nc] == 0 and visited[nr][nc] == -1 :
                qu.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1  


        
    
    
#dfs 하기
for i in range(n):
    for j in range(n):
        if info[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j)
            island += 1

visited = [[-1 for i in range(n)] for i in range(n)]

        
#bfs 하기
for i in range(island-1):
    visited = [[-1 for i in range(n)] for i in range(n)]
    temp = bfs(i+1)
    
    result = min(result,temp)
    

print(result)


    





    

