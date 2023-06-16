import sys

input=sys.stdin.readline

N, K = int(input()), int(input())

low, high = 1, K

def count(n):
    cnt = 0
    for i in range (1,N+1):
        a = n // i
        if a > N:
            cnt += N
        else:
            cnt += a   
        #cnt += min(N,a)
         
    return cnt

def binary_search(low, high):
    while low < high:
        mid = (low + high)//2
        
        if count(mid) < K: low = mid+1
        else: high = mid

    return low



print (binary_search(low, high))


