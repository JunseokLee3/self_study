# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄 씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)

    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result)

# min_value를 큰 것으로 하고 나서
# min() 값을 이용하여 작은 수를 구하는 구나
# 거기서 다음은 max를 이용하여 가장 큰 값을 찾기