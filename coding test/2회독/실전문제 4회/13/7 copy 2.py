from collections import deque
n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1, 0, 1 ,0]
dy = [0, -1, 0, 1]

def process(x, y, index):
    united = [] # 이것도 시작과 동시에 초기화 됨
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    while q:
        x, y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 문제 조건
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    count += 1
                    summary += graph[nx][ny]
                    q.append((nx,ny))
                    united.append((nx,ny))
                    union[nx][ny] = index
    for i, j in united:
        graph[i][j] = summary // count

total_count = 0

while True:
    # 시작할때마다 union 초기화 해야 하나?
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j, index)
                index +=1
    if index == n * n : # 이말은 각게 다 독립
        break
    total_count += 1

print(total_count)
