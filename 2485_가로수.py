def GCD(x, y) :
    '''
    x, y의 최대공약수를 반환하는 함수
    '''
    if x%y == 0:
        return y
    
    return GCD(y,x%y)

def howManyTree(n, myInput) :
    '''
    모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 리턴하는 함수를 구현하세요.
    '''
    
    distance = []
    for i in range(n-1):
        distance.append(myInput[i+1] - myInput[i])
   
    gcd = distance[0]
    for i in range(1,len(distance)):
        gcd = GCD(distance[i],gcd)
        
    total = myInput[-1] - myInput[0] 
    total = total//gcd
    total = total - n + 1
    
    cnt = total
    
    return cnt

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    
    n = int(input())
    myInput = []
    for _ in range(n) :
        myInput.append(int(input()))

    print((howManyTree(n, myInput)))
if __name__ == "__main__":
    main()
