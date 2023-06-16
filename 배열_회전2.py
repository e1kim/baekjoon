def reverse_left_and_right(array):
    for i in range(len(array)):
        array[i].reverse()
    return array

def reverse_up_and_down(array):
    array = array[::-1] 
    return array

def rotate_90_right(array):
    '''
    ex) 2 * 2 array
    (0,0) -> (0,2)
    (0,1) -> (1,2)
    (0,2) -> (2,2)
    회전 후의 행 번호 = 회전 전의 열 번호 
    회전 후의 열 = (N-1 ) - 회전 전의 행
    '''

    N = len(array)
    result = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            result[c][N-1-r] = array[r][c]
    return result

def rotate_90_left(array):
    '''
    123
    456
    789

    (0,0)->(2,0)
    (0,1)->(1,0)
    (0,2)->(0,0)
    회전 후의 열 = 회전 전의 행
    회전 후의 행 = (N-1) - 회전 전의 열 
    '''
    N = len(array)
    result = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            result[N-1-c][r] = array[r][c]
    return result
    

def main():
    n, q = map(int,input().split())
    
    array = []
    for i in range(n):
        input_i = list(map(int,input().split()))
        array.append(input_i)
    


    for i in range(q):
        select = int(input())
        if select == 1:
            array = reverse_left_and_right(array)
        elif select == 2:
            array = reverse_up_and_down(array)
        elif select == 3:
            array = rotate_90_right(array)
        else:
            array = rotate_90_left(array)
    

    for i in range(n):
        for j in range(n):
            print(array[i][j], end=' ')
        print()


if __name__=="__main__":
    main()
