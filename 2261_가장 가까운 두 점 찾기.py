import sys
from math import *
INF = sys.maxsize

global arr
read = sys.stdin.readline
def getDistance(point1, point2):
    return (point1[0]- point2[0])**2 + (point1[1]-point2[1])**2

def divide(start,end):
    if start==end:
        return float('inf')
    elif end-start==1:
        return getDistance(arr[end],arr[start])
    
    mid=(start+end)//2
    
    temp=min(divide(start,mid),divide(mid,end))

    candicate=[]
    #x축 기준으로 가까운 후보 점들을 candicate에 넣는다.
    for i in range(start,end+1):
        if (arr[mid][0]-arr[i][0])**2<temp:
            candicate.append(arr[i])
    candicate.sort(key=lambda x:x[1]) #y축 기준으로 정렬
    
    lc=len(candicate)
    for i in range(lc-1): #후보 1
        for j in range(i+1,lc): #후보2~~~ 와 비교
            
            #후보군과의 거리
            if (candicate[i][1]-candicate[j][1])**2<temp:
                temp=min(temp,getDistance(candicate[i],candicate[j]))
            else:
                break
    return temp

n = int(read())
    
arr = [list(map(int,read().rstrip().split())) for i in range(n)]
    

arr.sort()

print(divide(0,n-1))
