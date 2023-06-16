import sys


read = sys.stdin.readline


n = int(read())

info = list(map(int,read().rstrip().split()))

info2 = list(reversed(info))



best1 = [1 for i in range(n)]
best2 = [1 for i in range(n)]

prev1 = []
prev2 = []
for i in range(n):
    prev1.append(i)
    prev2.append(i)
    

for i in range(n):
    for j in range(i):
        if info[i]>info[j] and best1[i] < best1[j] + 1:
            best1[i] = best1[j] + 1
            prev1[i] = j
        if info2[i]>info2[j] and best2[i] < best2[j] + 1:
            best2[i] = best2[j] + 1
            prev2[i]=j

best = []
best2.reverse()
for i in range(n):
    best.append(best1[i] + best2[i])

print(max(best) -1 )

            
        
