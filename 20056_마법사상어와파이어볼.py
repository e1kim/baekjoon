import copy
from collections import deque


n, m, k = map(int, input().split())
direction = [ (-1,0), (-1,1), (0,1), (1,1), (1,0), (1, -1), (0,-1), (-1,-1) ]

input_fireballs = []
for i in range(m):
    a = list(map(int, input().split()))
    a[0] -= 1
    a[1] -= 1
    input_fireballs.append(a)


info = [[ []  for _ in range(n) ] for please in range(n)]
    

def outside(x, y):
    while x < 0:
        x += n
    while y < 0:
        y += n
    while x >= n:
        x -= n
    while y >= n:
        y-= n

    return x, y

def move(r, c, m, s, d):

    nr = r + direction[d][0] * s
    nc = c + direction[d][1] * s
    nr, nc = outside(nr,nc)

    
    return nr, nc
    

def twomore(info, a, b):

    Sum_m = 0
    Sum_s = 0
    cnt_odd = 0
    cnt_even = 0
    num = len(info[a][b])
    while info[a][b]:
        m, s, d = info[a][b].pop(0)
        Sum_m += m
        Sum_s += s
        if d % 2 == 0:
            cnt_even += 1
        else:
            cnt_odd += 1
    
    Sum_m //= 5
    Sum_s //= num
    all_d = (cnt_even == num or cnt_odd == num)

    return Sum_m, Sum_s, all_d

#main function

while True:

    if k == 0:
        break

    #파이어볼 이동
    while input_fireballs:
        br, bc, bm, bs, bd = input_fireballs.pop(0)
        nr, nc = move(br, bc, bm, bs, bd)
        info[nr][nc].append((bm, bs, bd))            

    
    for i in range(n):
        for j in range(n):
            if len(info[i][j]) >= 2:       
                #중복된 파이어볼을 없앤 리스트를 만든다. 
                m, s, d = twomore(info, i, j)

                #질량이 있는 경우 4개로 나뉨
                if m:
                    if d == 1:
                        for p in range(0,7,2):
                            input_fireballs.append((i,j,m,s,p))
                    else:
                        for p in range(1,8,2):
                            input_fireballs.append((i,j,m,s,p))

            if len(info[i][j]) == 1:
                lm, ls, ld = info[i][j].pop(0)
                input_fireballs.append((i, j, lm, ls, ld))
    k -= 1

#SUM M
answer = 0


for ball in input_fireballs:
    answer += ball[2]


print(answer)

    
    
