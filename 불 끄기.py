import copy
temp= [list (map(str,input())) for _ in range(10) ]


"""
O########O
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
O########O

정답: 100

"""
light = []
for i in range(10):
    light.append([])
    for j in range(10):
        if temp[i][j] == 'O':
            light[i].append(1)
            #불이 켜져있다면 1
        else:
            light[i].append(0)


minnimum = 1e7

for case in range(1<<10):
    count = 0
    mask = 1
    tmp = copy.deepcopy(light)
    
    #tmp는 light의 복사본
    #맨 첫번째 줄을 1024가지로 불을 끌지 말지 정한다.
    
    for i in range(10):
        turn = (( case & (1 << i) ) // (1<<i))
        if turn == 1: count+=1
        #첫번째줄에서 불을끈다면, 주변도 반대로 해야한다.
        tmp[0][i] ^= turn
        tmp[1][i] ^= turn #하
        #하좌우를 스위치 반대로! (맨위니까 상은 필요없음)
        if i-1>=0: #좌
            tmp[0][i-1] ^=turn
        if i+1<10: #우
            tmp[0][i+1] ^=turn
        
        
           
    
    
    for i in range(1,10):
        for j in range(10):
            if tmp[i-1][j] ==1:
                tmp[i-1][j] ^=1
                tmp[i][j] ^=1
                count += 1
                if j-1 >= 0:
                    tmp[i][j-1] ^=1
                if j+1 < 10:
                    tmp[i][j+1] ^=1
                if i+1 < 10:
                    tmp[i+1][j] ^=1

    all_off = 1
    #다 껐는지 확인하고 다 끄지 않았다면 update X
    for j in range(10):
        if tmp[9][j]:
            all_off = 0
            break

    if all_off :
        if minnimum > count:
            minnimum = count
            
    

if minnimum == 1e7 :
    print(-1)
else:
    print(minnimum)
    
    
    
            
    
