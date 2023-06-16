import sys
sys.setrecursionlimit(100000)

ans = 0

def prom(x, row, n):
    for i in range(x):
            if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
                return False
    return True


def n_queens(x, n, row):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if prom(x,row,n):
                n_queens(x+1,n,row)
        
def nQueen(n) :
    '''
    n개의 Queen을 배치하는 경우의 수를 반환하는 함수를 작성하세요.
    
    '''

    row = [0] * n
    n_queens(0,n,row)

    
    
    return ans

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    print(nQueen(n))

if __name__ == "__main__":
    main()
