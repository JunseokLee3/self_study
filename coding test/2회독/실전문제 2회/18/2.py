# 서로서로 해결 해야한다. 
# d왜냐하면 각 000 dptj 0이 속하
# 근데 이미 차있으면 이전에서 나와야 한다.

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = map(int, input())
p = map(int, input())

parent= [0] * (g + 1)

for i in range(1, g+1):
    parent[i] = i

result = 0

for _ in range(p):
    data = find_parent(parent, int(input()))
    if data ==0:
        break
    union_parent(parent, data, data-1)
    result += 1

print(result)