import sys


read  = sys.stdin.readline

INF = int(1e9)

n,m = map(int, read().rstrip().split())

start = int(read())


graph = [ [] for _ in range(n+1) ]
visited = [ False for _ in range(n+1) ]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,read().split())
    graph[a].append((b,c))
    #방향그래프이기 때문에 한 정점에서 다른 정점으로 이동하는 방향이 정해짐.

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index #최단거리 노드 반환

def dijkstra(start):
    distance[start] = 0
    visited[start]  = True

    for i in graph[start]:
        distance[i[0]] = i[1] #시작노드의 인접노드에 대해 모두 확인

    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for next in graph[now]:
            cost = distance[now] + next[1] #현재 거리 + 다음 거리의 
            if cost < distance[next[0]] :
                distance[next[0]] = cost







dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])


