INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+ 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range( 1, n + 1):
        for b in range(1, n + 1):
            graph[q][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1,n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)