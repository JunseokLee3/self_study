import sys
from collections import deque

INT_MAX = sys.maxsize
EMPTY = (-1, -1)

# dx, dy값을 
# 문제에서의 우선순위인 상좌우하 순으로 적어줍니다.
dxs = [-1,  0, 0, 1]
dys = [ 0, -1, 1, 0]

# bfs에 사용되는 변수들입니다.
# 최단거리 결과 기록
step = [
    [0] * n
    for _ in range(n)
]
# 방문 여부 표시
visited = [
    [False] * n
    for _ in range(n)
] 


# (x, y)가 격자 내에 있는 좌표인지를 판단합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# (x, y)로 이동이 가능한지 판단합니다.
def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 2


# start_pos를 시작으로 하는 BFS를 진행합니다.
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
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))


def nearest_basecamp_for_person(person_idx, basecamp_grid):
    min_dist = INT_MAX
    min_x, min_y = -1, -1
    bfs(cvs_list[person_idx])
    for i in range(n):
        for j in range(n):
            if visited[i][j] and basecamp_grid[i][j] == 1 and min_dist > step[i][j]:
                min_dist = step[i][j]
                min_x, min_y = i, j
                
    return min_x, min_y


def simulate():
    basecamp_grid = [[0 if grid[i][j] != 1 else 1 for j in range(n)] for i in range(n)]
    for i in range(m):
        if people[i] == EMPTY or people[i] == cvs_list[i]:
            continue
        bfs(cvs_list[i])
        px, py = people[i]
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

    if curr_t <= m:
        x, y = nearest_basecamp_for_person(curr_t - 1, basecamp_grid)
        people[curr_t - 1] = (x, y)
        basecamp_grid[x][y] = 0
        grid[x][y] = 2


def end():
    for i in range(m):
        if people[i] != cvs_list[i]:
            return False
    return True


people = [EMPTY] * m
curr_t = 0
while True:
    curr_t += 1
    simulate()
    if end():
        break

curr_t
