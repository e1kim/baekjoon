def reverse_function(array):

    array.reverse()
    
    return array

def rotate_function(array,k):
    
    left = array[:-k]
    right = array[-k:]

    return right + left

def main():
    n, q = map(int,input().split())

    array = list(input().split())

    for i in range(q):
        line = list(map(int,input().split()))
        if len(line) == 1:
            array = reverse_function(array)
        else:
            select,k = line[0], line[1]
            array = rotate_function(array,k)
    
    for i in range(n):
        print(array[i], end=' ')
            

if __name__=="__main__":
    main()
