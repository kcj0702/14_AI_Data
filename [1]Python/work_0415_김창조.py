# ======================================
#  25.2 예제 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기
print("="*5, "25.2 예제", "="*5)

x = {'a':10, 'b':20, 'c':30, 'd':40}
for i in x:
    print(i, end=' ')

for key, value in x.items():
    print(key, value)

print("="*21)
# ======================================
#  25.4 예제 딕셔너리 안에서 딕셔너리 사용하기
print("="*5, "25.4 예제", "="*5)

terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25614
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600
    }
}
print(terrestrial_planet['Venus']['mean_radius'])
    
print("="*21)
# ======================================
#  25.5.1 예제 중첩 딕셔너리의 할당과 복사 알아보기
print("="*5, "25.5.1 예제", "="*5)

x = {'a':{'python':'2.7'}, 'b':{'python':'3.6'}}
y = x.copy()
y['a']['python'] = '2.7.15'

print(x)
print(y)

x = {'a':{'python':'2.7'}, 'b':{'python':'3.6'}}
import copy
y = copy.deepcopy(x)
y['a']['python'] = '2.7.15'

print(x)
print(y)

print("="*23)
# ======================================
#  25.6 퀴즈
print("="*5, "25.6.1 퀴즈", "="*5)
print("""다음 중 딕셔너리 x에서 키 'python'과 해당 값을 삭제하는 방법으로 올바른 것을 모두 고르세요. ----- 답(c, e)
 a. x.pop()                 #  ==> X, 소괄호 안에 키를 입력해야함
 b. x.popitem()             #  ==> X
 c. x.pop('python',100)     #  ==> O, 'python'키와 값을 삭제하고 키가 없다면 100을 반환
 d. x.remove('python')      #  ==> X, remove 메서드 없음
 e. del x['python']         #  ==> O""")
print("="*23)
# ======================================
#  25.6 퀴즈
print("="*5, "25.6.2 퀴즈", "="*5)
print("""다음 중 딕셔너리의 메서드에 대한 설명으로 올바르지 않은 것을 모두 고르세요. ----- 답(b, c)
 a. setdefault는 딕셔너리에 키-값 쌍을 추가한다.        #  ==> O
 b. setdefault는 키만 지정하면 값은 0으로 저장한다.     #  ==> X, None으로 저장함
 c. keys는 딕셔너리의 키-값쌍을 모두 가져온다.          #  ==> X, 키들을 리스트 모양으로 보여주며 클래스는 dict_keys임
 d. clear는 딕셔너리의 모든 키-값 쌍을 삭제한다.        #  ==> O
 e. update는 딕셔너리에서 키의 값을 수정한다.           #  ==> O""")
print("="*23)
# ======================================
#  25.6 퀴즈
print("="*5, "25.6.3 퀴즈", "="*5)
print("""다음 중 반복문으로 딕셔너리 x의 모든 키를 출력하는 방법으로 올바른 것을 모두 고르세요. ----- 답(b, c, e)
 a. for key, value in x:            #  ==> X
        print(key)
 b. for key in x:                   #  ==> O, 키만 꺼내옴
        print(key)
 c. for key in x.keys():            #  ==> O, 키들만 뽑은 dict_keys에서 키만 꺼내옴
        print(key)
 d. for value in x.values():        #  ==> X
        print(value)
 e. for key, value in x.items():    #  ==> O, 키와 값들을 각각 key, value에 꺼내오고 key만 출력
        print(key)""")
print("="*23)
# ======================================
#  25.6 퀴즈
print("="*5, "25.6.5 퀴즈", "="*5)
print("""다음 코드에서 딕셔너리 terrestrial_planet의 키 'satellites'에 접근하는 방법으로 올바른 것을 고르세요. ----- 답(d)
terrestrial_planet = {
    'Earth': {
        'physical_characteristics': {
            'mean_radius': 6371.0,
            'mass': 5.97219E+24
        },
        'orbital_characteristics': {
            'orbital_period': 365.25641,
            'satellites': 1
        }
    },
    'Mars': {
        'physical_characteristics': {
            'mean_radius': 3389.5,
            'mass': 6.4185E+23
        },
        'orbital_characteristics': {
            'orbital_period': 686.9600,
            'satellites': 2
        }
    }
}
 a. terrestrial_planet('Earth')('orbital_characteristics')('satellites')    #  ==> X, 대괄호 써야함
 b. terrestrial_planet['satellites']                                        #  ==> X, 최상위 딕셔너리 안에는 'satellites' 키 없음
 c. terrestrial_planet['Earth']['satellites']                               #  ==> X, 뛰어넘기
 d. terrestrial_planet['Earth']['orbital_characteristics']['satellites']    #  ==> O
 e. terrestrial_planet['Mars']['physical_characteristics']['mass']          #  ==> X, 'mass'를 왜 불러옴?""")
print("="*23)
# ======================================
#  25.6 퀴즈
print("="*5, "25.6.6 퀴즈", "="*5)
print("""다음 코드의 실행 결과로 올바른 것을 고르세요. ----- 답(c)
 import copy
 x = {'python': {'version':'2.7'}, 'script': {'name': 'hello.py'}}
 a = x
 b = x.copy()
 c = copy.deepcopy(x)
 x['python']['version'] = '3.6'
 print(a['python']['version'], b['python']['version'], c['python']['version'])
 a. 2.7 2.7 2.7         #  ==> X
 b. 3.6 2.7 2.7         #  ==> X
 c. 3.6 3.6 2.7         #  ==> O, 중첩 딕셔너리는 copy 모듈의 deepcopy를 사용해야 독립된 두 개의 딕셔너리가 생성됨
 d. 3.6 3.6 3.6         #  ==> X
 e. 2.7 3.6 3.6         #  ==> X""")
