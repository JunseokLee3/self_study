import os

# def draw_tree(path, indent=""):
#     print(indent + os.path.basename(path))
#     if os.path.isdir(path):
#         for child in os.listdir(path):
#             child_path = os.path.join(path, child)
#             draw_tree(child_path, indent + "  ")

"""
def draw_tree(path, indent=""):
    base_name = os.path.basename(path)
    if base_name.startswith('.'):  # 숨김 파일 및 디렉토리 건너뛰기
        return
    print(indent + base_name)
    if os.path.isdir(path):
        for child in os.listdir(path):
            child_path = os.path.join(path, child)
            draw_tree(child_path, indent + "  ")
"""

# def draw_tree(path, prefix=''):
#     # 숨김 파일/디렉토리 건너뛰기
#     base_name = os.path.basename(path)
#     if base_name.startswith('.'):
#         return
    
#     # 파일/디렉토리 리스트 구하기
#     entries = os.listdir(path)
#     entries = [e for e in entries if not e.startswith('.')]
#     entries.sort()
    
#     for i, entry in enumerate(entries):
#         # 경로 합치기
#         entry_path = os.path.join(path, entry)
        
#         # 현재 entry가 마지막인지 확인
#         is_last = i == len(entries) - 1
        
#         # 출력을 위한 접두사 설정
#         if is_last:
#             print(prefix + '└── ' + entry)
#             new_prefix = prefix + '    '
#         else:
#             print(prefix + '├── ' + entry)
#             new_prefix = prefix + '│   '
        
#         # 디렉토리인 경우 재귀적으로 그리기
#         if os.path.isdir(entry_path):
#             draw_tree(entry_path, new_prefix)
   


def draw_tree(path, prefix=''):
    # 숨김 파일/디렉토리 건너뛰기
    base_name = os.path.basename(path)
    if base_name.startswith('.'):
        return

    # 디렉토리 리스트 구하기
    entries = os.listdir(path)
    entries = [e for e in entries if not e.startswith('.')]
    entries = [e for e in entries if os.path.isdir(os.path.join(path, e))]
    entries.sort()
    
    for i, entry in enumerate(entries):
        # 경로 합치기
        entry_path = os.path.join(path, entry)
        
        # 현재 entry가 마지막인지 확인
        is_last = i == len(entries) - 1
        
        # 출력을 위한 접두사 설정
        if is_last:
            print(prefix + '└── ' + entry)
            new_prefix = prefix + '    '
        else:
            print(prefix + '├── ' + entry)
            new_prefix = prefix + '│   '
        
        # 디렉토리인 경우 재귀적으로 그리기
        if os.path.isdir(entry_path):
            draw_tree(entry_path, new_prefix)


# 사용법:
draw_tree("./")
