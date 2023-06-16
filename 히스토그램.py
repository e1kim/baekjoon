import sys;input=sys.stdin.readline
from collections import deque



'''
stack을 이용해 뒤로 돌아가며 가능한 높이를 모두 구해주는 방법이다.

일단 나보다 낮은애가 나오면 내 뒤로 돌아보면서 낮은애들 높이에 나로부터의 가로거리를

곱한 넓이를 전부 비교해 최댓값을 가져간다. 나보다 낮은 곳이 나오면 다시 탐색한다.


7
2
1
4
5
1
3
3


8

'''

n = int(input())

graph = []

for i in range(n):
    temp = int(input())
    graph.append(temp)
graph.append(0) #맨 마지막에 0을 넣어야 최종적인 전체 가로에서 최소 높이를 곱한 것이 구해짐.

stack = [(0,graph[0])]
result = graph[0]

for now in range(1,n+1):
    left = now
    while stack and graph[now] < stack[-1][1] :
        left , height = stack.pop()
        result = max(result, height*(now-left))
        
    stack.append( (left,graph[now]))
    

print(result)
        
    
