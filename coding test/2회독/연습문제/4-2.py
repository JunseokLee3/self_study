# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시간 안에 '3' dl vhgksehldj dlt
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)