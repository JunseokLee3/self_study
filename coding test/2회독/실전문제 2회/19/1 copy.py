from collections import deque
INF = 1e9
n = int(input())
graph = [[0] * n for _ in range(n)]

# array 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 현재 위치 초기화
now_x, now_y = 0, 0

# 상어 시작 부분 초기화 및 저장
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i,j
            # array도 0으로 바꾸어서 이동할 수 있게  만듬
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, -1 ,0, 1]
now_size = 2

def bfs():
    dist = [[-1] * n for _ in range(n)]
    # dist -1로 초기화 하여서 다 못가는 거롤 바꿈
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and dist[i][j] < now_size:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    x, y = i, j
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result = 0
ate = 0    
while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        array[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0
