n, m, k = list(map(int, input().split()))

# 좌상단 (1,1)

array = []
for i in range(n):
    array.append(list(map(int, input())))

traveler = []
for _ in range(m):
    traveler.append(list(map(int, input().split())))

exit = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

