# 소수 판별 함수
def is_prime_number(x):
    # 2부터 (x -1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소스가 아님
    return True

print(is_prime_number)
print(is_prime_number)

import math

# 소스판별 함수
def in_prime_number(x):
    # 2부터 xdml 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x 가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(67))