from collections import deque

 # 큐(Queue) 구현을 위해 deque 라이브러리 사용
q = deque()

q.append(5)
q.append(2)
q.append(3)
q.append(7)
q.popleft()
q.append(1)
q.append(4)
q.popleft()

print(q)
q.reverse()
print(q)