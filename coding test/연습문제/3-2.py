# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N 개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수를 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)  # 최종 답안 출력


# 나의 생각: 이런 간단한 것도 생각지도 못했다. 반복과 고민을 충분히 해야 겠다.