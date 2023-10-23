n, k = map(int,input().split())
n1, k1 = n, k
count = 0

while True:
    if n == 1:
        break
    if n % k == 0:
        n //= k         
    else:
        n -= 1
    count += 1
print(count)

result = 0
n , k = n1, k1

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1


while n > 1:
    n -= 1
    result += 1
print(result)