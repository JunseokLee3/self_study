import copy

array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j*2], data[j*2 +1]-1]  # 방향이라서 -1 함

dx = [-1, -1 ,0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def turn_left(direction):
    return (direction + 1 ) % 8

result = 0

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

def move_all_fishes(array, now_x, now_y):
    for i in range(17):
        position = find_fish(array, i)
        if position != None:
            x, y= position[0], position[1]
            direction = array[x][y][1]
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < 4 and 0 <= nx < 4:
                    if not (nx == now_x and ny == now_y):  # 상어 있는 곳은 못감
                        array[x][y][1] = direction # 바뀐 방형으로 재설정
                        array[x][y], array[nx][ny] = array[nx][ny] , array[x][y]
                        break  # 찾으면 해제 -> 다른 물고기 확인
                direction  = turn_left(direction)

def get_possible_positions(array, now_x, now_y): # 상어가 물고기 먹는 위치 찾기
    positions = []
    direction = array[now_x][now_y][1] # 물고기의 방향에서 시작함
    for i in range(4):
        now_x = dx[direction]
        now_y = dy[direction]
        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

# 모든 경우를 탐색하기 위한DFS함수
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)

    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1

    move_all_fishes(array, now_x, now_y)

    positions = get_possible_positions(array, now_x, now_y)
    
    if len(positions) == 0:
        result = max(result, total)
        return
    
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

dfs(array, 0, 0, 0)
print(result)
                        

