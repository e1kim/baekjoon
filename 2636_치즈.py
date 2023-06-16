import sys
from collections import deque

read = sys.stdin.readline



n,m = map(int, read().rstrip().split())
dr = [1,-1,0,0]
dc = [0,0,-1,1]


cheeze = []
for i in range(n):
    cheeze.append(list(map(int,read().rstrip().split())))


visited = [[ 0 for i in range(m) ] for j in range(n) ]


q = deque()

for i in range(1,m):
    q.append((0,i))
    visited[0][i] = 1
    
for i in range(1,n):
    q.append((i,m-1))
    visited[i][m-1] = 1
        
for i in range(1,m):
    q.append((n-1,i-1))
    visited[n-1][i-1] = 1

for i in range(1,n):
    q.append((i-1,0))
    visited[i-1][0] = 1


temp = deque()
cnt = 0

cheeze_num =0
want = []
while temp or q:
    temp = deque()
    #print("남은 치즈의 개수: ",want)
    want.append(cheeze_num)
    cheeze_num=0
    while q:
        r,c = q.popleft()

        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if (nr <0 or nc <0 or nr >= n or nc >= m or visited[nr][nc] ):
                continue

            visited[nr][nc] = 1
            if (cheeze[nr][nc] == 1):
                temp.append((nr,nc))
                cheeze[nr][nc]= 0
                cheeze_num += 1
                #1을 만나면 temp에 저장하고 0으로 바꾼다.
            else:
                q.append((nr,nc))

    if temp:
        q = temp
        cnt += 1
        
        
print(cnt)
print(want[-1])

    
    
            
        









        
    
