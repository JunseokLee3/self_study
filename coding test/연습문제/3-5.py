n,k = map(int, input().split())
result = 0
# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1
print(result)

# 아 result를 0에서 시작해서 쌓아 놓는 방식이구나
# 그리고 큰 수 부터 나누는 것이 시작이다. 결국 result는 빼는거랑 나누는 횟수를 가장 작게 하는 것이기 떄문에
# 나누는것이 빼는것보다 크기 때문에 이렇게 한거구나
# 그리고 마지막 남은 수에 대하여 1씩 뺴주는것은 나눗샘의 숫자 k값이 커서 나눌수가 없구나