#Baekjoon

from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
data  = []
count = 0 # 총 개수 

for i in range(n):
    data.append(list(map(int, input().split())))

def out_of_range(x, y):
    return x < 0 or y < 0 or x >=n or y >= m

def bfs(r, c, dire):
    global count
    q = deque()
    q.append((r,c,dire))

    while q:
        x, y, d = q.popleft()
        #print(x,y,d)
        flag = 0 #주변 청소할 방을 찾으면 1
        if data[x][y] == 0: # 방을 청소해야한다면 청소하기 
            data[x][y] = 2
            count += 1
        for i in range(4):# 주변 청소할 방을 찾기 
            if d == 0:
                d = 3
            else:
                d -= 1
            dx, dy = directions[d]
            rx = x + dx
            ry = y + dy
            if data[rx][ry] != 0 or out_of_range(rx, ry):
                continue
            elif data[rx][ry] == 0:
                flag = 1
                q.append((rx,ry,d))
                break
                
        if flag == 1:
            continue
        dx, dy = directions[d]# 후진하기 
        dx = 0 - dx
        dy = 0 - dy
        if data[x + dx][y + dy] == 1:
            break
        else:
            q.append((x + dx, y + dy, d))


bfs(r, c, d)
print(count)

        
    
