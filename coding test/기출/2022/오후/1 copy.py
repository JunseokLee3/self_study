import sys
from collections import deque

INT_MAX = sys.maxsize
EMPTY = ( -1, -1)

n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

cvs_list = []
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    cvs_list.append((x - 1, y - 1))

people = [EMPTY] * m

curr_t = 0

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

step = [
    [0] * n
    for _ in range(n)
]

visited =[
    [False] * n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 2

def bfs(start_pos):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

    q = deque()
    q.append(start_pos)
    sx, sy = start_pos
    visited[sx][sy] = True
    step[sx][sy] = 0

    while q:
        x, y= q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))


def simulate():
    for i in range(m):
        if people[i] == EMPTY or people[i] == cvs_list[i]:
            continue

        bfs(cvs_list[i])

        px,py = people[i]

        min_dist = INT_MAX
        min_x, min_y = -1, -1
        for dx, dy in zip(dxs, dys):
            nx, ny = px + dx, py + dy
            if in_range(nx, ny) and visited[nx][ny] and min_dist > step[nx][ny]:
                min_dist = step[nx][ny]
                min_x, min_y = nx, ny

        people[i] = (min_x, min_y)

    for i in range(m):
        if people[i] == cvs_list[i]:
            px, py = people[i]
            grid[px][py] = 2

    if curr_t > m:
        return
    
    bfs(cvs_list[curr_t - 1])

    min_dist = INT_MAX
    min_x, min_y = -1, -1
    for i in range(n):
        for j in range(n):
            if visited[i][j] and grid[i][j] == 1 and min_dist > step[i][j]:
                min_dist = step[i][j]
                min_x, min_y  = i, j

    people[curr_t - 1] = (min_x, min_y)
    grid[min_x][min_y] = 2

def end():
    for i in range(m):
        if people[i] != cvs_list[i]:
            return False
        
    return True

while True:
    curr_t += 1
    simulate()
    if end():
        break
print(curr_t)