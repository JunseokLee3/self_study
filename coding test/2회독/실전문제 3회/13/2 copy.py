n, m = map(int, input().split())
# n 세로
# m 가로
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


# 깊이 우선 탐색(DFS)
def virus(x, y):
    for i  in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵 안전 영역 크기 게산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score +=1
    return score

# 깊이 우선 탐색 DFS
def dfs(count):
    global result
    if count ==3:
        for i in range(n):
            for j in range(m):
                temp[i][j] == data[i][j]
            for i in range(n):
                for j in range(m):
                    if temp[i][j] == 2:
                        virus(i, j)
            result = max(result, get_score())
            return
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    data[i][j] = 1
                    count += 1
                    dfs(count)
                    data[i][j] = 0
                    count -= 1


dfs(0)
print(result)
