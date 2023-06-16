import sys

read = sys.stdin.readline


n,m = map(int, read().rstrip().split())

array = [ 0 for i in range(m)]

down = []
up = []
for i in range(n):
    if i % 2 == 0: #아래 장애물
        down.append(int(read().rstrip()))
    else:
        up.append(int(read().rstrip()))


down.sort()
up.sort()



mini = 1e9
count = 0
cnt = 1
def lower_bound(nums, target):
    
    left, right = 0, len(nums)
    
    while left < right:  #left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = left + (right - left) // 2
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return right
def upper_bound(nums, target):

    left, right = 0, len(nums)

    while left < right:  #left와 right가 만나는 지점이 target값 보다 큰 값이 처음 나오는 위치
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid 

    return right

for i in range(1,m+1):
    low1 = lower_bound(down,i)
    low2 = upper_bound(up,m-i)
    count = n - low1 - low2
    
    if count <= mini :
        if count == mini:
            cnt += 1
        else:
            mini = count
            cnt = 1
            
    
print(mini, cnt)

    
    
    
    
                  
    
        
        
    
