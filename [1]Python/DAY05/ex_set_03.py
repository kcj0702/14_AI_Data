# =========================================================
# 컨테이너 자료형 - [5] Set 자료형
# 
# - set 자료형 전용 함수 즉, 메서드
# =========================================================
# ---------------------------------------------------------
# 예시 set 생성
# ---------------------------------------------------------
data = {1, 1, 2, 1, 3, 2, 5, 10, 11, 12}
print(f"data : {len(data)}개, {type(data)}, {data}")

# ---------------------------------------------------------
# 원소/요소 1개 추가 메서드 : add
#                       => 이미 존재하는 데이터이면 추가하지 않음. 에러 발생 X
# ---------------------------------------------------------
data.add(3)
print(f"data : {len(data)}개, {type(data)}, {data}")

data.add(11)
data.add(8)
data.add(3)
data.add(5)
print(f"data : {len(data)}개, {type(data)}, {data}")

# ---------------------------------------------------------
# 원소/요소 여러개 추가 메서드 : update
#                         => 반복 가능한 데이터가 인수로 들어감
# ---------------------------------------------------------
data.update([1,2,3,4,5,6,7,8,9,10])
print(f"data : {len(data)}개, {type(data)}, {data}")

data.update("Gooooood")     # str 타입으로 원소가 8개 존재, 중복 요소 제거
print(f"data : {len(data)}개, {type(data)}, {data}")

data.update(["Gooooood"])   # list 타입으로 원소가 1개 존재.
print(f"data : {len(data)}개, {type(data)}, {data}")

# ---------------------------------------------------------
# 원소/요소 삭제 메서드 : remove
# ---------------------------------------------------------
data.remove(1)
print(f"data : {len(data)}개, {data}")

data.remove('Gooooood')
print(f"data : {len(data)}개, {data}")

# 없으면 Error 발생
# data.remove('Gooooood')

# ---------------------------------------------------------
# 원소/요소 꺼내서 제거하는 메서드 : pop
# ---------------------------------------------------------
popped = data.pop()
print(f"data : {len(data)}개, {data}, 꺼낸 데이터 : {popped}")

popped = data.pop()
print(f"data : {len(data)}개, {data}, 꺼낸 데이터 : {popped}")

popped = data.pop()
print(f"data : {len(data)}개, {data}, 꺼낸 데이터 : {popped}")