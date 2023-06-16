def quickSort(array):
    '''
    퀵정렬을 통해 오름차순으로 정렬된 array를반환하는 함수를 작성하세요.
    '''
    if (len(array) < 2 ) :
        return array
    
    pivot = array[0]

    left = small(array[1:],pivot)
    right = big(array[1:],pivot)

    return quickSort(left) + [pivot] + quickSort(right)
    

    return array 
def small(array,pivot):
    data = []
    for a in array:
        if a<= pivot:
            data.append(a)
    return data

def big(array,pivot):
    data = []
    for a in array:
        if a> pivot:
            data.append(a)
    return data

def partiton(array, left, right):
    
    pivot = left
    for i in range(left, right):
        #pivot은 맨 오른쪽 값이 된다.
        if (array[i] < array[right]):
            array[i], array[pivot] = array[pivot], array[i]
            pivot += 1
        
    array[right], array[pivot] = array[pivot] , array[right]
    print("pivot: %d"%pivot)
    return pivot


def main():
    line = [int(x) for x in input("정렬할 수를 입력하세요 (예시:10 2 3 4 5 6 9 7 8 1): ").split()]

    print('정렬 결과:', *quickSort(line))

if __name__ == "__main__":
    main()
