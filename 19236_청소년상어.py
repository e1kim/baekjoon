from collections import deque
import copy


def outside(x,y):
    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return 1

    return 0

def fish_move(info, s1, s2):
    for n in range(1,17):
        x, y = (-1,-1)
        for f in range(4):
            for g in range(4):
                if n == info[f][g][0]:
                    x, y = f, g
                    break

        if x == -1 and y == -1:
            continue
        d = info[x][y][1]
        
        for i in range(8):
            nd = d + i
            if nd >= 8:
                nd -= 8
            nx = x + directions[nd][0]
            ny = y + directions[nd][1]

            #공간의 경계를 넘거나 상어가 있는 칸이면 pass
            if outside(nx, ny) or (nx == s1 and ny == s2):
                continue
            #빈칸이거나 다른 물고기가 있는 칸 go
            tmp = info[nx][ny]
            info[nx][ny] = (info[x][y][0], nd)
            info[x][y] = tmp
            break
    return info

            

def shark_move(info, s1, s2):
    feed = [] #먹이들을 저장한다.
    dx = directions[info[s1][s2][1]][0]
    dy = directions[info[s1][s2][1]][1]
    for i in range(4):
        new_s1 = s1 + dx
        new_s2 = s2 + dy
        s1, s2 = new_s1, new_s2
        if outside(new_s1, new_s2):
            continue
        if info[new_s1][new_s2][0] == 0:
            continue
        feed.append((new_s1,new_s2))
        

    return feed

def dfs(info, s1, s2, score):
    global answer
    score += info[s1][s2][0]
    answer = max(answer,score)

    info[s1][s2]= (0, info[s1][s2][1]) #기존 상어가 있던 곳은빈칸으로
    info = fish_move(info, s1, s2)
    feed = shark_move(info, s1, s2)
    for f in feed:
        fx, fy = f
        dfs(copy.deepcopy(info), fx, fy, score)
        
#main function
directions = [ (-1,0), (-1,-1), (0,-1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
data = []
info = [ [0] * 4 for _ in range(4) ]

for i in range(4):
    data.append(list(map(int, input().split())))
    for j in range(0, 8, 2):
        info[i][j//2] = (data[i][j], data[i][j+1]-1)



answer = 0
dfs(info, 0, 0, 0)
print(answer)
    
      
            
    
