n = int(input())
data = list(map(int, input().split()))

# 중간값 (median)을 출력
print(data[(n-1)// 2])