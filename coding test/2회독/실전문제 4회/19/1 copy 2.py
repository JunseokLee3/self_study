from collections import deque
INF = 1e9

n = int(input())

array =[]
for _ in range(n):
    array.append(list(map(int, input().split())))

now_x, now_y = 0, 0
now_size = 2

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i , j
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    # 최단거리 저장하는거 불러올때 마다 초기화
    dist  = [[-1] * n for _ in range(n)]
    q = deque() # q.deque([(now_x, now_y)])
    q.append((now_x, now_y))
    while q: # q 바닥 날때 까지
        x, y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and  0 <= ny < n:
                # 사각혀 안
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    # 최단거리등록 X 그리고 크기 작은거
                    dist[nx][ny] == dist[x][y] + 1
                    q.append((nx,ny))
    return dist
    
def find(dist):
    ## 찾는 거면 찾는 위치가 중요 하지 않을까?
    x, y = 0, 0 # 찾는 위치 불러올때마다 초기화
    min_dist = INF # 이것도 초기화
    for i in range(4):
        for j in range(4):
            if dist[i][j] != 1 and array[i][j] < now_size and 1 <= array[i][j]:
                # i,j의 좌표 중에서 위의 조건을 달성 하는 i, j 뽑기
                if min_dist > dist[i][j]:
                    x, y = i, j
                    min_dist = dist[i][j]
            
    if min_dist == INF: # 무한이면 없는거야
        return None
    else:
        return x, y, min_dist
result = 0
ate = 0

while True:
    # 최단거리 찾고
    # 찾기
    # 찾기(최단거리)
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        # 여기는 먹는 곳을 찾았을 때야
        now_x, now_y = value[0], value[1]
        result += value[2]
        array[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size +=1
            ate = 0

