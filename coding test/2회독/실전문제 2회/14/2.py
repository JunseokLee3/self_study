n = map(int, input())
array = []
array.append(list(map(int, input().split())))
array.sort()

print(array[(n-1)//2])

