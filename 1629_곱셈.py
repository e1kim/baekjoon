import sys

read = sys.stdin.readline



def getPower(m, n):
    '''
    m^n 을 LIMIT_NUMBER로 나눈 나머지를 반환하는 함수를 작성하세요.
    '''
    global LIMIT_NUMBER
    if n==0:
        return 1
    elif n%2==0:
        temp = getPower(m,n//2)
        return (temp * temp) % LIMIT_NUMBER
    else:
        temp = getPower(m,(n-1)//2)
        return (temp * temp * m) % LIMIT_NUMBER
    
def main():
    '''
    main 함수
    '''
    global LIMIT_NUMBER
    myList = [int(v) for v in input().split()]
    
    LIMIT_NUMBER = myList[2]

    print(getPower(myList[0], myList[1]))
    

if __name__ == "__main__":
    main()
