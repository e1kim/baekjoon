import sys
n = int(input())
read = sys.stdin.readline
array=[]
rank = []
for i in range(n):
    a,b = map(int,read().rstrip().split())
    array.append((a,b))
    rank.append(0)


for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if array[i][0] <array[j][0] and array[i][1] < array[j][1] :
            rank[i] += 1
        

for i in rank:
    print(i+1, end=' ')
