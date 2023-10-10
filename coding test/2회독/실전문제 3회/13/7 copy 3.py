from collections import deque

n, l, r = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def process(x, y, index):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = index
    count = 1
    summary = data[x][y]
    while q: # q가 빌때까지 하자
        x, y = q.popleft()
        for i in range(n):
            for j in range(n):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n  and 0 <= ny < n and union[nx][ny] == -1: #연합 아닌것도 확인
                    if l <= abs(data[nx][ny] - data[x][y]) <= r:
                        united.append((nx, ny)) # 연합된 것에 확인
                        count += 1
                        q.append((nx, ny))
                        union[nx][ny] = index
                        summary += data[nx][ny]
    for i, j in united:
        data[i][j] = summary // count

        
total_count = 0
while True:
    union = [[-1] * n for _ in range(n)]  # 어디 연합인지 표시용
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                #### 무언가 해야 하는데
                # 일단 1. i,j를 기준으로 움직이면서 
                # 확인 # 그리고 거기서 다시 i, j  움직이면서 확인
                # 마지막에 인구이동
                # 하나하나 확인하고 거기서 BFS 로 가는것이 맞는것 같에 
                # 쌓이고 앞에 쌓인거 빼는 방식이니깐 deque
                # 결구 코드가 가니 함수로 가자
                # 만약 하고 나서 없으면?
                # 어 일단 연합을 n * n의  개수 로 하고 마지막에 index == n *n 도달하면 다 끝난거니깐 break하자
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1

print(total_count)