import copy

array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input()))
    for j in range(4):
        array[i][j] = [data[j *2], data[j *2 + 1] - 1] # 방향이라서 -1

dx = [-1 ,-1 ,0 ,1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 결과적으로 가장 큰수를 찾는거
# 그리고 완전탐색 -> dfs -> 재귀

# 조건0. 0.0에 상어 들어감
# 조건1. 물고기 이동
#

def find_fish(index):
    for i in range(4):
        for j in range(4):
            if array[i][j] == index:
                return (i,j)
    return None

def turn_left(direction):
    return (direction +1) % 8

def move_all_fishes(array, now_x, now_y): #now 시리즈는 상어 위치
    # 상어 있는 곳에는 이동 못함
    # 모든 물고기가 1번부터 차례 대로 이동
    for i in range(17):
        # 물고기 위치?
        position = find_fish(i)

        # 여기서 position 할당 안되면 오류 나구나
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1] # 물고기 있느 방향 -> 근데 나중에 왼쪽으로 45도 회전행됨
            for _ in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (now_x== nx and now_y == ny):
                        # 상어 아니야
                        array[x][y][1] = direction # 일단 방향 다시 넣기
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break # 찾으면 지금 for문 없애야 됨
                        # 스위치
                # 다 됬는데 없어
                direction = turn_left(direction)

def shark_find_postion(array, now_x, now_y):




# 조건 0
result = 0
now_x, now_y = 0, 0

def dfs(array, now_x, now_y):
    global result
    array = copy.deepcopy(array)
    result += array[now_x][now_y][0]
    array[now_x][now_y][0] = 0

    shark_direction = array[now_x][now_y][1]

    # 조건2 물고기 이동
    move_all_fishes(array, now_x, now_y)

    # 조건 3 먹을 수 있는 물고기 위치 찾기
    posotion = shark_find_postion(array, now_x, now_y)
