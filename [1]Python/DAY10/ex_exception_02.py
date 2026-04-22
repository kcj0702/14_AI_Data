## =============================================
##          예외처리 (Exception Handling)
## 
## -> 문법 오류가 아닌 실행 시 발생되는 오류 처리
## =============================================
## [예시] 파일이 존재하지 않는 오류
##       FileNotFoundError: [Errno 2] No such file or directory
## =============================================
FILENAME = './infor.data'

## -----------------------
## => 오류 처리 X 
## -----------------------
# with open(FILENAME, mode='r', encoding='utf8') as F:
#     print(F.read())


## -----------------------
## => 오류 처리 O 
## -----------------------
try:
    with open(FILENAME, mode='r', encoding='utf8') as F:
        print(F.read())
except:
    print("파일 처리 시 문제가 발생했습니다.")

## -----------------------
## => 오류 처리 O 
## -----------------------
# FILENAME = './ex_package_01.py'
# F = None
# try:
#     F = open(FILENAME, mode='r', encoding='utf8')
# except:
#     print("파일 처리 시 문제가 발생했습니다.")
# else:
#     print(F.read())
# finally:
#     print("언제나 실행됨")
#     F.close()

## -----------------------
## => 오류 처리 O 
##    여러 개 ERROR 발생 시
##    특정 ERROR만 처리하는 코드에서
##    나머지 ERROR 대응 못함
## -----------------------
# try:
#     # with open(FILENAME, mode='r', encoding='utf8') as F:
#     #     print(F.read())
#     print(3/0)
# except FileNotFoundError as e:
#     print(f"{e} : 파일 처리 시 문제가 발생했습니다.")


## -----------------------
## => 오류 처리 O 
## -----------------------
try:
    a = []
    a.append(a[0])
    print(3/0)
    with open(FILENAME, mode='r', encoding='utf8') as F:
        print(F.read())
except ZeroDivisionError as e:
    print(f"ZeroDivisionError {e} : 파일 처리 시 문제가 발생했습니다.")
except FileNotFoundError as e:
    print(f"FileNotFoundError {e} : 파일 처리 시 문제가 발생했습니다.")
except Exception as e:
    print(f"Exception {e} : 파일 처리 시 문제가 발생했습니다.")

print("------ TEST END ------")