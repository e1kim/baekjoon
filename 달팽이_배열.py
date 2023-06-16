def make_outer(arr, st, length, num):
    last = st+length-1 
    for c in range(st, last + 1):
        print(c , end= ' ')
        arr[st][c] = num
        num += 1
    print()
    for r in range(st + 1, last + 1):
        print(r, end= ' ')
        arr[r][last] = num
        num += 1
    print()
    for c in range(last - 1, st - 1,-1):
        print(c, end= ' ')
        arr[last][c] = num
        num += 1
    print()
    for r in range(last - 1, st, -1):
        print(r,end= ' ')
        arr[r][st] = num
        num += 1
    print()
    return num

    
def main():
    n = int(input())
    count  = 1
    arr = []
    for i in range(n):
        arr.append([])
        for j in range(n):
            arr[i].append(0)
    #arr = [[0 for j in range(n)] for i in range(n)]
    num, st = 1, 0
    while n > 0:
        num = make_outer(arr, st, n, num)
        n -= 2
        st += 1
    

    for i in range(len(arr[0])):
        for j in range(len(arr[0])):
            print(arr[i][j],end=' ')
        print()
    
        

    
if __name__=="__main__":
    main()
