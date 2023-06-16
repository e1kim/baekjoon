#2828_사과담기게임

import sys

read = sys.stdin.readline

n,m = map(int, read().rstrip().split())

j = int(input())

apple= []
for i in range(j):
    a = int(input())
    apple.append(a)

min_apple = 1
max_apple = m


'''
12
45
12
45

'''
cnt = 0

for i in range(j):
    #print(min_apple,max_apple)
    if min_apple <= apple[i] and apple[i] <= max_apple:
        pass
    elif apple[i] < min_apple:
        cnt += min_apple - apple[i]
        max_apple -= (min_apple - apple[i])
        min_apple -= (min_apple - apple[i])
        
        
    elif apple[i] > max_apple:
        cnt += apple[i] - max_apple
        min_apple += (apple[i] - max_apple)
        max_apple += (apple[i] - max_apple)
        
  
print(cnt)
    
        
