from collections import deque


n, m = map(int, input().split())

virus = []
data = []
directions = [(-1,0), (1,0), (0,-1), (0,1)]

for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] == 2:
            virus.append((i,j))


comb = deque()
vi = [ _ for _ in range(len(virus))]
sel = []


def bfs(activation):
    q = deque()
    Max = 0
    visited = [ [0] * n for _ in range(n)]
    for act in range(len(activation)):
        if activation[act]:
            x, y = virus[act][0], virus[act][1]
            q.append((x,y))
            
            visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy= directions[i]
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >=n or visited[nx][ny] or data[nx][ny] == 1:
                continue
            q.append((nx,ny))
            visited[nx][ny] = visited[x][y] + 1


    for i in range(n):
        for j in range(n):
            if Max < visited[i][j] and data[i][j] == 0:
                Max = visited[i][j]
            if visited[i][j] == 0 and data[i][j] == 0:
                return 1e9


    return Max
        
        
        
        
    
def combinations(comb, depth):
    if len(comb) == m:
        new = []
        for c in comb:
            new.append(c)
        sel.append(new)
        return
    elif depth == len(vi):
        return

    comb.append(vi[depth])
    combinations(comb, depth + 1)
    comb.pop()
    combinations(comb, depth + 1)

combinations(comb, 0)

MIN = 1e9


for com in sel:
    activation = [False for _ in range(len(vi))]
    for c in com:
        activation[c] = True

    mm = bfs(activation)
    
    if MIN > mm :
        MIN = mm




if (MIN == 1e9):
    print(-1)
elif MIN == 0:
    print(0)
else:
    print(MIN - 1)

