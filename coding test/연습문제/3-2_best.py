# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N 개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수를 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두번째로 큰 수

result = 0

# 가장 큰 수ㄹ가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)  # 최종 답안 출력

# 수학이 별 쓸모 없을 것 같지만 이것은 3_2의 문제를 순열을 이용하여 풀어 낸것이다.
# 수학은 안보이는 곳에 규칙을 찾아서 계산을 간편하게 하는 것이 도움이 되는 것 같다.
# 이런식으로 문제를 풀어야 겠다.
