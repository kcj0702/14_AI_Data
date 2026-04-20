## =====================================================================
##                              복습  &  테스트
##                                                          2026-04-20
## ===================================================================== 
## [문제] 4칙 연산 계산기를 구현하세요.
## -> 기능 : 숫자 덧셈, 뺄셈, 곱셈, 나눗셈
## -> 조건 
##   ① 기능은 함수화
##   ② 2개 숫자 입력 받기 => 2개 또는 1개만 입력, 2개 입력 시에 모두 숫자 문자 체크, isdecimal, isnumeric, isdigit는 실수체크는 불가능('.')
##   ③ 연산자 입력 받기   => +, -, *, /
##   ④ x, X 입력 시 종료 => 1개만 입력 시 'x', 'X' 문자 체크
##   ※ 각각의 기능을 함수로 정의(숫자 체크(정수, 실수, 음수), 입력값 체크(입력값의 갯수), 숫자 변환)
## ===================================================================== 
# def cal():
#     while input("계산기를 종료하시려면 'x'나 'X'를 입력해주세요. >>>").strip() != 'x':
#         a, b, result = 0, 0, 0
#         a, b = input("계산할 숫자 2개를 입력해주세요. ex)(10 20) >>>").strip().split()
#         if a.isdecimal() and b.isdecimal():
#             a = float(a)
#             b = float(b)
#             opr = input("연산자를 입력해주세요. ex)(+) >>>")
#             if opr == '+': result = a + b 
#             elif opr == '-': result = a - b
#             elif opr == '*': result = a * b
#             elif opr == '/':
#                 result = a / b if b != 0 else print("나눌 숫자는 0이 아닌 숫자를 입력해주세요.")
#             else:
#                 print("사칙 연산기호 중 하나를 다시 입력해주세요.")
#                 continue
#             print(f"{a} {opr} {b} = {result}")
#         else:
#             print("숫자로 다시 입력해주세요.")

# cal()

# ====================================================================== 
# 정의할 함수 : 사칙 연산
#           : 입력 데이터 정수/실수/음수 판별, 변환
# ====================================================================== 
def operate(num1, num2):
    global opr 
    opr = input("+ - * /의 연산 기호 중 하나를 입력해주세요. >>> ").strip()
    if opr == '+': return num1 + num2
    elif opr == '-': return num1 - num2
    elif opr == '*': return num1 * num2
    elif opr == '/': return num1 / num2 if num2 != 0 else print("0으로 나눌 수는 없습니다. 다시 입력해주세요.")
    else: 
        print("유효하지 않은 연산 기호입니다. (+ - * / 중 1택)")
        return None
    
def str_to_num(num:str):
    isnegative = False
    isfloat = False
    idx = 0
    if num.find('-')>=0:
        num = num.replace('-', '')
        isnegative = True
    if num.find('.')>=0:
        idx = num.index('.')
        num = num.replace('.', '')
        isfloat = True
    if num.isdecimal():
        if isfloat:
            num = float(num[:idx] + '.' + num[idx:])
        else:
            num = int(num)
        if isnegative:
            num = -num
    else:
        print('숫자를 다시 입력해주세요.')
        return None
    return num

# ====================================================================== 
# 실행 코드
# ====================================================================== 
while input("계산기를 종료하시려면 'x'나 'X'를 입력해주세요. >>> ").strip() != 'x':
    num_list = input("계산할 숫자 2개를 입력해주세요. ex)(10 20) >>> ").strip().split() 
    if len(num_list) == 2:
        for i, num in enumerate(num_list):
            if not str_to_num(num) == None:
                num_list[i] = str_to_num(num)
            else:
                continue
    else:
        print("다시 입력해주세요.")
        continue
    
    result = operate(num_list[0], num_list[1])
    if  result != None:
        print(f"{num_list[0]} {opr} {num_list[1]} = {result:.3f}")
    else:
        continue