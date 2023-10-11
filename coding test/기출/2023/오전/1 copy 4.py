from collections import deque

n,m, k =  map(int, input().split())

# 포탑의 파워어느 정도 남았는지
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 언제 각성 했는지
rec = [
    [0] * m
    for _ in range(n)
]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]


allign_port = [] # port 포탑

# 이거 나중에 정렬 필요로 하는거
class Turrent:
    def __init__(self, x, y, r, p):
        self.x = x
        self.y = y
        self.r = r
        self.p = p


def awake():
    weak_board= allign_port[0]
    weak_board.sort(key= lambda x: (x.p, -x.r, ))


for _ in range(k):
    # 파워정도 찾아서 줄 세우기
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0: # 포탑이 아닌것은?
                allign_port.append(Turrent(i,j, rec[i][j], board[i][j]))
    # 각성
    awake()


## 출력
# print(남아있는 제일 강한 포탑)