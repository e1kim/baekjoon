import sys

read = sys.stdin.readline




n,m = map(int, read().rstrip().split())
array = list(map(int,read().rstrip().split()))

mx = max(array)

total = sum(array)
low = 1
mid = 0
high = total



def check(mid):
    if mid < mx:
        return False
    temp = mid
    cnt = 0
    for i in array:
        if i > mid:
            cnt +=1
            mid = temp

        mid -= i
    
    cnt += 1
    
    return cnt <= m

while low <= high:
    mid = ( low + high )//2
    
    if check(mid):
        high = mid -1
        res = mid

    else:
        low = mid +1

print(res)
    
    
