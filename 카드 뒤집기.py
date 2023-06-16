
a = int(input())
s = input()
s = list(s)

#풀이는 2번 행부터 보면서 문제의 조건대로 이전 행의 '#'인 부분은 뒤집어준 뒤에,
#이전 행에서 뒤집혀진 부분은 현재 행에서 다시 뒤집어주기 위해 현재 행을 '#'으로 바꿔주면 됩니다.
visited = []
gr = []
for i in range(a):
    visited.append([])
    gr.append([])
    for j in range(a):
        if i == 0:
            gr[i].append(s[j])
            visited[i].append(0)
            continue
        visited[i].append(0)
        gr[i].append(0)

for j in range(a):
    print(s[j],end='')
print()
for i in range(a-1):
    for j in range(a):
        if s[j] == '#': #현재문자열이 검정색이면 방문해서 변화시킨다.
            if j-1 >= 0 :
                visited[i][j-1] ^=1
            if j+1 < a:
                visited[i][j+1] ^=1
            if i+1 < a:
                visited[i+1][j] ^=1
    for j in range(a):#visited를 통한 다음 문자열이다.
        if visited[i][j] == 1:
            s[j] = '#'
        else:
            s[j] = '.'
    for j in range(a):
        print(s[j],end='')
    print()
            
        

        
    
