##### 조건 1
# 4x4
# 1x1 크기 정 사각형
# 각 공낙ㄴ의 각 칸은 (x, y)

# 물고기 번호 1<= n <= 16
# 방향 (상하좌우, 대각선)

##### 시작
## 청소년 상어 처음 시작 (0,0)
## (0,0)에 있었던 물고기 먹고, 물고기 방향과 일치 
## 이후 물고기가 이동한다.
# 방향 direction 이라고 하자

##### 조건2
## 번호가 작은 물고기부터 순서대로 이동
# for i in range(1, 17): 이렇게 시작하면 되지 않을까?
## 여기서 조건 물고기는 한칸 이동
## 이동 할 수 있는 칸은 @ 빈칸 그리고 다른 물고기가 있는 칸 @ -> 이거 조건문 해서 이동하면 되겠네
## 이동할수 있는 칸을 향할 때까지 방향을 45도 반시계 방향 -> 그럼 방향의 설정을 45도 변화하는 것 부터
## 이동할수 없는 칸 @상어가 and 공간의 경계@

dx = [-1, -1, 0, 1, 1, 1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
# 일단 45도로 회전하는 방향 

## 만약 이동할 수 있는 칸이 없으면 이동을 하지 않지만, 그외의 경우 이동


##### 조건 3
## 물고기의 이동이 모두 끝나면(조건2) 
## 상어가 이동
# 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기 먹음
# 그 물고기의 방향을 가짐
# 이동한느 중에 지나가는 칸에 있는 물고기느 ㄴ먹지 않음
# 상어가 이동할 수 있는 칸이 없으면 긑
## 상어 이동후 다시 물고기 이동

### 출력
# 번호의 합의 최댓값을 구하시오 (여기서 번호의 합은 최댓값에서 DFS 확인)


########################시작
# 먼저 4 x 4 만들기
graph = [[0]* (4) for _ in range(4)]  # 우선 0으로

# 물고기 정보 받기
## a 물고기 번호, b 방향
# 자 잠깐 array에 저장하자
array =[]
for _ in range(4): # 이제 받아야 하는데 데이터를 2개 묶음으로 한 물고기 정보임
    array.append(list(map(int, input().split())))

# 4 행의 8개의[a,b a,b a,b a,b] 로 저장됨 
# 어떻게 활용하지?
# 1안 위치 행렬, 물고기 행렬 각가 이용? 
# 굳이? 하나 묶어서 사용하면 코드 이용하기 편하지 않니?

for i in range(4):
    for j in range(4):
        array[i][j] = [array[i][2*j], array[i][2*j + 1] -1] # -1 해줘야지 dx을 할수 있음

total = 0
# 상어 시작
x, y = 0, 0
total += array[x][y][0]
array[x][y][0] = [0]
shark_direction = 0
shark_direction = array[x][y][1]

def find_fish(array, i):
    for x in range(4):
        for y in range(4):
            if array[x][y] == i:
                return x, y, array[x][y][1]

## 물고기 이동
for i in range(1, 16):
    fish_i, fish_j, fish_direction = find_fish(array, i)
    # 물고기 찾기
    for _ in range(8): # 8번시도 i안쓰는것은 이동 방향이 정해짐 왼쪽 45
        nx = fish_i + dx[fish_direction]
        ny = fish_j + dy[fish_direction]
        if 0 <= nx and 4 > nx and ny >= 0 and ny < 4: # 경계선 안에서 노는거
            # 조건 2에서 @ 빈칸 그리고 다른 물고기가 있는 칸 @ 
            # 이동할수 없는 칸 @상어가 and 공간의 경계@
            if array[nx][ny] != 0 and array[nx][ny] > 0:
                array[nx][ny], array[fish_i][fish_j] = array[fish_i][fish_j] , array[nx][ny]
                
