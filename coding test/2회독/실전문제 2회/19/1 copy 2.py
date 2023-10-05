from collections import deque
INF = 1e9

n = int(input())

# 그래프가 필요한가? bfs로 접근 해야 한다.

# 정보가 담긴 graph 초기화
graph = [[0] * (n) for _ in range(n)]
# 이거 필요한가?

# 초기 정보 초기화
now_x, now_y = 0, 0 # 일단 0
now_size = 2 # 주어진 조건

# array로 정보를 받구나
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i , j # i, j에 now_x, now_y
            array[now_x][now_y] = 0  # data 에서 이도잉 용이하게 0으로 수정

dx =[-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 먼저 bfs '최단거리만 계산"
def bfs():
    q = deque([(now_x, now_y)])
    dist = [[-1] * (n) for _ in range(n)] # 이거 최단거리 저장용 , 초기화
    dist[now_x][now_y] = 0 # 여기서0 하는 이유가 뭐지? 
    while q:
        x, y = q.popleft()
        # 아아 dist o으로 만들어야 되네
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                # 일단 맵 안에 작동하게 만듬
                # 다음 아래 조건이 필요? 어떤조건 지금은 이동 가능한지 확이하기 위한 것이기 때문에 
                # dist == -1 과 data[nx][ny] <= now_size
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    #이동조건 확인 완료
                    # dist 업데이트
                    dist[nx][ny] = dist[x][y] + 1                    
                    q.append((nx, ny))
                    # q에 다시 추가하면 x,y로 뽑히면서 됨

    return dist

                
# 자 최단거리 찾았으면 이제, 찾아야지?
def find(dist):
    # 어떻게 찾지?
    x, y = 0, 0  # 왜 이거를 0,0으로 초기화 하지? -> 초기화 해야 되네
    min_dist = INF
    # 우선 맵 전체를 다 확인하면서 보자
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and array[i][j] < now_size: # dist -1이 아닌곳과 now_size< 인 값을 뽑아야함.
                if dist[i][j] < min_dist: # 계속 제일 작은 것을 확인
                    min_dist = dist[i][j]
                    x, y = i, j
    if min_dist == INF: #만약 INF면 최단거리가 안나오는거고 없다는거
        return None
    else:
        return x, y, min_dist
    
result = 0
ate = 0

while True:
    value = find(bfs()) # bfs 최거리 확인, find() 에서 최단거리 찾기

    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1] # now_x, now_y = 0, 0 초기화하고 위에서 위치 설정함
        result += value[2]  # 최단거리에 있는 물고기 비용
        array[now_x][now_y] = 0 # 물고기 먹었으면 0으로 바꿈
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0

        

