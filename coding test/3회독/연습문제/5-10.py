n,m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global count
    for ix in range(4):
        nx = x + dx[ix]
        ny = y + dy[ix]
        if (0<= nx and nx < n) and (0<= ny and ny < m):
            if array[nx][ny] == 0:
              array[nx][ny] = 1
              count += 1
              dfs(nx, ny)

count = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            dfs(i,j)

print(count)
        
        