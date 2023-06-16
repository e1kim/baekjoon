import sys


n = int(input())
'''
array = [0,1,2,3,4,5,6,7,8,9,
         10,20,21,30,31,32,40,41,42,43,
         50,51,52,53,54,60,61,62,63,64,
         65,70,71,72,73,74,75,76,80,81,
         82,83,84,85,86,87,90,91,92,93,94,95,96,97,98
         210,310,320,321,410]
'''

array = [ 0 for i in range(1200)]
for i in range(10):
    array[i] = i

idx = 0
add = 0
can = 1

if n<=9:
    print(array[n])
elif n>=1023:
    print(-1)
else:  
    for i in range(10,n+1):
        if array[idx] % 10 > add : #마지막자리수가 add 보다 크면 추가!
            array[i] = array[idx] * 10 + add
            add += 1
        else:
            while array[idx] % 10 <= add:
                idx += 1
                add = 0
            
            array[i] = array[idx] * 10 + add
            add += 1
            
        
    
    #print(array[:n+1])
    print(array[n])
