import heapq 
def main():
    n,k  = map(int, input().split())
    
    pq = []
    A = list(map(int,input().split()))
    

    for i in range(1,n+1):
        heapq.heappush(pq,A[i-1])
        
        if len(pq)<k:
            continue
        elif len(pq)==k:
            print(pq[0],end=' ')
            
        else:
            heapq.heappop(pq)
            print(pq[0],end=' ')
            


if __name__=="__main__":
    main()
