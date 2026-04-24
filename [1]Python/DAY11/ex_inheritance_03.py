## ==========================================================
##                      상속(Inheritance)
## -> 메서드 오버라이딩(Overriding)
##    * 상속관계에만 적용되는 문법
##    * 자식 클래스에서 물려받은 부모의 메서드를 구현부만 수정하는 것
##    * 메서드 재정의라고 함
## ==========================================================

## ----------------------------------------------------------
## 클래스이름 : Point
## 클래스속성 : x, y          --- 위치. 좌표값  
##            color         --- 색상
##            radius        --- 반지름
##            shape         --- 형태. [기] 동그라미
## 클래스기능 : 정보 출력 기능  --- print_info()
##            점 그리기 기능  --- drawing()
## ----------------------------------------------------------
class Point:
    # -----------------------
    # 클래스 변수/속성/필드
    # -----------------------    
    
    # -----------------------
    # 인스턴스 변수/속성/필드 초기화 매직 메서드
    # -----------------------
    def __init__(self, x, y, color, radius, shape='동그라미'):
        self.x = x
        self.y = y 
        self.color = color
        self.radius = radius
        self.shape = shape

    # -----------------------
    # 인스턴스 메서드 
    # -----------------------
    def drawing(self):
        print(f'({self.x},{self.y})좌표에 {self.shape} 그리기')

    def print_info(self):
        print('[Point 정보]---')
        print(f'형  태 : {self.shape}')
        print(f'좌  표 : ({self.x},{self.y}) ')
        print(f'색  상 : {self.color}')
        print(f'반지름 : {self.radius}')
        print('-----------\n')


## ----------------------------------------------------------
## 클래스이름 : Point3D
## 클래스속성 : x, y, z       --- 위치. 좌표값  
##            color         --- 색상
##            radius        --- 반지름
##            shape         --- 형태. [기] 동그라미
## 클래스기능 : 정보 출력 기능  --- print_info()
##            점 그리기 기능  --- drawing()
##            점  변경  기능  --- converting()
## 부모클래스 : Point
## ----------------------------------------------------------
class Point3D (Point):
    # -----------------------
    # 클래스 변수/속성/필드
    # -----------------------    
    
    # -----------------------
    # 인스턴스 변수/속성/필드 초기화 매직 메서드
    # -----------------------
    def __init__(self, x, y, z, color, radius, shape='동그라미'):
        # 부모 인스턴스 생성
        super().__init__(x, y, color, radius, shape)
        # 부모 클래스에 없는 인스턴스 변수/속성 추가
        self.z = z

    # -----------------------
    # 인스턴스 메서드
    # -----------------------
    def converting(self, new_shape):
        self.shape = new_shape
        self.drawing()

    # -----------------------
    # 오버라이딩 인스턴스 메서드 
    # -----------------------
    def drawing(self):
        print('Point3D 그리기')
        print(f'({self.x},{self.y},{self.z})좌표에 {self.shape} 그리기')

    def print_info(self):
        print('[Point 정보]---')
        print(f'형  태 : {self.shape}')
        print(f'좌  표 : ({self.x},{self.y},{self.z}) ')
        print(f'색  상 : {self.color}')
        print(f'반지름 : {self.radius}')
        print('-----------\n')

## ==========================================================
## 인스턴스 즉, 객체 생성 및 사용
## ==========================================================
## => 객체 생성
p1 = Point(3, 5, 'green', 10, '사각형')
p2 = Point3D(5, 5, 5, 'red', 3, "다각형")


## => 객체 사용
p1.print_info()
p1.drawing()

print("-"*10)
p2.print_info()             ## <- Point로부터 상속받은 메서드
p2.drawing()                ## <- Point로부터 상속받은 메서드
p2.converting('동그라미')    ## <- Point3D의 메서드

