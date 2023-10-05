n, m, k = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

smell = [[[0, 0]] * n for _ in range(n)]  # 상어 번호와 냄새

priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

def move():
    new_array = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if array[x][y] != 0:
                direction = directions[array[x][y] - 1]
                found = False
                for index in range(4):
                    nx = x + dx[priorities[array[x][y]-1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y]-1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0:
                            directions[array[x][y] -1] = priorities[array[x][y] -1][direction -1][index]
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break
            if found:
                continue
            for index in range(4):
                nx = x + dx[priorities[array[x][y]-1][direction - 1][index] - 1]
                ny = y + dy[priorities[array[x][y]-1][direction - 1][index] - 1]
                if 0 <= nx and nx < n and 0 <= ny and ny < n:
                    if smell[nx][ny][0] == array[x][y]:
                        directions[array[x][y] - 1] = priorities[array[x][y] -1][direction -1][index]
                        new_array[nx][ny] = array[x][y]
                        break
    return new_array

time = 0
while True:
    update_smell()
    new_array = move()
    array = new_array
    time += 1

    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break