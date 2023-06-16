import sys
from math import *


read = sys.stdin.readline
'''

2
5 3
8 1 7 3 1
3 6 1

1 1 3 7 8
1 3 6




3 4
2 13 7
103 11 290 215

'''

def lower_bound(nums, target):
    
    left, right = 0, len(nums)
    
    while left < right:  #left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = left + (right - left) // 2
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return right

testcase = int(read())

for i in range(testcase):
    n, m = map(int, read().rstrip().split())
    A = list(map(int, read().rstrip().split()))
    A.sort()
    B = list(map(int,read().rstrip().split()))
    B.sort()
    count = 0
    
    for a in A:
        count += lower_bound(B,a)
    print(count)

        
