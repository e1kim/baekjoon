import sys
read = sys.stdin.readline


def main():
    
    n = int(read())
    step = n # 이동갯수
    a = [[0 for j in range(n)] for i in range(n)]
    
    c = -1 #열
    r = 0  #행
    d = 1  #방향
    cnt = 1 # value

    #처음 두번은 증가방향, 다음두번은 감소방향.. 무한루프
    while step > 0:
        for i in range(step):
            c += d
            a[r][c] = cnt
            print(r,c,end=' ')
            cnt += 1
        step -= 1
        print()
        for i in range(step):
            r+= d
            a[r][c] = cnt
            print(r,c,end=' ')
            cnt += 1
        d = d*(-1)
    
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = ' ')
        print()

if __name__ == '__main__':
    main()
