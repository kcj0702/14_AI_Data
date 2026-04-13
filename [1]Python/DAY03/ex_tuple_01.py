# ========================================
# 컨테이너 자료형 - [2] Tuple
# 
# * 다양한 자료형 데이터를 여러 개 저장 가능
# * 단, 저장/읽기만 가능
#   => Read Only List라고도 함
# ========================================
# -------------------
# Tuple 생성
# -------------------
# 변수명 = (데이터1, 데이터2, ...)
# 변수명 = 데이터1, 데이터2, ...
# 변수명 = (데이터1,)       ★ 꼭 쉼표(,) 입력
# 변수명 = 데이터1,         ★ 꼭 쉼표(,) 입력

# ==> 데이터가 여러개인 경우
datas1 = ("2026-04-13", "이O환", 27)
datas2 = "2026-04-13", "이O환", 27

print(f"데이터 : {datas1}, 타입 : {type(datas1)}, 원소 수 : {len(datas1)}개")
print(f"데이터 : {datas2}, 타입 : {type(datas2)}, 원소 수 : {len(datas2)}개")

# ==> 데이터가 한 개인 경우
# datas1 = ("이O환",)
# datas2 = ("이무O")
datas3 = "이무ㅎ",

print(f"데이터 : {datas1}, 타입 : {type(datas1)}, 원소 수 : {len(datas1)}개")
print(f"데이터 : {datas2}, 타입 : {type(datas2)}, 원소 수 : {len(datas2)}개")
print(f"데이터 : {datas3}, 타입 : {type(datas3)}, 원소 수 : {len(datas3)}개")

# -------------------
# Tuple과 연산자
# -------------------
# 산술 연산자 : +, * => 새로운 튜플 반환
# -------------------
new_datas = datas1 + datas2
print(f"데이터 : {new_datas}, 타입 : {type(new_datas)}, 원소 수 : {len(new_datas)}개")

new_datas = datas1 * 3
print(f"데이터 : {new_datas}, 타입 : {type(new_datas)}, 원소 수 : {len(new_datas)}개")

# -------------------
# 멤버 연산자 : 데이터 in 튜플          # 존재하면 True
#             데이터 not in 튜플      # 존재하지 않으면 True
# -------------------
print(f"27 in datas : {27 in datas1}")
print(f"27 not in datas : {27 not in datas1}")




