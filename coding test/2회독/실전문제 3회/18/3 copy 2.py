n, m, k = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

# 격자에 다 정보가 담김

directions =list(map(int, input().split()))
priorities= [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))
# 방향과 우선순위 들어 옴

smell = [[[0,0]] * n for _ in range(n)]  # n*n 격자의 상어종류와 냄새남은 시간 저장

# 문제에 동시에 이동한다
## 냄새가 없는 곳으로 이동한다 

dx = [-1, 1, 0,0 ]
dy = [0, 0, -1, 1]


def smell_update():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

# 격자에 누가 있는지 확인 부터하자
def move():
    for i in range(n):
        for j in range(n):
            if array[i][j] != 0: # 상어 발견!
                direction = directions[array[i][j] -1]
                x, y = i, j
                found = False
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] -1][direction-1][index]-1]
                    ny = y + dy[priorities[array[x][y] -1][direction-1][index]-1]               
                    if smell[nx][ny][1] == 0:# 여기서 냄새가 없다면
                        # 그다음 방향 바뀔 수 있으니깐 방향 바꾸고
                        directions[array[x][y] -1]  = priorities[array[x][y] -1][direction-1][index]
                        
                        if array[nx][ny] == 0:
                            array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        else: 
                            array[nx][ny] = min(array[x][y], array[nx][ny])
                        found =True
                        break
                # 만약에 주위에 다 냄새가 있어?
                if found:
                    continue
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] -1][direction-1][index]-1]
                    ny = y + dy[priorities[array[x][y] -1][direction-1][index]-1]   
                    if smell[nx][ny][0] == array[x][y]:
                        directions[array[x][y]  - 1] = priorities[array[x][y] -1][direction-1][index]
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
count = 0
while True:
    # 냄새 업데이터
    smell_update()
    move()
    count +=1

    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False

    if check:
        print(count)
        break

    if count >= 1000:
        print(-1)
        break
