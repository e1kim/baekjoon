import sys

read = sys.stdin.readline

n = int(read())


ayo = []

for i in range(n):
    a,b = map(int, read().rstrip().split())
    ayo.append((a,b))

ayo.sort()
'''
3
2 1
8 3
5 7

2 1
5 7
8 3

3
12
15
'''
start = ayo[0][0] + ayo[0][1]

for cow in ayo[1:] :
    
    if cow[0] < start :
        start += cow[1]
    else:
        start = cow[0] + cow[1]
        
    
print(start)
