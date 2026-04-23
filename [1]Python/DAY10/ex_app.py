## =================================================
##      메모 관리 프로그램  - MEMO APP
## =================================================
## -> 주요기능 : 메모 저장, 삭제, 보기 
## =================================================
## -------------------------------------------------
## 모듈 로딩
## -------------------------------------------------
import os 
from datetime import datetime

## -------------------------------------------------
## 전역변수
## -------------------------------------------------
MEMO_DIR = '../Memo'
M_VIEW, M_MEMO, M_SAVE, M_DELETE, M_EXIT = list('12345')
wdate = f"{datetime.today().year:04}_{datetime.today().month:02}_{datetime.today().day:02}"


## -------------------------------------------------
## 사용자정의 함수 
## -------------------------------------------------
## 함수기능 : 메뉴 출력
## 함수이름 : print_menu
## 매개변수 : 없음
## 함수결과 : 없음
## -------------------------------------------------
def print_menu():
    print("="*30)
    print(f"{'MENU':^30}")
    print("="*30)
    print("1.전체보기")
    print("2.선택보기")
    print("3.메모저장")
    print("4.메모삭제")
    print("5.종료")
    print("="*30)


def print_stat(msg):
    print("="*30)
    print(f"{msg:^30}")
    print("="*30)

## -------------------------------------------------
## 함수기능 : 메모 목록 출력
## 함수이름 : print_meno
## 매개변수 : 없음
## 함수결과 : 없음
## -------------------------------------------------
def create_folder():
    while True:
        response = input("메모 폴더를 만드시겠습니까?(y/n) >>> ").strip()
        if len(response) == 1 and response.isalpha:
            if response.lower() == 'y': 
                os.mkdir(MEMO_DIR)
                print(f'메모 폴더가 {os.path.abspath(MEMO_DIR)}에 생성되었습니다.')
                break
            elif response.lower() == 'n':
                print('이전 화면으로 돌아갑니다.')
                break
        else:
            print(f'{response}는 유효하지 않은 입력입니다.')
            continue


def print_memo():
    mlist = os.listdir(MEMO_DIR)
    print("="*30)
    print(f"{'-메모목록-':^30}")
    print("="*30)
    for m in mlist:
        print(m)
    print("="*30)


def view_memo():
    ## 메모 선택
    global filepath
    item = input("메모 날짜입력(예:2025_02_11):")
    item = f'memo_{item}.txt'
    filepath=f'{MEMO_DIR}/{item}'
    ## 선택된 메모 내용 화면에 출력
    mitems = os.listdir(MEMO_DIR)
    if item in mitems:
        with open(filepath, mode='r', encoding='utf8') as F:
            print("="*30)
            print(F.read())
            print("="*30)
    else:
        print(f'{item} : 존재하지 않는 메모입니다. ')


def delete_memo():
    global filepath
    view_memo()
    while True:
        response = input('삭제하시겠습니까?(y/n) >>> ').strip()
        if len(response) == 1 and response.isalpha:
            if response.lower() == 'y': 
                os.remove(filepath)
                print('메모가 삭제되었습니다.')
                break
            elif response.lower() == 'n':
                print('이전 화면으로 돌아갑니다.')
                break
        else:
            print(f'{response}는 유효하지 않은 입력입니다.')
            continue


## -------------------------------------------------
## 함수기능 : 메모 저장 
## 함수이름 : save_meno
## 매개변수 : 없음
## 함수결과 : 없음
## -------------------------------------------------

def save_memo():
    memo = input("메모할 내용 : \n")
    save_path = f"{MEMO_DIR}/{f'memo_{wdate}.txt'}"
    
    if not os.path.exists(save_path):
        cnt = 0
    else:
        with open(save_path, mode='r', encoding='utf-8') as Fr:
            for line in Fr.readlines():
                if line.find('\nMemo ') >= 0:
                    cnt = int(line[line.find('\nMemo ')+1:line.find('\nMemo ')+2])
            
    wCnt = 0
    with open(save_path, mode='a', encoding='utf-8') as F:
        wCnt = F.write(f'\nMemo {cnt+1:0<2}.\n')
        wCnt = F.write(memo+'\n')

    msg = "파일이 존재하지 않거나 저장 실패" if not os.path.exists(save_path) else f'{wCnt}개 데이터 저장 완료'
    print(msg) 


## =================================================
## 프로그램 구동
## =================================================
if __name__ == '__main__':
    print_stat('MEMO APP START')

    while True:
        print_menu()
        choice = input("메뉴 선택(1~5):").strip()

        if choice not in [M_VIEW, M_MEMO, M_SAVE, M_DELETE, M_EXIT]:
            print(f"{choice}는 유효하지 않은 메뉴입니다.")
        else:
            if not os.path.exists(MEMO_DIR):
                print("메모 폴더가 삭제되었거나 생성되지 않았습니다.")
                create_folder()
            else: 
                if choice == M_VIEW:
                    print_memo()
                elif choice == M_MEMO:
                    view_memo()
                elif choice == M_SAVE:
                    save_memo()
                elif choice == M_DELETE:
                    delete_memo()
                else:
                    print("사용자 요청으로 종료합니다.")
                    break

    print_stat('MEMO APP END')
