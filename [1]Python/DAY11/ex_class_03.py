# =============================================
#         객체지향프로그래밍 언어 - 파이썬
# -> 모든 데이터 관련 자료형 --- 클래스로 구현
# -> 객체지향언어 특징      --- 정보은닉, 다형성, 상속
# =============================================
# -> 정보은닉 특징
#    [기본] 속성과 메서드를 숨기기/감추기
#          공개용 속성과 메서드 따로 존재
# -> 숨겨진 속성의 사용 방법 : getter/setter 메서드
# =============================================
# ---------------------------------------------
# 클래스 목적 : 자동차 데이터를 저장하는 타입
# 클래스 이름 : Car
# 클래스 속성 : number, user, ckey
# 클래스 기능 : forward()
# ---------------------------------------------
class Car:
    # 자동차 인스턴스/객체를 생성 및 초기화 해주는 매직 메서드
    def __init__(self, user, number, ckey):
        self.user = user
        self.number = number
        self.__ckey = ckey          # 비공개 속성 저장. 클래스 내에서만 사용가능

    def forward(self):
        print('forward() 호출')
        print(f"{self.number} 번호 자동차가 앞으로 전진한다.")
        print(f'ckey : {self.__ckey}')

    # getter, setter 메서드 : 비공개 속성의 외부 접근 가능 메서드
    def get_ckey(self):
        return self.__ckey
    
    def set_ckey(self, nkey):
        self.__ckey = nkey

# ---------------------------------------------
# 객체 즉, Car 인스턴스 생성 : 변수명 = 클래스이름()
# -> 생성자 메서드 : 클래스이름() ==> 연결 ==> __init__()
# ---------------------------------------------
myCar = Car('이수홍', '43머1688', '998877')

myCar.forward()

# 자동차 인스턴스/객체의 속성 읽기
print("나의 자동차 번호 :", myCar.number)
print("나의 자동차 소유자 :", myCar.user)
# print("나의 자동차 키 :", myCar.__ckey)     # 비공개 속성으로 클래스 밖에서 사용 불가
print("나의 자동차 키 :", myCar.get_ckey())   # 간접 접근

# 자동차 인스턴스/객체의 속성 변경
myCar.user = '나의 차'
myCar.__ckey = '111111'                     # <= 새로운 __ckey 변수 생성해버림
myCar.set_ckey('새로운 키')                  # <= 비공개 속성 변수값 변경됨
print('나의 자동차 소유자 :', myCar.user)
print("나의 자동차 키    :", myCar.__ckey)
print(myCar.__dict__)

yourCar = Car('마징가', '1111', '998877')
print('나의 자동차 소유자 :', yourCar.user)
# print("나의 자동차 키    :", yourCar.__ckey)
print(yourCar.__dict__)