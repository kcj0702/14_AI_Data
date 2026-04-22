# ================================================
# 문제 1. 메모 저장 기능 만들기
# ------------------------------------------------
# 구현 : 간단한 메모 프로그램의 저장 기능. 
#
# 요구사항
# -> 사용자에게 메모 내용을 입력받기.
# -> 날짜별 폴더 생성 및 해당 날짜 폴더에 파일 저장.
#    폴더 생성 함수는 import os 
#                   os.mkdir("폴더명")
# -> 입력받은 내용을 memo_YYYY_MM_DD.txt 파일에 저장.
# -> 저장이 끝나면 "메모가 저장되었습니다."를 출력.
#
# 저장 형식
# -> 날짜
# -> 메모 내용
# -> 기존 내용은 유지하고 새 내용은 뒤에 추가
# ================================================
import os
from datetime import datetime
cnt = 0
def memo():
    global cnt
    memo = input("메모할 내용을 적어주세요. >>> ").strip()
    folder_path = f'{datetime.today().year:04}_{datetime.today().month:02}_{datetime.today().day:02}'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    with open(folder_path+f"/{'memo_'+folder_path.lstrip('../')}", 'a', encoding='utf-8') as f:
        if cnt == 0:
            f.write(f"{datetime.today().year}년 {datetime.today().month}월 {datetime.today().day}일\n\n")
        else:
            f.seek(2)
        f.write(f"메모 {cnt+1}\n")
        f.write(memo+'\n\n')
    cnt +=1
# memo()
# memo()

# ================================================
# 교수님 풀이
# ================================================
# 1. 폴더 존재 여부 체크
#   -> 없으면 생성 os.mkdir("Memo")
# 2. 내용 입력
#   -> input()
#   -> 입력 받을 내용 : 날짜, 메모내용
# 3. 메모 저장
#   -> memo_YYYY_MM_DD.txt 파일에 저장
#   -> 저장 완료 후 "메모가 저장되었습니다."를 출력
# 4. 함수 구현
#   -> 범위 : 입력 따로, 저장 따로
#            메모 저장 기능 함수로
#   -> 함수 기능: 메모내용 저장
#                Memo 폴더 아래에 memo_YYYY_MM_DD.txt로 저장
#   -> 매개 변수: 날짜, 내용
#   -> 함수 결과: 저장 여부 메시지 출력
# ================================================
# MEMO_PATH = '../Memo'
# def save_memo(wdate, memo):
#     # (1) Memo 폴더 존재 여부
#     if not os.path.exists(MEMO_PATH): os.mkdir(MEMO_PATH)
#     else: print(f"{MEMO_PATH} 존재합니다.")
#     # (2) 파일에 기록 : open -> write -> close  ==> with ~ as 구문으로 간소화
#     file_path = f"{MEMO_PATH}/{f'memo_{wdate}.txt'}"
#     wCnt = 0
#     with open(file_path, mode='a', encoding='utf-8') as F:
#         wCnt = F.write('\n[Memo-1]\n')
#         wCnt = F.write(memo+'\n')
#     # (3) 저장 여부 출력
#     msg = "파일이 존재하지 않거나 저장 실패" if not os.path.exists(file_path) else f'{wCnt}개 데이터 저장 완료'
#     print(msg)

# 입력 받은 메모 저장
# 입력 받기 => 날짜, 메모내용
# IPdata = input("날짜와 메모내용 입력(예: 2026_03_01 내용입니다): ").strip().split()

# 입력 데이터 검사 => 최소 2개 존재
# if len(IPdata) >= 2:
#     pass
#     # 0번째 원소는 날짜
#     if IPdata[0].replace("_",'').isdecimal():
#         # 1번째 원소부터는 메모 내용
#         Memo = ' '.join(IPdata[1:])
#         save_memo(IPdata[0], Memo)
#     else:
#         print("YYYY_MM_DD 형식의 날짜가 아닙니다.")
# else:
#     print("날짜와 메모내용 중 누락된 부분이 있습니다.")

# ================================================
# 문제 2. 회원 추가 기능 만들기
# ------------------------------------------------
# 구현 : 회원 관리 프로그램의 회원 등록 기능.
#
# 요구사항
# -> 사용자에게 연락처, 이름(지역, 직업, 취미) 입력받기.
# -> 입력받은 정보를 users.txt 파일에 추가 저장.
# -> 이미 저장된 회원 정보는 유지되어야 함.
# -> 저장 후 "회원 등록 완료" 출력.
# -> 이미 존재하는 회원이면 "이미 등록되어 있습니다" 출력.
# 
# 저장 형식
# 연락처             이름        지역        직업        취미
# 010-1111-1111     마징가      대구        운동선수     태권도
# ================================================
def register():
    isregister = False
    profile = input("회원정보를 연락처 이름 (지역 직업 취미) 순으로 입력해주세요. >>> ").strip().split()
    if os.path.exists('user.txt'):
        with open('user.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
            for user in data:
                if user.find(profile[1]):           # 이름으로 했지만 연락처로 하는게 확실(동명이인 존재)
                    print('이미 등록되어 있습니다.')
                    isregister = True
                    break
    if isregister == False:
        with open('user.txt', 'w', encoding='utf-8') as f:
            a = ['연락처', '이름', '지역', '직업', '취미']
            f.write(f"{a[0]}{' '*13}{'        '.join(a[1:])}\n")
            f.write(f"{profile[0]}{' '*4}")
            for i in profile[1:]:
                f.write(f'{i:<10}')
            print('회원 등록 완료')
    
register()
register()

# ================================================
# 교수님 풀이
# ================================================
member_path = '../Member'
user_path = f"{member_path}/user_path.txt"
def create_file_path(path, isfile=False):
    # 존재 여부 체크
    if not os.path.exists(path):
    # 폴더 생성
        if not isfile:
            os.mkdir(path)
        # 파일 생성
        else:
            with open(user_path, 'x', encoding='utf-8') as F:
                F.write(f"{'연락처':<15}{'이름':<10}{'지역':<10}{'직업':<10}{'취미':<10}")
        return os.path.exists(path)
    else:
        return True


def join_user(phone, name, loc, job, hobby):
    if phone.replace('-', '').isdecimal():
        with open(user_path, 'r', encoding='utf-8') as rF:
            alldatas = rF.read()
        if phone in alldatas:
            print(f"{phone} 이미 등록된 회원입니다.")
            with open(user_path, 'w', encoding='utf-8') as F:
                wCnt = F.write(f"{phone:<15}{name:<10}{loc:<10}{job:<10}{hobby:<10}\n")
                print(f"{wCnt}개 데이터 저장")

    else:
        print('유효한 데이터가 아닙니다.')

if create_file_path(member_path) and create_file_path(user_path, True):
    print('폴더 및 파일 준비 완료')
    
    IPdata = input('회원등록 연락처, 이름, 지역, 직업, 취미 입력 : ').strip().split(',')

    if len(IPdata) == 5:
        join_user(*IPdata)
    else:
        print('필수 회원 정보 연락처, 이름, 지역, 취미가 \n모두 입력되었는지 확인바랍니다.')
else:
    print('폴더 및 파일 문제 체크 필요')