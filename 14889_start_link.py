import sys

read = sys.stdin.readline
n = int(read())

Min = 1e9

def go(idx,cnt):
    start = 0
    link = 0

    global Min, array
    if idx == n//2:
        for i in range(n):
            for j in range(n):
                if check[i] and check[j] :
                    start += array[i][j]
                if check[i] == 0 and check[j] == 0 :
                    link += array[i][j]

        tmp = abs(start-link)
        if Min > tmp :
            Min = tmp
        return
    
    for i in range(cnt,n+1):
        check[i] = 1
        go(idx + 1, i + 1)
        check[i] = 0
                    


array = []
check = [ 0 for i in range(n+1)]
for i in range(n):
    array.append(list(map(int,read().rstrip().split())))
    
go(0,1)
print(Min)
    
    
