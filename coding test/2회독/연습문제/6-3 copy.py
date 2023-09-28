array = [7,5 ,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 부터 0까지 감소하여 반보하는 무법
        if array[j] < array[j-1]: # 한 칸씩 이동하기
            array[j], array[j-1] = array[j-1], array[j]

        else: # ㅈ가ㅣ보다 작은 데잍를 만나면 그 위치에서 멈춤
            break

print(array)


