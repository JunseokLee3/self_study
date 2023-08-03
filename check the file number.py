import os

### 1차 코드
# def count_md_files(directory):
#     total_count = 0
#     print(f"Searching in directory: {directory}")

#     # 각 하위 디렉터리 별로 .md 파일 갯수 저장
#     subdirectory_counts = {}

#     for root, dirs, files in os.walk(directory):
#         count = 0
#         for file in files:
#             if file.endswith('.md') and file != 'README.md':
#                 count += 1

#         # 현재 디렉터리의 .md 파일 개수를 총 개수에 더하고 하위 디렉터리 개수 저장
#         total_count += count
#         if count > 0 :
#             subdirectory_counts[root] = count
    
#     print(f"ToTal (excluding README.md) : {total_count}")
#     print("Subdirectory counts : ")
#     for sub_dir, count in subdirectory_counts.items():
#         print(f"{sub_dir} : {count}")

#     return total_count

def count_md_files(directory):
    total_count = 0
    subdirectory_summary = {} # 0.1 backbone, 0.2 segmentation 등의 카운터

    print(f"Searching in directory: {directory}")

    for root, dirs, files in os.walk(directory):
        count = 0
        if "0.0 참고" in root: # "0.0 참고" 디렉터리는 건너뜁니다.
            continue

        for file in files:
            if file.endswith('.md') and file != 'README.md':
                count += 1

        # 현재 디렉터리의 .md 파일 개수를 총 개수에 더합니다.
        total_count += count

        # "0.1 Backbone", "0.2 segmentation" 등의 키에 대한 카운트를 업데이트 합니다.
        for key in ["0.1 BackBone", "0.2 segmentation", "0.3 ZSL"]:
            if key in root:
                subdirectory_summary[key] = subdirectory_summary.get(key, 0) + count

    print(f"Total paper: {total_count} \n")
    print("Subdirectory counts: ")
    for key, count in subdirectory_summary.items():
        print(f"{key}: {count}")
    return total_count


# 원하는 디렉터리 경로 지정
directory_path = './paper study'
count_md_files(directory_path)