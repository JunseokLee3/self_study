n = int(input())
k = int(input())
<<<<<<< HEAD
data = [[0] * (n +1) for _ in range(n+1)]
=======
data = [[0] * (n + 1) for _ in range(n+1)]
>>>>>>> c090cfd305ded109f01317efb20f92a84a22fb6c
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

<<<<<<< HEAD
def turn(direciton, c):
    if c == 'L':
        direction = (direciton -1)  % 4
    else:
        direction = (direction + 1) % 4
=======
def turn(direction, c):
    if c == 'L':
        direction  = (direction - 1) % 4
    else:
        direction = (direction +1) %4
>>>>>>> c090cfd305ded109f01317efb20f92a84a22fb6c
    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
<<<<<<< HEAD
    time = 0 
=======
    time = 0
>>>>>>> c090cfd305ded109f01317efb20f92a84a22fb6c
    index = 0
    q = [(x, y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
<<<<<<< HEAD
        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] == 2
                q.append((nx, ny))
=======
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
>>>>>>> c090cfd305ded109f01317efb20f92a84a22fb6c
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
<<<<<<< HEAD
        if index < l and time == info[index][0]:
=======
        if index < 1 and time == info[index][0]:
>>>>>>> c090cfd305ded109f01317efb20f92a84a22fb6c
            direction = turn(direction, info[index][1])
            index += 1
    return time

<<<<<<< HEAD
print(simulate())

=======
print(simulate())
>>>>>>> c090cfd305ded109f01317efb20f92a84a22fb6c
