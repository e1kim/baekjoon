import sys
read = sys.stdin.readline

import heapq
class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다

    '''
    
    def __init__(self) :
        self.data = []


    def push(self, value) :

        heapq.heappush(self.data, (abs(value), value))

    def pop(self) :
        if len(self.data) > 0:

            heapq.heappop(self.data)
        
            


    def top(self) :
        if len(self.data) == 0 :
            return 0
        else :
            return self.data[0][1]


n = int(read().rstrip())
pq = PriorityQueue()

for i in range(n):
    temp = int(read().rstrip())
    if temp == 0:
        print(pq.top())
        pq.pop()
    else:
        pq.push(temp)
        
    
