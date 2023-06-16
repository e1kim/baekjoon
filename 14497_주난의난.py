import sys
from collections import deque

read = sys.stdin.readline
global visited, arr

'''
1#10111
1101001
001*111
1101111
0011001

1#10111
1100001
000*011
1100111
0011001

1#00001
0000000
000*001
0000011
0000001

'''
def bfs(a,b):
    global visited, arr
    q = deque()
    q.append((a,b))
    visited[a][b] = 1

    dr = [1,-1,0,0]
    dc = [0,0,-1,1]
    cnt = 0
    while 1:
        temp = deque()
        cnt += 1
        
        visited = [ [ 0 for i in range(m)] for j in range(n)]
        while q:
            
            r,c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr < 0 or nc < 0 or nr >= n or nc >=m:
                    continue
                if arr[nr][nc] == '#':
                    pass
                elif arr[nr][nc] == '1':
                    arr[nr][nc] = '0'
                    temp.append((nr,nc))
                else:
                    q.append((nr,nc))
                    visited[nr][nc] = 1
                    
        if len(q) == 0:
            q=(temp)
                
    return cnt
        
        




n,m = map(int,input().split())

print(n,m)

x1,y1,x2,y2 = map(int,read().rstrip().split())

print(x1,y1,x2,y2)

arr = [ [input()] for _ in range(n)]

print(arr)
print(arr[0][0])
arr[0][0] = '3'
visited = [ [ 0 for i in range(m)] for j in range(n)]
print(visited)


print(bfs(x1-1,y1-1))