print("="*23)
# ======================================
#  25.7 연습문제: 평균 점수 구하기 
print("="*5, "25.7 연습문제", "="*5)

maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
avg = sum(maria.values()) / len(maria)
print(avg)

print("="*25)
# ======================================
#  25.8 심사문제: 딕셔너리에서 특정 값 삭제하기
print("="*5, "25.8 심사문제", "="*5)

keys = input("키들을 입력하세요 >>>").split()
values = map(int, input("값들을 입력하세요 >>>").split())
x = dict(zip(keys, values))
key_30 = ""
for key, value in x.items():
    if value == 30:
        key_30 = key
del x['delta']
del x[key_30]
print(x)

print("="*25)
# ======================================
#  26.2 예제 집합 연산 사용하기
print("="*5, "26.2 예제", "="*5)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(a.union(b))
print(a & b)
print(a.intersection(b))
print(a - b)
print(a.difference(b))
print(a ^ b)
print(a.symmetric_difference(b))

a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4})
print(a.issubset({1, 2, 3, 4, 5}))
print(a < {1, 2, 3, 4, 5})
print(a >= {1, 2, 3, 4})
print(a.issuperset({1, 2, 3, 4, 5}))
print(a > {1, 2, 3, 4, 5})

print(a.isdisjoint({5, 6, 7, 8}))
print(a.isdisjoint({3, 4, 5, 6}))

print("="*21)
# ======================================
#  26.5 예제 반복문으로 세트의 요소를 모두 출력하기
print("="*5, "26.5 예제", "="*5)

a = {1, 2, 3, 4}
for i in a:
    print(i)

print("="*21)
# ======================================
#  26.7 퀴즈
print("="*5, "26.7.1 퀴즈", "="*5)
print("""다음 중 세트를 만드는 방법으로 올바르지 않은 것을 고르세요. ----- 답(b)
 a. a = {1, 2, 3, 4, 5}         #  ==> O
 b. a = {}                      #  ==> X, 빈 dict가 생성됨
 c. a = set('hello')            #  ==> O
 d. a = set(range(10))          #  ==> O
 e. a = set()                   #  ==> O""")
print("="*23)
# ======================================
#  26.7 퀴즈
print("="*5, "26.7.2 퀴즈", "="*5)
print("""세트 a = {1, 2, 3} 그리고 b = {3, 4, 5}가 있을 때 집합 연산의 결과로 잘못된 것을 모두 고르세요. ----- 답(b, e)
 a. set.union(a, b)는 {1, 2, 3, 4, 5)       #  ==> O
 b. a ^ b는 {1, 3, 5}                       #  ==> X, 대칭차집합, {1, 2, 4, 5}
 c. a - b는 {1, 2}                          #  ==> O
 d. a & b는 {3}                             #  ==> O
 e. set.difference(b, a)는 {4}              #  ==> X, b - a {4, 5}""")
print("="*23)
# ======================================
#  26.7 퀴즈
print("="*5, "26.7.3 퀴즈", "="*5)
print("""다음 중 부분집합, 상위집합에 대한 설명으로 잘못된 것을 모두 고르세요. ----- 답(b, d)
 a. 부분집합은 <=와 issubset로 구할 수 있고, 두 세트가 같을 때 참이다.          #  ==> O
 b. 진부분집합은 <와 issubset로 구할 수 있고, 두 세트가 다를 때 참이다.         #  ==> X, 진부분집합은 issubset로 구할 수 없음
 c. 상위집합은 >=와 issuperset로 구할 수 있고, 두 세트가 같을 때 참이다.        #  ==> O
 d. 진상위집합은 >로 구할 수 있고, 두 세트가 같을 때 참이다.                    #  ==> X, 두 세트가 같을 때는 거짓임
 e. 진부분집합과 진상위집합을 구하는 메서드는 없다.                             #  ==> O""")
print("="*23)
# ======================================
#  26.7 퀴즈
print("="*5, "26.7.4 퀴즈", "="*5)
print("""다음 중 세트 메서드에 대한 설명으로 올바른 것을 모두 고르세요. ----- 답(d, e)
 a. intersection_update는 현재 세트와 다른 세트 중에서 겹치는 요소만 현재 세트에 저장한다.      #  ==> O
 b. set.symmetric_difference는 두 세트의 대칭차집합을 구한다.                               #  ==> O
 c. isdisjoint는 현재 세트가 다른 세트와 겹치지 않는지 확인한다.                              #  ==> O
 d. discard는 현재 세트에서 특정 요소를 삭제하고 요소가 없으면 에러를 발생시킨다.                #  ==> X, 요소가 없어도 에러를 발생시키지 않음
 e. pop은 현재 세트에서 지정된 요소를 삭제하고 요소가 없으면 에러를 발생시킨다.                  #  ==> X, 임의의 요소를 삭제함""")
print("="*23)
# ======================================
#  26.7 퀴즈
print("="*5, "26.7.5 퀴즈", "="*5)
print("""다음 중 메서드와 연산자의 기능이 잘못 짝지어진 것을 고르세요. ----- 답(c, d)
 a. set.intersection은 &와 같다.                    #  ==> O
 b. set.update는 |=와 같다.                         #  ==> O
 c. symmetric_difference_update는 -=와 같다.        #  ==> X, -=는 difference_update와 같으며, symmetric_difference_update는 대칭차집합임
 d. issuperset은 >와 같다.                          #  ==> X, issuperset은 >=와 같음
 e. set.union은 |와 같다.                           #  ==> O""")
print("="*23)
