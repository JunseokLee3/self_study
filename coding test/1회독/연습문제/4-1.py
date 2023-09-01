# N 입력 받기
n = int(input())
x, y = 1, 1  # 아 여기가 시작점 (1,1) 이다.
plans = input().split() # R R 또는 L 또는 U 갈지 입력 하는 곳

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans: # 입력 받은 : # R R 또는 L 또는 U 갈지 입력 하는 곳
    # 이동 후 좌표 구하기
    for i in range(len(move_types)): # move_types = ['L', 'R', 'U', 'D']에서 len 은 4이고 range4 이면 0, 1,2,3
        if plan == move_types[i]: # 오 if로 L , R, U, D를 맞추고 시작하는 구ㅏ
            nx = x + dx[i]
            ny = y + dy[i]
            # (x, y)가 (1,1) 이고 그것을 더하는것을 plans 리스트로 했고 if로 맞추고 dx, dy로 그것을 뽑았구나
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)


# 와우 이런 방법이 있었군