# =======================================
# 기본 + 컨테이너 자료형 - [3] str 타입
# 
# * str 전용 함수 즉, 메서드 이해
# =======================================
# -------------------------
# [10] 특정 문자열/문자로 시작하는지 또는 끝나는지 검사하는 메서드
#       -> startswith(문자열/문자) : 시작검사   => True/False
#       -> endswith(문자열/문자)   : 끝 검사    => True/False
# -------------------------
file_name1 = "data.csv"
file_name2 = "image.jpg"
file_name3 = "image.png"

# Unpacking 언패킹
# 컨테이너 자료형에서 1개의 변수명으로 관리하던 데이터를 여러개의 변수명으로 나누어서 저장
file_name1, file_name2, file_name3 = "data.csv", "image.jpg", "image.png"

# 특정 문자열/문자로 시작하는지 검사 진행 : startswith()
ret = file_name1.startswith("i")
print(f"{file_name1} => {ret}")

ret = file_name1.startswith("ima")
print(f"{file_name1} => {ret}")

ret = file_name1.startswith("d")
print(f"{file_name1} => {ret}")

# 특정 문자열/문자로 끝나는지 검사 진행 : endswith()
ret = file_name1.endswith(".csv")
print(f"{file_name1} : .csv? => {ret}")

ret = file_name2.endswith(".csv")
print(f"{file_name2} : .csv? => {ret}")

ret = file_name1.endswith((".csv", ".jpg"))
print(f"{file_name1} : .csv or jpg? => {ret}")