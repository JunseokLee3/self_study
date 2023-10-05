import copy  # 이거 나중에 dfs 호출때 배열 deepcopy를 위한거

array = [[None] * 4 for _ in range(4)] # 물고기의 번호와 방향 저장

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j * 2], data[j * 2 + 1] -1 ]  # 번호와 방향 저장 짝, 홀

# 8가지 방형
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 위체이서 왼족으로 회전
def turn_left(direction):
    return (direction + 1) % 8

result = 0

# 물고기 위치 파악 붙어 할까?
def find_fish(array, index):
    for i in range(4):
        for j in range(4): # 왜나하면 4x4 크기제한이 잇엇어 그래
            if array[i][j][0] == index:
                return (i, j)
    return None

# 물고기 먼저 이동 시킨 다고 했으니
def move_all_fish(array, now_x, now_y): # now_x, now_y 이것은 상어의 이동 방향이구나
    for i in range(1, 17): # 16번 까지 있는지 확인
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]  # position 따온거에서 방향을 가지고 옴
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turn_left(direction)
# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 변환
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)

    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1

    move_all_fish(array, now_x, now_y)

    positions = get_possible_positions(array, now_x, now_y)
    if len(positions) == 0:
        result = max(result, total)
        return
    for next_x, next_y in positions:
        dfs(array, next_x, next_y)

dfs(array, 0, 0, 0)
print(result)

