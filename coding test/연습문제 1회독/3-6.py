# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될때까지 1씩빼기
    target = (n //k) *k
    result += (n - target)
    n = target
    # N이 K보다 적을 떄(더 이상 나눌 수 없을 때 ) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //=k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)

# 이거 문제 이해하는데 오래 걸림
    # target = (n //k) *k
    # result += (n - target)
# 을 이해 해야 하는데 
# 빼기 관점에서 보아야 함

# n에서 k를 나눈 몫에 대한 정수를 곱하기 K를 한것을
# 다시 n에 빼는 행위가 나머지에  나중에 1을 더하는 것을 다시 하는 것으로 생각할 수 있음
# 따라서 if을 거치면 중간에 나가는것은 딱 그 위치가 좋은거고
# 나누기 할때 result += 1 를 해주어서 count 해준다.
# result += (n-1) 이값은 if에서 탈출했을 때 마지막 값에 대해서 처리를 해준다.