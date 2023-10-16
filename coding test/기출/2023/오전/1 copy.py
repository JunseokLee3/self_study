from collections import deque

n, m, k = tuple(map(int, input().split()))

board = [
    list(map(int, input().split()))
    for _ in range(n)
]

rec = [
    [0] * m 
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dxs2 = [0, 0, 0, -1, -1, -1, 1, 1, 1]
dys2 = [0, -1, 1, 0, -1, 1, 0, -1, 1]

turn = 0

vis = [
    [0] * m 
    for _ in range(n)
]

back_x = [
    [0] * m 
    for _ in range(n)
]

back_y = [
    [0] * m
    for _ in range(n)
]

is_active = [
    [False] * m
    for _ in range(n)
]

class Turrent:
    def __init__(self, x, y, r, p):
        self.x =x 
        self.y = y
        self.r = r
        self.p = p

live_turret = []

def init():
    global turn
    turn += 1

    for i in range(n):
        for j in range(m):
            vis[i][j] = False
            is_active[i][j] = False

def awake():
    live_turret.sort(key = lambda x : (x.p, -x.r, -(x.x + x.y ), -x.y))

    weak_turret = live_turret[0]
    x = weak_turret.x
    y = weak_turret.y

    board[x][y] += n + m
    rec[x][y] = turn
    weak_turret.p = board[x][y]
    weak_turret.r = rec[x][y]
    power = weak_turret.p
    live_turret[0] = weak_turret


def laser_attack():
    weak_turret =  live_turret[0]
    sx = weak_turret.x
    sy = weak_turret.y
    power = weak_turret.p

    strong_turret = live_turret[-1]
    ex = strong_turret.x
    ey = strong_turret.y

    q = deque()
    vis[sx][sy] = True
    q.append((sx, sy))

    can_attack = False
    while q:
        x, y = q.popleft()

        if x == ex and y == ey:
            can_attack = True
            break

        for dx, dy in zip(dxs, dys):
            nx = (x + dx + n) % n
            ny = ( y + dy + n) % n

            if vis[nx][ny]:
                continue

            if board[nx][ny] == 0:
                continue

            vis[nx][ny] = True
            back_x[nx][ny] = x
            back_y[ny][ny] = y
            q.append((nx,ny))

    if can_attack:
        board[ex][ey] -= power
        if board[ex][ey] < 0:
            board[ex][ey] = 0
        is_active[ex][ey] = True

        cx = back_x[ex][ey]
        cy = back_y[ex][ey]

        while not (cx == sx and cy == sy):
            board[cx][cy] -=  power //2
            if board[cx][cy] < 0:
                board[cx][cy] = 0
            is_active[cx][cy] = True

            next_cx = back_x[cx][cy]
            next_cy = back_y[cx][cy]

            cx = next_cx
            cy = next_cy

    return can_attack

def bomb_attack():
    weak_turret = live_turret[0]
    sx = weak_turret.x
    sy = weak_turret.y
    power = weak_turret.p

    strong_turret = live_turret[-1]
    ex = strong_turret.x
    ey = strong_turret.y

    for dx2, dy2 in zip(dxs2, dys2):
        nx = (ex + dx2 + n) % n
        ny = (ey + dy2 + m) % m

        if nx == sx and ny == sy:
            continue

        if nx == ex and ny == ey:
            board[nx][ny] -= power
            if board[nx][ny] < 0:
                board[nx][ny] = 0
            is_active[nx][ny] = True

        else:
            board[nx][ny] -= power // 2
            if board[nx][ny] < 0:
                board[nx][ny] = 0
            is_active[nx][ny] = True

def reserve():
    for i in range(n):
        for j in range(m):
            if is_active[i][j]:
                continue
            if board[i][j] == 0:
                continue
            board[i][j] += 1

for _ in range(k):
    live_turret = []
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                new_turret = Turrent(i, j, rec[i][j], board[i][j])
                live_turret.append(new_turret)
    if len(live_turret) <= 1:
        break

    init()

    awake()

    is_suc = laser_attack()
    if not is_suc:
        bomb_attack

    reserve()

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, board[i][j])

print(ans)