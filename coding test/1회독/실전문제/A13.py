from itertools import combinations

n,m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반집
        elif data[c] == 2:
            chicken.append((r, c)) # clzlswlq

# 모든 치킨집 중에서 m 개의 치킨집을 뽑느 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨 집 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy-cy))
        # 가장 가까운 치킨집까지의 거리를 구하기
        result += temp
        return result

# 치킨 거리의 갑의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)

