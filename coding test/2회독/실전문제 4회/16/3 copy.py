n = int(input())
t = []
p = []
dp = [0] * (n + 1)  # 다이나민 프로그래밍을 위한 1차원 DP
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(t)
    p.append(p)

for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(max_value, p[i] + dp[time])
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)