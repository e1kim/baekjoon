import sys
import heapq

read  = sys.stdin.readline
INF = int(1e9)
n,m = map(int, read().rstrip().split())
start = int(read())

graph = [ [] for _ in range(n+1) ]
heap = []
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,read().split())
    graph[a].append((b,c))
    #방향그래프이기 때문에 한 정점에서 다른 정점으로 이동하는 방향이 정해짐.

def dijkstra(start):
    distance[start] = 0

    for i in graph[start]:
        heapq.heappush(heap ,(i[1], i[0]))
    #시작노드의 인접노드에 대해 모두 확인
    while heap:
        weight, now = heapq.heappop(heap)
        if distance[now] <= weight:
            continue
        distance[now] = weight
        for n in graph[now]:
            cost = distance[now] + n[1]
            if cost < distance[n[0]]:
                heapq.heappush(heap,(cost,n[0]))
        

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])


