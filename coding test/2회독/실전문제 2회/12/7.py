# n, m= map(int, input().split())
# data = []
# for _ in range(n):
#     data.append(list(map(int, input().split())))

# house = []
# chicken = []
# for i in range(n):
#     for j in range(n):
#         if data[i][j] == 1:
#             house.append((i,j))
#         if data[i][j] == 2:
#             chicken.append((i,j))

from itertools import combinations

n, m = map(int, input().split())
chicken , house = [], []

for r in range(n):
    data= list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] ==2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy- cy))
        result += temp

    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)