import sys
from collections import deque

INT_MAX = sys.maxsize
EMPTY = ( -1, -1)

n,m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

cvs_list = []
for _ in range(n):
    x, y = tuple(map(int, input().split()))
    cvs_list.append((x-1, y-1))

people = [EMPTY] * m

curr_t = 0

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

step = [
    [0] *n
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 2

def simulate(start_pos):
    for i in range(m):
        if people[i] == EMPTY or people[i] == cvs_list[i]:
            continue

        bfs(cvs_list[i])

        px, py = people[i]

        min_dist = INT_MAX
        min_x, min_y =-1, -1
        for dx, dy in zip(dxs, dys):
            nx, ny = px + dx, py + dy
            


while True:
    curr_t += 1
    simulate()
    if end():
        break