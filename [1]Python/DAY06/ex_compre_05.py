# ==============================================================
# 컴프리헨션(Comprehension)
# -> 반복문 + 조건문 => 컨테이너 자료형 생성
# ==============================================================
# --------------------------------------------------------------
# SET 자료형과 컴프리헨션
# -> {조건부표현식 for 원소 in 반복가능한자료형 필터링}
# --------------------------------------------------------------
orgList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 8, 2, 5, 10, 3]
print(f"orgList => {orgList}")

# => 기본 방식
newdata = set()
for num in orgList:
    newdata.add(num)
print(f"기본 newdata => {newdata}, {type(newdata)}")

# => 간결하게 처리 : 컴프리헨션
# => 리스트의 모든 원소 추가
newdata = {num for num in orgList}
print(f"기본 newdata => {newdata}, {type(newdata)}")

# => 리스트의 원소 중 짝수값 원소만 집합에 저장
# => 짝수값 가진 원소만 필터링
newdata = {num for num in orgList if not num%2}
print(f"기본 newdata => {newdata}, {type(newdata)}")

# => 리스트의 원소값이 짝수면 2를 곱하고, 홀수면 3을 곱해서 저장
newdata = {num*3 if num%2 else num*2 for num in orgList}
print(f"기본 newdata => {newdata}, {type(newdata)}")

# => 리스트의 원소값이 짝수인 원소만 추가하고   => 필터링
#    그 값이 6 미만이면 '작은 수'로 저장
#    그 값이 6 이상이면 '큰 수'로 저장
#    단, 집합 자료형으로 저장
newdata = {"큰 수" if num >= 6 else "작은 수" for num in orgList if num%2==0}
print(f"기본 newdata => {newdata}, {type(newdata)}")






