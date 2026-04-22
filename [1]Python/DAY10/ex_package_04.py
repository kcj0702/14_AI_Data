# ======================================================================
#                       파이썬 표준 모듈 및 패키지
# ======================================================================
# random 모듈 : 무작위 값 생성 모듈
# ======================================================================
# ----------------------------------------------------------------------
# 모듈 로딩
# ----------------------------------------------------------------------
import random

# ----------------------------------------------------------------------
# 모듈 사용
# ----------------------------------------------------------------------
# random.random()      : 실수
# => 0 이상 1 미만(0<= ~ <1)의 실수를 무작위로 반환
print(random.random(), random.random(), random.random())

# random.randint(a, b) : 정수 a<= ~ <=b
# => a 이상 b 미만(a<= ~ <=b)의 정수를 무작위로 반환
print(random.randint(1, 2), random.randint(1, 2), random.randint(1, 2))

# random.randrange(start, stop, step) : 정수, start<= ~ <stop
# => range()처럼 범위를 정해서 무작위 값 반환
print(random.randrange(1, 10))      # 1~9
print(random.randrange(0, 10, 2))   # 0,2,4,6,8

# random.uniform(start, stop) : 실수, start<= ~ <stop
# => a 부터 b 사이의 실수를 무작위로 반환
print(random.uniform(1, 2), random.uniform(1, 2), random.uniform(1, 2))

# random.choice(순서있는 데이터타입)
# => 1개 무작위 선택 반환
print(random.choice([1, 2, 3]), random.choice([1, 2, 3]), random.choice([1, 2, 3]))

# random.choices(순서있는 데이터타입, k=n)
# => n개 무작위 선택 반환, 중복 가능
print(random.choices([1, 2, 3], k=5))

# random.sample(순서있는 데이터타입, k=n)
# => n개 무작위 선택 반환, 중복 불허
print(random.sample([1, 2, 3], k=2))

print(random.sample(range(1, 46), k=6))
print(random.sample(range(1, 46), k=6))
print(random.sample(range(1, 46), k=6))
print(random.sample(range(1, 46), k=6))

# random.seed()
# => 매번 동일한 랜덤값 추출하도록 고정
random.seed(10)

print('seed 고정')
print(random.sample(range(1, 46), k=6))
print(random.sample(range(1, 46), k=6))
print(random.sample(range(1, 46), k=6))
print(random.sample(range(1, 46), k=6))