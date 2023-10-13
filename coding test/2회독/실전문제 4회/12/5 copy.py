n = int(input())
k = int(input())

data = [[0] * (n +1) for _ in range(n+1)]
info = []

for _ in range(n):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

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





