from collections import deque


n = int(input())


data = []
baby = ()
directions = [ (-1,0), (1,0), (0,-1), (0,1) ]


for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] == 9:
            baby = (i,j)
            
def bfs(s1, s2, size):
    q = deque()
    q.append((s1,s2))
    visited = [ [0] * n for u in range(n) ]
    visited[s1][s2] = 1
    fish = []
    while q:
        x, y = q.popleft()

        for d in directions:
            dx, dy = d[0], d[1]

            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                continue
            if size < data[nx][ny]:
                continue
            if data[nx][ny] == 0 or data[nx][ny] == size:
                q.append((nx, ny))
            else:
                #물고기 save
                fish.append((visited[x][y] + 1, nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    if not fish:
        return 0
    
    fish.sort()
    return fish[0]

#main function


shark_size = 2
time = 0
while True:
    for eat in range(shark_size):
        result = bfs(baby[0], baby[1], shark_size)
        if not result:
            break
        
        time += result[0] - 1
        data[baby[0]][baby[1]] = 0
        baby = (result[1], result[2])
        data[baby[0]][baby[1]] = 9

        
    
    if not result:
        break
    shark_size += 1

    
    
print(time)
        

            
