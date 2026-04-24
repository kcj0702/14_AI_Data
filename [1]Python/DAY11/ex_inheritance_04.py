# ==========================================================
#                      상속(Inheritance)
# -> 다중 상속
#    * 파이썬은 다중 상속 허용
#    * 형식 : 자식클래스이름(부모클래스1, 부모클래스2, ... , 부모클래스N)
#    * 규칙 :
#      - 메서드/속성 사용시 실행규칙
#      - (1) 자신의 클래스에서 메서드/속성 찾음
#      - (2) 자신의 클래스에 존재 X => 부모클래스1
#      - (3) 부모클래스1에   존재 X => 부모클래스2
#      - (4) 부모클래스N에   존재 X => ERROR
# ==========================================================
class Animal:
    def hello(self):
        print('안녕 나는 Animal이야')

class Dog(Animal):
    # 상속관계 메서드를 재정의 : 오버라이딩
    def hello(self):
        print('안녕 나는 Dog이야')

class Cat(Animal):
    # 상속관계 메서드를 재정의 : 오버라이딩
    def hello(self):
        print('안녕 나는 Cat이야')

class NewAnimal(Dog, Cat):
    pass

# ==========================================================
# 인스턴스 생성 및 사용
# ==========================================================
# => 인스턴스 생성
dog = Dog()
cat = Cat()
data = list()
new_ani = NewAnimal()

# => 부모-자식 관계 검사
print(f'issubclass(Dog, Animal) : {issubclass(Dog, Animal)}')
print(f'issubclass(Cat, Animal) : {issubclass(Cat, Animal)}')
print(f'issubclass(Cat, Dog)    : {issubclass(Cat, Dog)}')

# => 특정 클래스로 생성된 인스턴스 즉, 객체 여부 검사 isinstance
print(f'issubclass(dog, Animal) : {isinstance(dog, Animal)}')
print(f'issubclass(cat, Animal) : {isinstance(cat, Dog)}')
print(f'issubclass(data, list) : {isinstance(data, list)}')


# => 메서드 사용
cat.hello()
dog.hello()
new_ani.hello()

print(new_ani.__dict__)
print(NewAnimal.__dict__)

print(cat.__dict__)
print(Cat.__dict__)

# 메서드 호출 순서
print('Cat.mro() =>', Cat.mro())
print('NewAnimal.mro() =>', NewAnimal.mro())
