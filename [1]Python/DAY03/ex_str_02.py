# =======================================
# 기본 + 컨테이너 자료형 - [3] str 타입
# 
# * 산술 연산자
#   + : str + str 만 가능 ==> str 연결
#   * : str * int 만 가능 ==> str을 정수만큼 반복 연결
# =======================================
# -------------------------
# str 생성
# -------------------------
msg = "Good Luck"
year = str("2026")

# -------------------------
# str과 산술 연산자 : 덧셈
# -------------------------
new_msg = msg + " " + year

print(f"msg : {msg}")
print(f"year : {year}")
print(f"new_msg : {new_msg}")

# -------------------------
# str과 산술 연산자 : 곱셈
# -------------------------
new_msg = (msg + " ") * 5

print(f"msg : {msg}")
print(f"new_msg : {new_msg}")


# =======================================
# * 멤버 연산자
#   데이터 in str     : 존재하면 True
#   데이터 not in str : 존재하지 않으면 True
# =======================================
msg = "Happy Day"

print(f"'h' in msg : {'h' in msg}")
print(f"'H' not in msg : {'H' not in msg}")
print(f"'Hap' not in msg : {'Hap' in msg}")
