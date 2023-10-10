from itertools import combinations
n, m = map(int, input().split())
# n 세로
# m 가로

array = [[0]* m for _ in range(n)]

virus, wall = [],[]

for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(m):
        if array[i][j] == 1:
            wall.append((i,j))
        elif array[i][j] == 2:
            virus.append((i, j))

candidates = list(combinations(wall, 3))

dx =[0, 1, 0, -1]
dy = [-1,0,1, 0]
def virus_expand(candidates):
    x, y= virus.pop(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < n: # 벽 안이야
            if array != 1 and array != 2:
                array[nx][ny] = 2
                virus.append((nx,ny))

while True:
    for _ in candidates:
        



    


