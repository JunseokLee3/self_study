## 서로서 집합을 활용한 사이클 판별 소스코드

# 특정 원소가 속한 집합을 찾기
def find_paraent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_paraent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_paraent(parent, a)
    b = find_paraent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union)의 개수 입력받기
v,e