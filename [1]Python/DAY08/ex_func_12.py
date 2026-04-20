# ===========================================================================
# 변수 - 지역(Local)변수와 전역(Global) 변수
# ===========================================================================
# -> 지역(Local) 변수 : 함수의 매개변수, 함수 내부에 선언된 변수
#                      함수가 호출될 때 메모리에 존재
#                      함수 종료될 때 메모리에서 삭제
#                      함수에서만 사용가능
# 
# -> 전역(Global) 변수 : 파이썬 파일 안에 생성된 함수
#                       파이썬 파일 실행 시에 메모리에 생성
#                       파이썬 파일 종료 시에 메모리에 생성
#                       파이썬 파일 안에서 모두 사용 가능
# ===========================================================================
# ---------------------------------------------------------------------------
# [예시] 지역변수에서 전역변수 사용하기
# ---------------------------------------------------------------------------
year = 2026         # 전역변수

# 사용자 정의 함수
# => 함수기능 : 금일 날짜 출력하기
def print_today(month, day):
    # year : 매개변수 X, 함수 내 코드에서 X ==> 함수 밖 파일(py)의 전역변수 사용
    #        전역변수 값 변경
    global year         # year는 전역변수
    year = 2000         # 전역변수 year 값 변경
    print(f"오늘은 {year}년 {month}월 {day}일 입니다.")

# 실행코드
print(f"전역변수 year : {year}")

print_today(4, 20)

print(f"전역변수 year : {year}")


# Global Variable
num = 100

# Custom Function
def test(a, b):             # local variable : a, b
    print(a, b, num)        # use global variable
    
def change(a, b):           # local variable : a, b
    global num              # use & change global variable
    num *= 2                # change global variable
    print(a, b, num)        # use global variable
    
# Run code
print("Before num :", num)
test(10, 5)
print("After num :", num)

print("-"*20)

print("Before num :", num)
change(10, 5)
print("After num :", num)
