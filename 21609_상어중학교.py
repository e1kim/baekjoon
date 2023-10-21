from collections import deque


def gravity(data):
    for col in range(n):
        stock = deque()

        for row in range(n-1,-1,-1):
            if data[row][col] == -1: 
                while stock:
                    stock.popleft()
            elif data[row][col] == -2: 
                stock.append((row, col))
            elif data[row][col] >= 0 and stock:
                sx, sy = stock.popleft()
                data[sx][sy] = data[row][col]
                data[row][col] = -2
                stock.append((row, col))
    return data
                


                

def rotation(data):
    result = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            result[n - c - 1][r] = data[r][c]

    return result


def bfs(x,y, col):
    q = deque()
    q.append((x,y,col))
    
    visited[x][y] = 1
    block_cnt = 1
    rainbow_cnt = 0
    blocks = [(x,y)]
    rainbows = []

    while q:
        r, c, color = q.popleft()

        for i in range(4):
            dx, dy = directions[i]
            nx = r + dx
            ny = c + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= n or data[nx][ny] == -1 or visited[nx][ny] != 0:
                continue

            if data[nx][ny] == 0 or data[nx][ny] == color:
                visited[nx][ny] = 1
                if data[nx][ny] == 0:
                    rainbows.append((nx,ny))
                    rainbow_cnt += 1
                else:
                    blocks.append((nx,ny))
                q.append((nx,ny,color))
                block_cnt += 1

    for rx, ry in rainbows:
        visited[rx][ry] = 0
            
        
    return (block_cnt, rainbow_cnt, blocks + rainbows)
#main 함수 

n, color = map(int, input().split())

data = []

for i in range(n):
    data.append(list(map(int, input().split())))

score = 0
directions = [(-1,0), (0,1), (1,0), (0,-1)]    


while True:
    blocks = []
    visited = [ [0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if data[i][j] > 0 and visited[i][j] == 0:
                info = bfs(i, j, data[i][j])
                
                if info[0] >= 2:
                    blocks.append(info)
    blocks.sort(reverse=True)
    
    if not blocks:
        break
    for b in blocks[0][2]:
        bx, by = b
        data[bx][by] = -2
    score += blocks[0][0]**2    
    data = gravity(data)
    data = rotation(data)
    data = gravity(data)
  

print(score)
    
                        
                    
            
            
            
