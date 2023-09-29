n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력 받기
for _ in range(n):
    students.append(input().split())


'''
[정렬기준]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번재 원소가 같은 경우, 세번 재 원소를 기준으로 오르차순 정렬
3) 세ㅂ, 네번 재 원소를 기ㄴ준으로 내림차순 정렬
4) cjtqjsWo rlsndmfh dhfk
'''

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력.
for student in students:
    print(student[0])