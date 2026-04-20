# ======================================
#  32.1 예제 람다 표현식으로 함수 만들기
print("="*5, "32.1 예제", "="*5)

print((lambda x : x+10)(1))                      # 기본 람다 사용법

y = 10
print((lambda x: x+y)(1))                        # 입력값 1에 전역변수 y를 덧셈

print(list(map(lambda x: x+10, [1, 2, 3])))      # 리스트 요소에 10을 더한후 반환

print("="*21)
# ======================================
#  32.2 예제 람다 표현식과 map, filter, reduce 함수 활용하기
print("="*5, "32.2 예제", "="*5)

a = list(range(1, 11))
print(list(map(lambda x: str(x) if x%3==0 else float(x) if x%3==1 else x, a)))      # 리스트 요소가 3의 배수라면 문자열, 3의 배수+1이라면 실수 변환

a, b = list(range(1, 6)), list(range(2, 11, 2))
print(list(map(lambda x, y: x*y, a, b)))         # a, b 리스트에서 하나씩 가져와서 곱셈

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]            # 리스트에서 5보다 크고 10보다 작은 수 여과
print(list(filter(lambda x: x>5 and x<10, a)))

from functools import reduce
a = list(range(1, 6))
print(reduce(lambda x, y: x+y, a))               # 리스트 요소를 더하면서 누적

print("="*21)
# ======================================
#  32.3 퀴즈
print("="*5, "32.3.1 퀴즈", "="*5)
print("""다음 중 값 세 개를 매개변수로 받은 뒤 매개변수를 모두 곱해서 반환하는 람다 표현식으로 올바른 것을 고르세요. ----- 답(d)
 a. lambda a, b: a * b                           #  ==> X
 b. lambda a, b, c: return a * b * c             #  ==> X
 c. lambda a, b, c -> a * b * c                  #  ==> X
 d. lambda a, b, c: a * b * c                    #  ==> O, lambda 매개변수(쉼표로 구분) : 매개변수가 포함된 코드의 방식으로 표현 
 e. lambda(a, b, c): a * b * c                   #  ==> X""")
print("="*23)

print("="*5, "32.3.2 퀴즈", "="*5)
print("""다음 중 람다 표현식 자체를 호출하는 방법으로 올바른 것을 고르세요. ----- 답(b)
 a. lambda a: a + 1(10)                          #  ==> X
 b. (lambda a: a + 1)(10)                        #  ==> O, b 보기와 같이 람다 표현식을 소괄호에 묶고 다음 소괄호에 입력값을 넣음
 c. lambda a: a + 1: 10                          #  ==> X
 d. lambda a: a + 1, 10                          #  ==> X
 e. lambda a: a + 1 <- 10                        #  ==> X""")
print("="*23)

print("="*5, "32.3.3 퀴즈", "="*5)
print("""다음 중 리스트 a의 요소 중 7로 끝나는 숫자만 다시 리스트로 만드는 방법으로 올바른 것을 고르세요. ----- 답(c)
 a. list(lambda x: x % 10 == 7, a)               #  ==> X
 b. list(map(lambda x: x % 10 == 7, a))          #  ==> X
 c. list(filter(lambda x: x % 10 == 7, a))	     #  ==> O, filter 함수로 람다표현식 내부의 조건식이 True인 a의 요소만 리스트로 만듬
 d. list(reduce(lambda x: x % 10 == 7, a))		 #  ==> X
 e. list(filter(lambda x: x % 7 == 0, a))		 #  ==> X""")
print("="*23)

# ======================================
#  32.4 연습문제: 이미지 파일만 가져오기
print("="*5, "32.4 연습문제", "="*5)

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda file: file[file.find('.')+1:] in ['jpg', 'png'], files)))

print("="*25)
# ======================================
#  32.5 심사문제: 파일 이름을 한꺼번에 바꾸기
print("="*5, "32.5 심사문제", "="*5)

file_list = input("파일 이름을 숫자.확장자의 형식, 공백으로 구분하여 입력해주세요.").strip().split()
print(list(map(lambda file: f"{int(file[:file.find('.')]):0>3d}{file[file.find('.'):]}", file_list)))

print("="*25)
# ======================================
#  33.1 예제 변수의 사용 범위 알아보기
print("="*5, "33.1 예제", "="*5)

x = 10
def foo():
    x = 20
    print(x)		# 20
foo()
print(x)			# 10

x = 10
def foo():
    global x
    x = 20
    print(x)		# 20
print(x)			# 20

def foo():
    x = 10
    print(locals())	# 함수 내의 변수들을 딕셔너리 형태로 반환
foo()

print("="*21)
	