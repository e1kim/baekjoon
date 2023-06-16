import sys;input=sys.stdin.readline
def getSlope(a,b):
    
    return abs((b[1] - a[1])/ (b[0]- a[0]))

def maxSlope(points) :
    '''
    n개의 점들 중에서 2개의 점을 선택했을 때
    얻을 수 있는 기울기의 절댓값 중에서 가장 큰 값을 반환하는 함수
    '''
    points.sort()
    
    MAX = 0
    index1 = 1e9
    index2 = 1e9
    
    for i in range(len(points)-1):
        slope = getSlope(points[i],points[i+1])
        
        if MAX <= slope :
            if MAX < slope:
                MAX = slope
                #두 점의 숫자를 비교해서 작은것을 index1에 넣기.
                if points[i+1][2] > points[i][2]:
                    index1 = points[i][2]
                    index2 = points[i+1][2]
                else:
                    index1 = points[i+1][2]
                    index2 = points[i][2]
            else:
                #MAX == slope
                #기울기가 같은경우 새로운 점(points[i+1][2], aka new)를 기존 점 2개와 비교.
                # new < index1이면 index2에 기존 작은점을 저장.
                #index1에는 new를 저장
                if points[i+1][2] < index1:
                    index2 = index1
                    index1= points[i+1][2]
                elif points[i+1][2] < index2:
                    #기존 큰 점을 new로 update.
                    index2 = points[i+1][2]
                
                    

            
    return (index1+1,index2+1)



"""
greedy algorithm으로 문제해결하기.
점들을 정렬하면 x좌표기준으로 정렬이된다.
x좌표들은 모두 다르기 때문에 같은 x좌표는 존재하지 않고,
따라서 무한대의 기울기 또한 존재 하지 않는다.

기울기가 가장 크게하려면 x축간의 거리가 작아야하고,
y축간의 거리가 커야한다.

x축간의 거리가 작게하기 위해서 x좌표 정렬 뒤
인접한 x좌표들 사이에서의 기울기만 구하면 된다.

기울기의 절댓값이 가장 큰 두 점의 번호 A와 B를 빈 칸을 사이에 두고 출력한다.
(A < B) 그러한 두 점의 쌍이 둘 이상인 경우 A가 가장 작은 것을 출력하고,
만일 A가 가장 작은 답도 여러 가지가 있으면 B가 가장 작은 것을 출력한다.
4
4 0
2 6
3 3
1 3

1 2

(1,3,3)(2,6,1)(3,3,2)(4,0,0)

"""
n = int(input())
points = []

for i in range(n) :
    line = [int(x) for x in input().split()]
    points.append( (line[0], line[1], i))

ans1,ans2 = maxSlope(points)

if n == 1:
    print(1,1)
else:
    print(ans1,ans2)

