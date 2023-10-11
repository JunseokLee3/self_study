n, m, k = map(int, input().split())

array = [[0] * (n * 1) for _ in range(n+1)]
next_array = [[0] * (n * 1) for _ in range(n+1)]

ans = 0 # (모든 참가자 이동거리)
sx, sy, square_size = 0, 0, 0 # (정사각형 만드는거 초기화)

## 벽을 따로 두는게 좋나? 벽 종류는 같은거고 내구도만 있는 거잖아.
## 그냥 한곳에 뫃아 놓는게 좋을것 같다
for i in range(1, n+1):
    # 여기서 (1,1)이 좌측 상단이라고 한다
    # array[i].append([0] + list(map(int, input().split())))
    array[i] = [0] + list(map(int, input().split()))
traveler = []
for _ in range(m):
    traveler.append(list(map(int, input().split())))

exist = list(map(int, input().split()))
######################################
# 위에는 다 받은거

def move():
    global ans 
    for i in range(m):
        if traveler[i] == exist:
            continue # 러너가 이미 출구면 생략
        tx, ty = traveler[i]
        ex, ey = exist
        if tx != ex:
            nx, ny = tx, ty # 잠시 임시
            if nx < ex:
                nx +=1                
            else:
                nx -=1
                
            if not (array[nx][ny] != 0):
                ans += 1
                traveler[i] = [nx, ny]
                continue #  다음 러너
        if ty != ey:
            nx, ny = tx, ty
            if ny < ey:
                ny +=1                
            else:
                ny -=1
                
            if not (array[nx][ny] != 0):
                ans += 1
                traveler[i] = [nx, ny]
                continue #  다음 러너
        

def find_square():
    # 2이상 작은것 부터
    global sx, sy, square_size
    ex, ey = exist
    for sz in range(2, n +1 - square_size +1 ):
        for xx in range(1, sz +1): # x좌표
            for yy in range(1, sz + 1): # y좌표
                if not (xx <= ex < xx + sz  and yy <= ey < yy + sz):
                    continue
                for i in range(m):
                    is_traveler_in = False
                    if traveler[i] == exist:
                        continue # 러너가 이미 출구면 생략
                    tx, ty = traveler[i]
                    if (xx <= tx < xx + sz  and yy <= ty < yy + sz):
                        is_traveler_in = True
                    
                if is_traveler_in:
                    sx, sy = xx, yy
                    square_size = sz
                    


def rotate_square():
    for xi in range(sx, sx + square_size):
        for yi in range(sy, sy + square_size):
            # 굳이 이거 회전 해야되 참가자, 출구만 회전하면 되는거야니야?
            # 벽도 있구나
            # 우선 내부 벽 부터 감서
            if array[xi][yi] != 0:
                array[xi][yi] -= 1

    # 내구도 감소
    # 그다음에는
    for xi in range(sx, sx + square_size):
        for yi in range(sy, sy + square_size):
            ox, oy = xi -square_size, yi- square_size
            # 시계 방향 90도 회전
            rx, ry = oy, square_size -1 -ox
            # board만 하면 충돌 생기지 않을까?
            next_array[sx + rx][sy + ry] = array[xi][yi]
    # 위에거 임시 next_array 돌린거  다 넣음

    for xi in range(sx, sx + square_size):
        for yi in range(sy, sy + square_size):
            array[xi][yi] =next_array[xi][yi]

def rotate_the_person_exsit():
    global exist
    for i in range(m):
        tx, ty = traveler[i]
        if sx <= tx < sx+square_size-1 and sy <= ty < sx+square_size-1:
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다. 
            ox, oy = tx - sx, ty - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, square_size - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            traveler[i] = [rx + sx, ry + sy]
    ex, ey = exist
    if sx <= ex < sx+square_size-1 and sy <= ey < sx+square_size-1:
        # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다. 
        ox, oy = ex - sx, ey - sy
        # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
        rx, ry = oy, square_size - ox - 1
        # Step 3. 다시 (sx, sy)를 더해줍니다.
        exist = [rx + sx, ry + sy]


## K동안 진행
    ## print( 모든 참가자들의 이동 거리 합 , 출구 좌표)
    ## print( ans)
    ## print (ex, ey)
for _ in range(k):
    ## 1. 이동
    move()
    is_all_escaped = True # 다 들어가갔음
    for i in range(m):
        if traveler[i] != exist:
            is_all_escaped = False # 아직 다 들어가지않음
    if is_all_escaped:
        break
    ## 2. 이동이 끝나고 회전
    
        ## 2.1 사각형 찾기 (2 이상) ,한명이상의 참가자와 출구 포함
    find_square()
        ## 2.2 시계 방향 회전 (이때, 벽 내구도 1 감소) 그리고 출구 사람 회전
    rotate_square()
    rotate_the_person_exsit()

print(ans)    
print(exist[0], exist[1])