# =========================================================
# 컨테이너 자료형 - [4] Dict 자료형
# 
# Dict와 추가 메서드들 살펴보기
# =========================================================
# ---------------------------------------------------------
# dict에서 원소/요소 읽어오는 메서드 => get
# ---------------------------------------------------------
# 예시 dict 생성
data = {1:100, 2:98, 3:100}
print(f"원소 개수 : {len(data)}개, {data}")

# 키가 존재하는 경우
value = data.get(2)
print(f"get(data) : {value} | {data}")
print(f"data[2] : {data[2]} | {data}")

# 키가 존재하지 않는 경우
value = data.get("a", "존재하지 않는 키입니다.")
print(f"get(a) : {value} | {data}")
# print(f"data[a] : {data[a]} | {data}")        # Key Error

value = data.get(1, "존재하지 않는 키입니다.")
print(f"get(1) : {value} | {data}")

# ---------------------------------------------------------
# 키 정보만 가지고 dict 생성 메서드 : fromkeys
# ---------------------------------------------------------
key = range(10, 100, 10)
data = dict.fromkeys(key)
print(f"원소 개수 : {len(data)}개, {data}")

data = dict.fromkeys(key, 0)
print(f"원소 개수 : {len(data)}개, {data}")