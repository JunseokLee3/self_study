n = int(input())
t = []
p = []
dp = [0] * (n +1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(t)
    p.append(p)

# for i in range(n - 1, -1, -1)
for i in range(n -1 , -1, -1):
    time = t[i] + i  # 엄청 복잡한거인 숫자 1이 부족한데 그냥 range를 계산한거임 이거2번생각해야됨
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]

    else:
        dp[i] = max_value

print(max_value)