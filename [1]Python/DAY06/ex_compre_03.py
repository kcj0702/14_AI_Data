# ==============================================================
# 컴프리헨션(Comprehension)
# -> 반복문 + 조건문 => 컨테이너 자료형 생성
# ==============================================================
# --------------------------------------------------------------
# [형식3] 반복문으로 컨테이너 자료형 생성
#        [원소 if 조건식 else 원소 for 원소 in 반복가능한자료형]
#           ↑     ↑        ↑          ---- (1) ----
#           |     |________|__(2)___________|
#        (3)|_(참)|_(거짓)__|(3)
# --------------------------------------------------------------
# orgList의 원소 중에 짝수값을 가진 원소는 3을 곱하고,
#                   홀수값을 가진 원소는 그대로 사용해서
#                   새로운 newList 생성
orgList = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"orgList => {orgList}")

# => 기본 방식
newList = []
for num in orgList:
    # if not (num % 2):
    #     newList.append(num * 3)
    # else:
    #     newList.append(num)
    newList.append(num*3 if not (num%2) else num)
print(f"기본 newList => {newList}")

# => 간결하게 처리 : 컴프리헨션
newList = [num*3 if not (num%2) else num for num in orgList]
print(f"컴프리 newList => {newList}")

