import sys


read = sys.stdin.readline
modul = 1000000007

def main():
    N = int(read())
    a = read().rstrip()
    s = []
    flag = False

    for i in range(N):
        if flag:    # 괄호 연속으로 여닫아서 숫자 넣는 경우
            flag = False
            continue
        # 연속으로 여닫는 경우 숫자 넣기
        elif a[i] == '(' and a[i:i+2] == '()':
            flag = True
            x = 2
            if len(s) > 0 and type(s[-1]) is int:
                x = ((x % modul) + (s[-1] % modul)) % modul
                s.pop()
            s.append(x % modul)

        elif a[i] == '[' and a[i:i+2] == '[]':
            flag = True
            x = 3
            if len(s) > 0 and type(s[-1]) is int:
                x = ((x % modul) + (s[-1] % modul)) % modul
                s.pop()
            s.append(x % modul)
        ################# 여기 밑으로는 () [] 이렇게 연속으로 나오지 않는 경우 #################
        # 여는 괄호 나온 경우는 무조건 push
        elif a[i] == '(' or a[i] == '[':
            s.append(a[i])

        # 닫는 괄호 ] or ) 나오는 경우
        else:
            x = s[-1]
            s.pop()
            # 현재 닫는 괄호에 따른 값 곱하기
            if a[i] == ')':
                x *= 2
            else:
                x *= 3
            s.pop()

            # 숫자인 경우는 덧셈 해줘야 됨
            if len(s) > 0 and type(s[-1]) is int:
                x = ((x % modul) + (s[-1] % modul)) % modul
                s.pop()
            s.append(x % modul)
    res = s[-1] % modul
    s.pop()

    if len(s) == 0:
        print(res)
        return
    elif s[-1] == '[':
        res = (res * 3) % modul
    elif s[-1] == '(':
        res = (res * 2) % modul

    print(res)


if __name__ == "__main__":
    main()

