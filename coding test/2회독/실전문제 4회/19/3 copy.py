n, m, k = map(int,input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

directions= map(int, input())

priorities = [[] for _ in range(m)]

for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

smell = [[[0,0]] * n  for _ in range(n)]

## 동시에 라는 것이 new_ array 에서 array 로 합치면 되
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

## 처음 냄새 뿌리는 거
## 

def smell_update(): #냄새 업데이트야
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1

            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

                # 모든 상어에 대해서 작동해야 함
                
def move():  # 상어만이야 상어가지고 해야되, 그리고 구현 문제이다.
    new_array = [[0] * n for _ in range(n)] # array랑 최대한 유사하게
    for x in range(n):
        for y in range(n):
            if array[i][j] != 0:
                direction = directions[array[x][y] -1]
                found = False
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction -1][index] -1]
                    ny = x + dy[priorities[array[x][y] - 1][direction -1][index] -1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:
                            directions[array[x][y] -1] = priorities[array[x][y] - 1][direction -1][index]
                            if new_array[nx][ny] == 0:  # 이게 생각하기 힘들어 구현 하면서 이거 조건 도 생각해야 하잖아
                                # 그니끈 이거는 글 써가면서 확인 할것을 찾아야해
                                new_array[nx][ny] = array[x][y]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break
                if found:
                    continue

                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction -1][index] -1]
                    ny = x + dy[priorities[array[x][y] - 1][direction -1][index] -1]
                    if 0 <= nx < n and 0 <= ny < n:         
                        # 자기 냄새
                        if smell[nx][ny][0] == array[x][y]:
                            directions[array[x][y] -1] = priorities[array[x][y] - 1][direction -1][index]
                            new_array[nx][ny] = array[x][y]
                            # 난 수낙ㄴ 바꺼야 하나 했어 근데 new _array 로 해서 다행
                            break  # 등록 되면 꺼야됨
    return new_array                    



time = 0
while True:
    smell_update()
    new_array = move()
    array = new_array
    time += 1
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
                break
            
    if check: 
        print(time)
        break

    if time >= 1000:
        print(-1)
        break
#### 냄새
#### 이동
#### array에 상어가 없으면
#### print(tiem)

### if time >= 1000:
    # print(-1)
