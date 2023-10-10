n, m, k = map(int, input().split())

for i in range(n):
    array = list(map(int,input().split()))
        
directions = list(map(int, input().split()))

priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

count = 0

for i in range(n):
    for j in range(n):
        if array[i][j] != 0:
            direction = directions[array[i][j] -1]
            if sme

