from itertools import combinations

n,m = map(int, input().split())

data = [[0] * n for _ in range(n)]

array = []
house, chicken = [], []
for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            house.append((i, j))
        elif array[i][j] ==2:
            chicken.append((i,j))

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        if data[c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken, m))
# 후보자 뽑음

def calculate(candidate):
    
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+ abs(cx - cy))
            # temp가 나왔어
        result += temp # house 중에서 가장 가까운 치킨과 거리  뽑은거 더하기
    return result



result = 1e9
# 결과 
# 후보자들 중에서 비교 해서 가장 작은거 뽑아야 합
for candidate in candidates:
    ## 무엇을 해야 하지?
    # 후보자로 무엇을 해야되
    result  = min(calculate(candidate), result)



print(result)
