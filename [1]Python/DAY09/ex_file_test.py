# ===========================================
# 파일 복사 기능 구현
# - 파일명 : member.txt
# - 구  현 
#   (1) member.txt 파일 생성
#         이름    성별    지역
#       -----------------------
#        홍길동   남자    부산
#        마징가   여자    대구
#        베트맨   남자    서울
# ===========================================
file_path = './member.txt'
profile = [
    {'이름' : '이수홍', '성별' : '남자', '지역' : '부산'},
    {'이름' : '오재윤', '성별' : '여자', '지역' : '대구'},
    {'이름' : '이영희', '성별' : '남자', '지역' : '서울'}
]

with open(file_path, mode='wt', encoding='utf-8') as f:
    f.write(f"이름        성별        지역\n")
    f.write(f"--------------------------\n")
    for i in profile:
        f.write("       ".join(i.values()))
        f.write("\n")


# ===========================================
#   (2) 복사 기능
#       member_copy.txt
# ===========================================
import os
if os.path.exists(file_path):
    with open(file_path, mode='rt', encoding='utf-8') as f:
        all_data = f.read()

    file_path = file_path[:-4] + "_copy" + file_path[-4:]
    with open(file_path, mode='wt', encoding='utf-8') as f:
        f.write(all_data)
