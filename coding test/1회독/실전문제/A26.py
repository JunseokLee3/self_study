import heapq

n = int(input())

# 힙(heap)에 초기 카드 묶음을 모두 삽입
heap =  []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힘(Heap)에 원소가 1개 남을 때까지
while len(heap) !=  1:
    # 가장 적은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)