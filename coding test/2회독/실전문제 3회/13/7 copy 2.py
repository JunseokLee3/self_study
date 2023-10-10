from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def process(x, y, index):
    united = []  # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = x + dy[i]
            if 0 <= nx < n and 0 <= ny < y and union[nx][ny] == -1:
                if l <= abs(graph[x][y]- graph[nx][ny]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary // count
        

total_count = 0
while True:
    union = [[-1]* n for _ in range(n)]  # 각 표마다 연합을 표시하는 것을 하나 만들기
    index = 0 # 어차피 맵 크기 만큼 연합 나올껑미 n * n개 만큼
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 연합 안된것만 먼저
                process(i, j, index)  # 여기서 함수 처리
                index += 1  #연합 한번 된거면 한번 체크
    if index == n * n:
        break
    total_count += 1

print(total_count)