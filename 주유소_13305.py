'''
N
도로의 길이 N-1개
리더당 가격 N개
4
2 4 3 1
5 3 2 4 1
10
22

'''

n = int(input())

cost = list(map(int,input().split()))
oil = list(map(int,input().split()))
'''
point:
현재 도시가 다음 도시보다 작으면 구매, 그 다음으로 넘어감.


'''

total = 0
point = 0
for i in range(n-1):
    if i == point:
        total += cost[i] * oil[i]

    if i+1<= n-2:
        if oil[point] < oil[i+1]:
            total += cost[i+1] * oil[point]
        else:
            point = i+1
        
print(total)
    
