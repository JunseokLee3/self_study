from collections import deque

n,m,k = tuple(map(int, input().split()))

board = [
    list(map(int, input().split()))
    for _ in range(n)
]
rec = [
    [0] * m
    for _ in range(m)
]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

dxs2 = [0,  1, 0, -1]
dys2 = [1, 0, -1, 0]

dxs2 = [0, 0, 0, -1, -1, -1, 1, 1, 1] 
dys2 =  [0, -1, 1, 0, -1, 1, 0, -1, 1]

turn = 0

# 빛이 공격을 할때 방문 여부와 경로 방향을 기록
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

# 공격과 무관했는지 여부 저장
is_active = [
    [False] * m
    for _ in range(n)
]

class Turrent:
    def __init__(self, x, y, r, p):
        self.x = x
        self.y = y
        self.r = r
        self.p = p

live_turrent = []

def init():
    global turn
    turn += 1
    for i in range(n):
        for j in range(m):
            vis[i][j] = False
            is_active[i][j] = False

def awake():
    live_turrent.sort(key=lambda x : (x.p, -x.r, -(x.x + x.y), -x.y))

    weak_turrent = live_turrent[0]
    x = weak_turrent.x
    y = weak_turrent.y

    board[x][y] += n + m
    rec[x][y] = turn
    weak_turrent.p = board[x][y]
    weak_turrent.r = rec[x][y]
    is_active[x][y] = True

    live_turrent[0] = weak_turrent

def laser_attack():
    weak_turrent = live_turrent[0]
    sx = weak_turrent.x
    sy = weak_turrent.y
    power = weak_turrent.p

    strong_turrent = live_turrent[-1]
    ex= strong_turrent.x
    ey = strong_turrent.y

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
            nx = ( x + dx + n) % n
            ny = (y + dy + m) % m

            if vis[nx][ny]:
                continue

            if board[nx][ny] == 0:
                continue
            vis[nx][ny] =  True
            back_x[nx][ny] = x
            back_y[nx][ny] = y
            q.append((nx, ny))
    
    if can_attack:
        board[ex][ey] -= power
        if board[ex][ey] < 0:
            board[ex][ey] = 0
        is_active[ex][ey] = True

        cx = back_x[ex][ey]
        cy = back_y[ex][ey]

        while not (cx == sx and cy == sy):
            board[cx][cy] -= power // 2
            if board[cx][cy] < 0:
                board[cx][cy] = 0
            is_active[cx][cy] = True

            next_cx = back_x[cx][cy]
            next_cy = back_y[cx][cy]

            cx = next_cx
            cy = next_cy
    return can_attack

def bomb_attack():
    weak_turrent = live_turrent[0]
    sx = weak_turrent.x
    sy = weak_turrent.y
    power = weak_turrent.p

    strong_turrnet = live_turrent[-1]
    ex = strong_turrnet.x
    ey = strong_turrnet.y

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
            board[nx][ny] -=  power //2
            if board[nx][ny] < 0:
                board[nx][ny] = 0
            is_active[nx][ny] = True

def reverse():
    for i in range(n):
        for j in range(m):
            if is_active[i][j]:
                continue
            if board[i][j] == 0:
                continue
            board[i][j] += 1



for _ in range(k):
    live_turrent = []
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                new_turrent = Turrent(i, j, rec[i][j], board[i][j])
                live_turrent.append(new_turrent)
    if len(live_turrent) <= 1:
        break

    init()
    awake()
    is_suc = laser_attack()
    if not is_suc:
        bomb_attack()

    reverse()

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, board[i][j])

print(ans)