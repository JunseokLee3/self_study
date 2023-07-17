# N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 적은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)


# 리스트를 받으면서 작은 수를 찾은다음 result=0을 이용하여 max를 하는 구나