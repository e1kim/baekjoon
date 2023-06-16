#2559_수열


import sys

read = sys.stdin.readline


n,k = map(int, read().rstrip().split())

array = list(map(int,read().rstrip().split()))

save= sum(array[:k])

Max = save
for i in range(k,n):
    save += array[i]
    save -= array[i-k]
    if save > Max:
        Max = save
print(Max)
    
