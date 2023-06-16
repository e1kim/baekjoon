import sys
from itertools import *

n = int(input())
read = sys.stdin.readline


array = list(map(int, read().rstrip().split()))

ok = list(permutations(array,n))



maxx = 0

for p in ok :
    total = 0
    for i in range(1,len(p)):
        total += abs(p[i-1] - p[i])

    maxx = max(maxx,total)
print(maxx)
