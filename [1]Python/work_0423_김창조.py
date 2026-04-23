# ======================================
#  34.1 예제 클래스와 메서드 만들기
print("="*5, "34.1 예제", "="*5)
 
class Person:
    pass
james = Person()
print(isinstance(james, Person))
def factorial(n):
    if not isinstance(n, int) or n<0:
        return None
    if n == 1:
        return 1
    return n * factorial(n-1)

print("="*21)
# ======================================
#  34.2 예제 속성 사용하기
print("="*5, "34.2 예제", "="*5)
 
class Person:
    __slots__ = ['name', 'age']    # 'name', 'age' 속성만 허용함, 속성이름은 반드시 문자열
maria = Person()
maria.name = '마리아'
maria.age = 20
# maria.address = '서울시'            # 허용되지 않은 속성 => Error

print("="*21)
# ======================================
#  34.3 예제 비공개 속성 사용하기
print("="*5, "34.3 예제", "="*5)
 
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
    
    def pay(self, amount):
        self.__wallet -= amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))

maria = Person('마리아', 20, '서울시', 10000)
maria.pay(3000)

print("="*21)
# ======================================
#  34.4 퀴즈
print("="*5, "34.4.1 퀴즈", "="*5)
print("""다음 클래스의 greeting 메서드를 호출하기 위한 방법으로 올바른 것을 고르세요. ----- 답(d)
class Person:
    def greeting(self):
        print('Hello')
 a. Person.greeting()               #  ==> X
 b. greeting()                      #  ==> X
 c. maria = Person                  #  ==> X
    maria.greeting()
 d. maria = Person()                #  ==> O, 먼저 인스턴스를 생성하고 클래스 객체의 메서드를 사용한다.
    maria.greeting()
 e. Person(greeting)                #  ==> X""")
print("="*23)

print("="*5, "34.4.2 퀴즈", "="*5)
print("""클래스로 인스턴스를 만들 때 호출되는 메서드는 무엇인가요?  ----- 답(__init__)
(메서드 뒤의 괄호는 생략하고 메서드 이름만 입력)""")
print("="*23)

print("="*5, "34.4.3 퀴즈", "="*5)
print("""다음과 같이 Person 클래스가 있습니다. 클래스에서 다른 메서드를 만들었을 때 인스턴스 속성 name에 접근하기 위한 방법으로 올바른 것을 고르세요. ----- 답(e)
class Person:
    def __init__(self, name):
        self.name = name
 a. name                    #  ==> X
 b. self                    #  ==> X
 c. Person.name             #  ==> X
 d. self[name]              #  ==> X
 e. self.name               #  ==> O, self로 인스턴스의 주소를 불러오고, 인스턴스의 속성 name에 접근한다.""")
print("="*23)

print("="*5, "34.4.4 퀴즈", "="*5)
print("""클래스의 메서드 def __init__(self):에서 속성을 만들려고 합니다. 다음 중 비공개 속성을 고르세요. ----- 답(c)
 a. self.name               #  ==> X
 b. self._name              #  ==> X
 c. self.__name             #  ==> O, 비공개 속성명은 언더스코어('_') 두 개로 시작하며, 속성명 끝에는 붙이지 않는다.
 d. self.__name__           #  ==> X
 e. self.name__             #  ==> X""")
print("="*23)

# ======================================
#  34.5 연습문제: 파일에서 10자 이하인 단어 개수 세기
print("="*5, "34.5 연습문제", "="*5)

class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    
    def slash(self):
        print('베기')

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

print("="*25)
# ======================================
#  34.6 심사문제: 게임 캐릭터 클래스 만들기
print("="*5, "34.6 심사문제", "="*5)

class Annie:
    def __init__(self, AP):
        self.ap = AP
    
    def tibbers(self):
        return self.ap * 0.65 + 400
    
health, mana, ap = map(float, input("애니의 체력, 마나, AP 수치를 입력해주세요 >>> ").strip().split())
annie = Annie(ap)
print(f'티버: 피해량 {annie.tibbers()}')

print("="*25)
# ======================================
#  35.2 예제 정적 메서드 사용하기
print("="*5, "35.2 예제", "="*5)

class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

print(Calc.add(10, 20))            # 정적 메서드는 클래스에서 바로 호출 가능
print(Calc.mul(10, 20))            # 정적 메서드는 클래스에서 바로 호출 가능

print("="*21)
# ======================================
#  35.3 예제 클래스 메서드 사용하기
print("="*5, "35.3 예제", "="*5)

class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))

james = Person()
maria = Person()

Person.print_count

print("="*21)

# ======================================
#  35.4 퀴즈
print("="*5, "35.4.1 퀴즈", "="*5)
print("""다음 중 클래스 바깥에서 클래스 속성 x에 접근하는 방법으로 올바른 것을 고르세요. ----- 답(a)
class Person:
    x = {}
 a. Person.x                #  ==> O, 클래스 속성은 클래스명으로 불러올 수 있다.
 b. Person(x)               #  ==> X
 c. x                       #  ==> X
 d. self.x                  #  ==> X
 e. Person['x']             #  ==> X""")
print("="*23)

print("="*5, "35.4.2 퀴즈", "="*5)
print("""다음 중 정적 메서드로 올바른 것을 고르세요. ----- 답(c)
 a. def print_count(self):          #  ==> X
        print(self.count)
 b. @staticmethod                   #  ==> X
    def sub(self, a, b):
        print(a - b)
 c. @staticmethod                   #  ==> O, 데코레이터 @staticmethod가 첫 줄에 사용되고, 메서드의 매개변수로 self, cls를 받지 않아야 함
    def div(a, b):
        print(a / b)
 d. @staticmethod                   #  ==> X
    def add(cls, a, b)
        print(a + b)
 e. def print_count(cls):           #  ==> X
        print(cls.count)""")
print("="*23)

print("="*5, "35.4.3 퀴즈", "="*5)
print("""다음 중 클래스 메서드에 대한 설명으로 잘못된 것을 고르세요. ----- 답(c, e)
 a. 클래스 메서드는 클래스.메서드() 형식으로 호출한다.#  ==> O
 b. 클래스 메서드는 위에 @classmethod를 붙여서 만든다.#  ==> O
 c. 클래스 메서드의 첫 번째 매개변수는 self이며 현재 인스턴스가 들어온다.#  ==> X, 첫 번째 매개변수는 cls이며, 클래스 정보가 들어옴
 d. 클래스 메서드는 인스턴스 없이 호출할 수 있다.#  ==> O
 e. 클래스 메서드는 위에 @staticmethod를 붙여서 만든다.#  ==> X, @classmethod를 붙여서 만듦""")
print("="*23)

# ======================================
#  35.5 연습문제: 날짜 클래스 만들기
print("="*5, "35.5 연습문제", "="*5)

class Date:
    @staticmethod
    def is_date_valid(date):
        year, month, day = map(int, date.split('-'))
        if (year >= 0) and (1 <= month <=12) and (1<= day <= 31):
            return True
        else:
            return False

if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

print("="*25)
# ======================================
#  35.6 심사문제: 시간 클래스 만들기
print("="*5, "35.6 심사문제", "="*5)

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return (0 <= hour <= 23) and (0 <= minute <= 59) and (0 <= second <= 59)

    @staticmethod
    def from_string(time_string):
        hour, minute, second = time_string.split(':')
        return Time(hour, minute, second)

time_string = input()
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')

print("="*25)
# ======================================