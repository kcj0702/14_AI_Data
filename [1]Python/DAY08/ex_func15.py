## ====================================================================
## 람수 표현식 / 람다 함수 / 익명 함수
## ====================================================================
## -> 재사용될 가능성은 낮지만, 문법상 함수가 필요한 경우 
## -> 이름이 없는 1줄 함수  
## -> 형식 : lambda 매개변수1,.., 매개변수 : 코드           
## ====================================================================
## --------------------------------------------------------------------
## [예시] 다양한 사용법
## --------------------------------------------------------------------
## 1. 기본 계산
## --------------------
print((lambda x, y: x - y)(10, 3))    # 7
print((lambda x: x + 10)(5))          # 15

## --------------------
## 2. 문자열 처리
## --------------------
print((lambda s: s.upper())("python"))      # PYTHON
print((lambda s: s * 3)("hi"))              # hihihi
print((lambda s: len(s))("lambda"))         # 6

## --------------------
## 3. 조건 표현식과 함께 사용
## --------------------
print((lambda n: "짝수" if n % 2 == 0 else "홀수")(7))   # 홀수
print((lambda n: "양수" if n > 0 else "음수" if n < 0 else "0")(-2)) # 0 또는 음수

## --------------------
## 4. 리스트/튜플 요소 다루기
## --------------------
print((lambda lst, n: lst[n])([10, 20, 30], 0))          # 10
print((lambda t: t[1] + t[2])((1, 2, 3)))          # 5

## --------------------
## 5. 함수의 반환값으로 사용
## --------------------
def make_double():
    return lambda x: x * 2

f = make_double()       # f = lambda x: x * 2
print(f(8))   # 16

## --------------------------------------------------------------------
## [예시] 내장함수와 사용법 : map(), filter()
## --------------------------------------------------------------------
## --------------------
## 6. map(함수이름 또는 코드, 반복가능한타입) 함께 사용
##    => 모든 원소에 함수/코드 적용
##    => 반환값 : map 타입 ==> 원하는 타입으로 형변환 필요
## --------------------
nums = [1, 2, 3, 4]
result = list(map(lambda x: x * x, nums))
print(result)   # [1, 4, 9, 16]

result = [x*x for x in nums]
print(result)   # [1, 4, 9, 16]

## --------------------
## 7. filter(함수이름 또는 코드, 반복가능한타입)
##    => 모든 원소에 함수/코드 적용
##    => 반환값 : 적용 결과 True인 것, filter 타입 반환
## --------------------
nums = [1, 2, 3, 4, 5, 6]

result = []
for x in nums:
    if x % 2 == 0:
        result.append(x)
print(result)   # [2, 4, 6]

result = [x for x in nums if x%2==0]
print(result)   # [2, 4, 6]

result = list(filter(lambda x: x % 2 == 0, nums))
print(result)   # [2, 4, 6]

## --------------------
## 8. sorted의 key로 사용
## --------------------
words = ["banana", "kiwi", "apple", "grape"]

# str 원소에 인덱스별 알파벳 코드값 비교 정렬
result = sorted(words)
print(result)   # ['apple', 'banana', 'grape', 'kiwi']

# str 원소에 원소개수에 따른 정렬 기준 설정 : key 매개변수
result = sorted(words, key=lambda x: len(x))
print(result)   # ['kiwi', 'apple', 'grape', 'banana']

result = sorted(words, key=lambda x: len(x), reverse=True)
print(result)   # ['banana', 'apple', 'grape', 'kiwi']

## --------------------
## 9. 딕셔너리 값 기준 정렬
## --------------------
data = {"a": 3, "b": 1, "c": 2}

# [기본] 키 기준 정렬
result = sorted(data.items())
print(result)   # [('b', 1), ('c', 2), ('a', 3)]

# [변] 값 기준 정렬로 기준 변경
# data.items() => dict_items([(key1, value), (key2, value), (key3, value)])
result = sorted(data.items(), key=lambda item: item[1])
print(result)   # [('b', 1), ('c', 2), ('a', 3)]

## --------------------
## 10. None 말고 불리언 반환
## --------------------
print((lambda x: x > 10)(15))   # True
print((lambda x: x > 10)(3))    # False