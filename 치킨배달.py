import sys
from itertools import combinations
read = sys.stdin.readline


n,m = map(int,read().rstrip().split())

array =[]
chicken = []
home = []
for i in range(n):
    temp = list(map(int,read().rstrip().split()))
    array.append(temp)
    for j in range(len(temp)):
        if temp[j] == 2:
            chicken.append((i,j))
        elif temp[j] == 1:
            home.append((i,j))


'''
입력:
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

출력:
10

'''
        

def calc(Open, home):

    MIN = 1e9
    total = 0
    for h in home:
        distance = 1e9
        for o in range(len(Open)):
            if Open[o] == True:
                t = abs(chicken[o][0] - h[0]) + abs(chicken[o][1] - h[1])
                distance = min(distance , t)

        
        total += distance


    return total






selection = list(combinations( range(len(chicken)), m)) #선택한 치킨집


Mini = 1e9
for com in selection:
    Open= [ False for i in range(len(chicken)) ]
    for i in com:
        Open[i] = True

    a = calc(Open, home)
    Mini = min(Mini, a)
print(Mini)

    
    



    
