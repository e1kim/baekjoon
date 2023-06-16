import sys
    
read= sys.stdin.readline


'''

항상 2행 n열...
DP문제
50 40 vs 10  200 vs 150 140 vs 120  250 vs 
30 100 vs 50 110 vs 120 210 vs 110 200 vs 260
0  50
'''

testcase = int(read())

for i in range(testcase):
    info = []
    n = int(read())
    better = [ [ 0 for i in range(n)] for i in range(3) ] 
    info.append(list(map(int,read().rstrip().split())))
    info.append(list(map(int,read().rstrip().split())))

    #선택은 세가지가 있다.
    #dp문제
    #첫번째 선택
    #-> 다음에는 첫번째 선택불가
    #두번째 선택
    #-> 다음에는 두번째 선택불가
    #선택안함
    #->다음에 아무거나 선택가능
    better[0][0] = info[0][0]
    better[1][0] = info[1][0]
    better[2][0] = 0
    
    for j in range(1,n):       
        better[0][j] = max(better[1][j-1] ,  better[2][j-1] ) + info[0][j]
        better[1][j] = max(better[0][j-1] , better[2][j-1] ) + info[1][j]
        better[2][j] = max(better[0][j-1], better[1][j-1])
        
    print(max (better[0][n-1],better[1][n-1], better[2][n-1]))
    
        
   
    
    
    
    
