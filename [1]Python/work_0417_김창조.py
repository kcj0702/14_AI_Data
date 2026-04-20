# ======================================
#  29.6 퀴즈
print("="*5, "29.6.1 퀴즈", "="*5)
print("""다음 중 매개변수가 없는 hello 함수를 호출하는 방법으로 올바른 것을 고르세요. ----- 답(c)
 a. def hello       #  ==> X
 b. hello           #  ==> X
 c. hello()         #  ==> O, 함수이기 때문에 함수명()로 호출하며 매개변수가 없으므로 소괄호내에 인수가 없음
 d. hello[]         #  ==> X
 e. def hello:      #  ==> X""")
print("="*23)

#  29.6 퀴즈
print("="*5, "29.6.2 퀴즈", "="*5)
print("""두 수를 받은 뒤 곱한 결과를 반환하는 함수를 만들려고 합니다. 올바른 코드를 고르세요. ----- 답(d)
 a. def mul():          #  ==> X, 함수에 두 수를 받을 매개변수 없음
        a * b
 b. def mul(a, b):      #  ==> X, 결과값을 반환하지 않는 함수
        a * b
 c. mul(a, b):          #  ==> X, 함수 정의 문법이 잘못됨, def 명령어가 빠짐
        return a * b
 d. def mul(a, b):      #  ==> O
        return a * b
 e. mul(a, b):          #  ==> X, c와 같음
        return a * b""")
print("="*23)

#  29.6 퀴즈
print("="*5, "29.6.3 퀴즈", "="*5)
print("""다음 중 값을 세 개 반환하는 함수를 만들려고 합니다. 올바른 코드를 모두 고르세요. ----- 답(a, c, d)
 a. def three():                #  ==> O, 튜플 (1, 2, 3)을 반환
        return 1, 2, 3
 b. def three():                #  ==> X, 1만 반환하고, 2, 3은 반환하지 않음
        return 1
        return 2
        return 3
 c. def three():                #  ==> O, 튜플 (1, 2, 3)을 반환
        return (1, 2, 3)
 d. def three():                #  ==> O, 리스트 [1, 2, 3]을 반환
        return [1, 2, 3]
 e. def three():                #  ==> X, 오류 발생
        return 1, return 2, return 3""")
print("="*23)


# ======================================
#  29.7 연습문제: 몫과 나머지를 구하는 함수 만들기
print("="*5, "29.7 연습문제", "="*5)

x = 10
y = 3
def get_quotient_remainder(x, y):
    quotient = x // y if not y==0 else 0
    remainder = x % y if not y==0 else 0
    return quotient, remainder

quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지 : {1}'.format(quotient, remainder))

print("="*25)
# ======================================
#  29.8 심사문제: 사칙 연산 함수 만들기
print("="*5, "29.8 심사문제", "="*5)

x, y = map(int, input().split())
def calc(x, y):
    a = x + y
    s = x - y
    m = x * y
    d = x / y if not y==0 else 0
    return a, s, m, d
a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3:.1f}'.format(a, s, m, d))

print("="*25)
# ======================================
#  30.2 예제 키워드 인수 사용하기 
print("="*5, "30.2 예제", "="*5)

def personal_info(name, age, address):
    print('이름: ',name)
    print('나이: ',age)
    print('주소: ',address)

personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
personal_info(name='홍길동', address='서울시 용산구 이촌동', age=30,)

print("="*21)
# ======================================
#  30.3 예제 키워드 인수와 딕셔너리 언패킹 사용하기
print("="*5, "30.3 예제", "="*5)

def personal_info(name, age, address):
    print('이름: ',name)
    print('나이: ',age)
    print('주소: ',address)
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)      # 함수의 매개변수 이름과 딕셔너리의 키 이름이 같아야 함
                        # 애스타리스크를 한번만 쓰면 키만 언패킹
print("="*21)
# ======================================
#  30.4 예제 매개변수에 초깃값 지정하기
print("="*5, "30.4 예제", "="*5)

def personal_info(name, age, address="비공개"):
    print('이름: ',name)
    print('나이: ',age)
    print('주소: ',address)

personal_info('홍길동', 30)

print("="*21)
# ======================================
#  30.5 퀴즈
print("="*5, "30.5.1 퀴즈", "="*5)
print("""함수를 def print_numbers(a, b, c): 처럼 만들었을 때 이 함수를 호출하는 방법으로 잘못된 것을 고르세요. ----- 답(d)
 a. print_numbers(1, 3, 5)              #  ==> O
 b. print_numbers(a=1, b=2, c=3)        #  ==> O
 c. a = [5, 0, 2]                       #  ==> O
    print_numbers(*a)
 d. a = [3, 7, 9]                       #  ==> X, a가 리스트이므로 애스터리스크를 한 번만 써야함
    print_numbers(**a)
 e. print_numbers(*[9, 1, 2])           #  ==> O""")
print("="*23)
# ======================================
#  30.5 퀴즈
print("="*5, "30.5.2 퀴즈", "="*5)
print("""다음 중 print_numbers(*[10, 20, 30])으로 호출할 수 있는 함수롤 올바른 것을 모두 고르세요. ----- 답(b, c)
 a. def print_numbers(args)             #  ==> X
 b. def print_numbers(a, b, c)          #  ==> O
 c. def print_numbers(*args)            #  ==> O
 d. def print_numbers(**kwargs)         #  ==> X
 e. def print_numbers()                 #  ==> X""")
print("="*23)
# ======================================
#  30.5 퀴즈
print("="*5, "30.5.3 퀴즈", "="*5)
print("""다음 중 personal_info(**{'name': '홍길동', 'age': 30})으로 호출할 수 있는 함수로 올바른 것을 모두 고르세요. ----- 답(a, c)
 a. def personal_info(**kwargs):                #  ==> O, 키워드 인수로 딕셔너리를 언패킹해서 딕셔너리의 키와 값를 가져올 수 있음
 b. def personal_info(*args):                   #  ==> X, 매개변수가 가변 인수로 정의되어 딕셔너리의 키와 값은 사용할 수 없음
 c. def personal_info(name='미공개', age=0)      #  ==> O, 딕셔너리의 키 이름과 함수의 키 이름이 같으므로 사용 가능
 d. def personal_info(name, address):           #  ==> X, 함수의 키 이름 중 address가 딕셔너리 키 이름과 다르므로 사용 불가
 e. def personal_info(kwargs):                  #  ==> X, 애스타리스크가 없으므로 매개변수 하나만을 필요로하는 함수임""")
print("="*23)
# ======================================
#  30.6 연습문제: 가장 높은 점수를 구하는 함수 만들기
print("="*5, "30.6 연습문제", "="*5)

korean, english, mathematics, science = 100, 86, 81, 91
def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)

print("="*25)
# ======================================
#  30.7 심사문제: 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기
print("="*5, "30.7 심사문제", "="*5)

korean, english, mathematics, science = map(int, input().split())
def get_min_max_score(*args):
    min_score = min(args)
    max_score = max(args)
    return(min_score, max_score)

def get_average(**kwargs):
    average_score = sum(kwargs.values())/len(kwargs)
    return average_score

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))

print("="*25)
# ======================================