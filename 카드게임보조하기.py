import heapq

class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''
    def __init__(self) :
        self.data = []

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        heapq.heappush(self.data,-1 * value)
        
    def pop(self,value) :
        Reload = []
        if len(self.data) > 0: 
            while(True):
                if self.data[0] == -1 * value:
                    heapq.heappop(self.data)
                    break
                else:
                    Reload.append(self.data[0])
                    heapq.heappop(self.data)

            for i in Reload:
                heapq.heappush(self.data,i)
        
    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        if (len(self.data) == 0): 
            return -1
        else : 
            return (self.data[0] * -1)

def main():
    n = int(input())
    pq = PriorityQueue()
    
    for i in range(n):
        line = list(map(int,input().split()))

        if len(line) == 1:
            print(pq.top())
        else:
            select,x = line[0], line[1]
            if select == 1:
                pq.push(x)
            else:
                pq.pop(x)

    
    

if __name__=="__main__":
    main()
