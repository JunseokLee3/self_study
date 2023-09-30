n = int(input())
array = list(map(int, input().split()))

count = 0
# 이진 탐색(Binary Search) 수행
for i in range(n):
    if array[i] == i:
        print(i)
        count += 1
        print('count : ', count)

if count == 0:
    print('-1')