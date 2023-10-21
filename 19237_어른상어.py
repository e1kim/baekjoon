import copy


def outside(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return 1
    return 0

def next_dir(info, shark, s1, s2):
    #shark : shark number
    # s1, s2: shark rocation
    #info[s1][s2][1] : 현재 상어 방향 
    first_dir = first[shark - 1][info[s1][s2][1] - 1]
    for d in first_dir:
        nx = s1 + directions[d-1][0]
        ny = s2 + directions[d-1][1]
        if outside(nx, ny):
            continue
        if info[nx][ny] == 0:
            #아무 냄새가 없다면
            return nx, ny, d
    for d in first_dir:
        nx = s1 + directions[d-1][0]
        ny = s2 + directions[d-1][1]
        if outside(nx, ny):
            continue
        if info[nx][ny][0] == shark:
            #자신의 냄새와 동일하다면 
            return nx, ny, d


    return 0

def smell(info):
    for si in range(n):
        for sj in range(n):
            if info[si][sj] == 0:
                continue
            info[si][sj] = (info[si][sj][0], info[si][sj][1], info[si][sj][2] -1)
            if info[si][sj][2] == 0:
                info[si][sj] = 0
    
def func(info):
    global shark_rocation, count
    while True:
        if len(shark_rocation) == 1:
            break
        if count >= 1000:
            count = -1
            break
        new_shark_rocation = []
        for shark in shark_rocation:
            #print("shark:", shark)
            s1, s2 = shark[1]
            result = next_dir(info, shark[0], s1, s2)
            if not result:
                continue
            nx, ny, d = result
            #상어 이동
            shark_data[s1][s2] = 0 #현재 상어위치는 0으로 두기.
            if shark_data[nx][ny]:
                #상어는 죽는다.
                continue
            else:
                #이동한다.
                shark_data[nx][ny] = shark[0]
                new_shark_rocation.append((shark[0], (nx,ny)))
                shark_dir[shark[0]-1] = d
            
        for shark in new_shark_rocation:
            number = shark[0]
            s1, s2 = shark[1]
            info[s1][s2] = (number, shark_dir[number-1], k+1)
        shark_rocation = copy.deepcopy(new_shark_rocation)
        smell(info)
        count += 1
        

        
            
#main function
    
        
n, m, k = map(int, input().split())

shark_data = []
shark_dir = []
directions = [ (-1,0), (1,0), (0,-1), (0,1) ]
first = [ [0] * 4 for _ in range(m) ]
shark_rocation = []
count = 0
info = [ [0] * n for _ in range(n) ]

#상어 정보 입력 받기 
for i in range(n):
    shark_data.append(list(map(int,input().split())))
    for j in range(n):
        if shark_data[i][j] :
            shark_rocation.append((shark_data[i][j], (i,j)))
shark_rocation.sort()


#상어 방향 입력 받기 
shark_dir = list(map(int,input().split()))
#상어 방향 우선순위 입력받기

for i in range(m):
    for j in range(4):
        first[i][j] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if shark_data[i][j] == 0:
            continue
        info[i][j] = (shark_data[i][j], shark_dir[shark_data[i][j]-1], k)

func(info)
print(count)
