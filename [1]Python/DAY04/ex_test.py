# ====================================
# 복습 실습 문제
# ====================================
# [문제1] 사용자로부터 데이터를 입력 받은 후
#        해당 데이터가 알파벳만 있는지,
#        숫자만 있는지, 알파벳과 숫자가 있는지
#        검사 결과 출력해 주세요.
# [예시] 메시지 입력 : Good
#       검  사 결과 : 알파벳만     True
#                    숫자만      False
#                 알파벳, 숫자    True
# ====================================
print("=" * 30)

msg = input()
print("알파벳만", msg.isalpha())
print("숫자만", msg.isdecimal())
print("알파벳, 숫자", msg.isalnum())

print("=" * 30)
# ====================================
# [문제2] 1~100 범위에서 3의 배수와 7의 배수 숫자만 저장하세요.
#        그리고 해당 데이터에서 가장 큰 수, 가장 작은 수 출력하세요.
#        그리고 해당 데이터를 내림차순으로 정렬해 주세요.
# ====================================
print("=" * 30)

li = set(range(3, 101, 3))
li.update(set(range(7, 101, 7)))
li = list(li)
print("가장 큰 수 :", max(li))
print("가장 작은 수 :", min(li))
li.sort(reverse=True)
print("내림차순 정렬 :", li)

print("=" * 30)
# ====================================
# [문제3] 사용자의 주민등록 번호, 성별을 저장하세요.
#        해당 데이터는 저장 후 변경이 불가한 데이터 입니다.
#        그런데, 개명신청에 따른 이름 변경이 발생되었고
#        변경된 이름을 적용후 다시 변경이 불가하도록
#        저장해 주세요.
# ====================================
print("=" * 30)

change = []
profile = tuple(input("주민등록 번호, 성별, 이름을 적어주세요.(oooooo-ooooooo 남/여 이름) ").split())
print("타입", type(profile), profile)
name_change = input("변경된 이름을 적어주세요.(이름) ")
for i in range(len(profile)-1):
    change.append(profile[i])
change.append(name_change)
profile = tuple(change)
print(profile)