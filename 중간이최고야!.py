import heapq


def find_mid(nums) :
    '''
    n개의 정수들을 담고 있는 배열 nums가 매개변수로 주어집니다.
    nums의 각 정수들이 차례대로 주어질 때, 매 순간마다 
    "지금까지 입력된 수 중에서 중간값"을 리스트로 저장하여 반환하세요.
    '''
    
    result = []
    small = [] #최대 힙
    big = [] #최소 힙

     
    for i in range(len(nums)):
        x = nums[i]
        
        if not small or not big:
            heapq.heappush(small,-x)

        else:
            if x >= -small[0]:
                heapq.heappush(big,x)
            else:
                heapq.heappush(small,-x)
        
        while not (len(small) == len(big) or len(small) == len(big) + 1):
            if (len(small) > len(big)) :
                heapq.heappush(big, -heapq.heappop(small))
            else:
                heapq.heappush(small, -heapq.heappop(big))
        
        result.append(-small[0])


    return result
def main():
    x = int(input())
    nums = [int(v) for v in input().split()]
    
    print(*find_mid(nums))

if __name__=="__main__":
    main()
