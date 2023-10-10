graph  = [[]* 4 for _ in range(4)]

for _ in range(4):
    graph.append(list(map(int, input().split())))

data = [] # 정보 한번 정리용  data에 (a, b) 로 넣음 a 는 물고기 번호 b는 방향

for i in range(4):
    for j in range(4):
        data.append((data[i][2*j], data[i][2*j + 1]))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

data.sort() #번호별 정리


# 상어가 0,0에서 나타남 어떻게 구현 해야힞? 
#일단 먹힌다는 표현 
# 상어 위치를 따로 해야하나? 분리해야 하나
# 아니면 흠... 


