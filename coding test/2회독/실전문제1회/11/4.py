n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 바복 종료
    if target < x:
        print('target', target, end= ' ')
        print('x', x)
        break
    target += x

# 만들 수 없는 금액 출력
print(target)