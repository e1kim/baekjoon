import math 

def rotate_function(array,k):
    
    left = array[:-k]
    right = array[-k:]
    
    return right + left

def main():
    n = int(input())
    
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    mini = math.inf

    for i in range(n):
        similarity = 0
        B = rotate_function(B,1)
        
        for j in range(n):
            similarity += (A[j]-B[j])**2
        if mini > similarity:
            mini = similarity
    
    print(mini)
        

        

if __name__=="__main__":
    main()
