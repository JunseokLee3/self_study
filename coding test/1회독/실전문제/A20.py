from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # 복도 정보 (N x N)
teachers = []  # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        # 장애물을 설치할 수 이쓴 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))


# 특정 방향으로 감시를 진행 (할생 발견 : True, 학생 미발견 : False )
def watch(x, y, direction):
    # 왼쪽 방향을 ㅗ감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == '0': # 장애물이 있는 경우
                return False
            y -= 1


    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == "0": # 장애물이 있는 겨웅
                return False
            y += 1
    
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == "0": # 장애물이 있는 겨웅
                return False
            x -= 1
            
    
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == "0": # 장애물이 있는 겨웅
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학새잉 감지되는지 검사
def process():
    # 모든 선생님의 위치르 하나씩 확ㅇ니
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False  # 학생이 한명도 감지 되지 않도록 설치할 수 이쓴지의 여부

# 빈 공간에서 3개를 뽑느 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물 설치해보기
    for x, y  in data:
        board[x][y] = '0'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우룰 발견한 것임
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')

