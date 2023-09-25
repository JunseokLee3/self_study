# 이진 탐색 소스코드 구현(재귀 함수)
def binary_serach(array, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    # 고정점을 찾는 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_serach(array, start, mid - 1)
    # 중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른족 확인
    else:
        return binary_serach(array, mid + 1 , end)
    
n = int(input())
array = list(map(int, input().split()))

# 이진 탐색(Binary Search ) 수행
index = binary_seach( array, 0, n - 1)

# 고정점이 없는 경우 -1 출력
if index == None:
    print(-1)
# 고정점이 잇는 경우 해당 인덱스 출력
else:
    pritn(index)