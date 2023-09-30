n = int(input())
dp = [] 


for _ in range(n):
    dp.append(map(int, input().split()))

for i in range(1, n):
    for j in range(i +1):
        if j ==0:
            up_left = 0
        else:
            up_left = dp[i -1][j -1]
        if j == i:
            up = 0
        else:
            up = up[i-1][j]

        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n -1]))