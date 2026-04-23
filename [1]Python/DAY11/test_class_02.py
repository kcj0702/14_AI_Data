# =============================================================
# 사용자 정의 클래스
# =============================================================

# -------------------------------------------------------------
# 사람 클래스 정의
# -------------------------------------------------------------
# -> 데 이 터 : 이름, 성별, 나이, 키, 몸무게
# -> 기능/역할 : 먹기, 자기
# -------------------------------------------------------------
# -> 클래스 이름 : Hongsu_Lee
# -> 클래스 속성 : name, gender, age, height, weight
# -> 클래스 함수 : eat(), sleep(), diet()
# -------------------------------------------------------------
class Hongsu_Lee:

    def __init__(self, name, gender, age, height, weight):
        self.name = name
        self.gender = gender
        self.age = int(age)
        self.height = int(height)
        self.weight = int(weight)

    def eat(self, food):
        print(f'{self.name}이/가 {food}을/를 먹습니다.')
        if food == '떡국':
            print(f'새해가 되어 {self.name}이 {food}을/를 먹고 나이도 먹었습니다.')
            self.age += 1
            print("나이 :", self.age)
        self.weight += len(food)
        print(f'{self.name}의 몸무게가 무럭무럭 증가하여 {self.weight}kg이 되었습니다.')
    
    def sleep(self, hour):
        print(f'{self.name}이/가 {hour}시간 잤습니다.')
        self.height += hour * 0.1
        print(f'{self.name}의 키가 무럭무럭 커서 {self.height}cm가 되었습니다.')

    @staticmethod
    def diet():
        print('다이어트에 실패했습니다.')

suhong = Hongsu_Lee('수홍', '남', '28', '190', '95')
suhong.eat('햄버거')
suhong.diet()
suhong.sleep(8)
suhong.eat('떡국')
suhong.eat('떡국')
suhong.diet()