n = int(input())
k = int(input())

<<<<<<< HEAD
data = [[0] * (n +1) for _ in range(n+1)]
=======
data = [[0] * (n+ 1) for _ in range(n+1)]
>>>>>>> c090cfd305ded109f01317efb20f92a84a22fb6c
info = []

for _ in range(n):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

<<<<<<< HEAD
dx = [0, -1 ,0, 1]
dy = [1, 0 , -1, 0]



def simulater():
    x, y = 0,0 # 뱀 처음시작
    direction = 0 # 처음 방향 동쪽
    data[x][y] = 2 # 2는 뱀 있다.
    time = 0
    q = [(x,y)]
    index = 0
    while True:
        
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0: # 빈공간
                q.append((nx, ny))
                data[nx][ny] = 2                
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 2:
                q.append((nx,ny))
                data[nx][ny] = 2
        else: 
            time += 1
            break 
        
        x, y = nx,ny
        time += 1

        if time == info[index][0] and index <l:
            if info[index][1] == 'L':
                direction = (direction -1 ) % 4
            else:
                direction = (direction +1 ) % 4
            index += 1
    return time


print(simulater())





=======
dx = [0,-1 ,0, 1]
dy = [1, 0, -1, 0]

x, y = 1, 1 #시작 부분
direction = 0 # 지금 동쪽
time = 0 # 시간에 따라서 회전하니깐
data[x][y] = 2 # 뱀이 여기 있다는 표시
index = 0 # 어떤 뱀이냐?
q = [(x,y)]
# for _ in range(4) 의 방법을 쓰는거은 방향이 상하좌우일떄 쓴느데
# 지금 그냥 어떤 조건일떄만 변함, 그럼 while True

# turn(direction, info[index][1])
# turn(direciton, info[index][1])
# turn(direciton, info[index][1])
def turn(direction, c):
    if c == "L":
        diretion = (direction -1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    time += 1

    # 그전에 경계 확인 그리고 뱀의 몸통이면 안되잖아
    if 1 <= nx <= n and 1 <= ny <= n and data[x][y] != 2:
        # 공간안이야 -> 이제 공간일때, 그리고 사과일때
        if data[nx][ny] == 1: # 사과일때
            q.append((nx, ny))
            data[nx][ny] = 2
        if data[nx][ny] == 0: # 빈 공간일때
            q.append((nx, ny))
            qx, qy = q.pop(0)  # 꼬리 끝 부분임
            data[qx][qy] = 0
            data[nx][ny] = 2
        x, y = nx, ny
        time += 1
    else:
        time +=1
        break

    # 방향 바꿈
    if time == info[index][0] and index < l:
        if info[index][1] == 'L':
            direction = (direction -1) % 4
        else:
            direction = (direction +1) % 4
    

print(time)
>>>>>>> c090cfd305ded109f01317efb20f92a84a22fb6c
