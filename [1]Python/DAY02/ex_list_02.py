# ====================================================
# 컨테이너 자료형 - [1] 순서있는 자료형 List

#  -> 다양한 내장함수 활용
# ====================================================
# list 생성하기 => 다양한 데이터
# ====================================================
datas1 = []
datas2 = ["Hello", 123, 0.98, True]
datas3 = [[100, 200, 300], [6, 9, 8], ["god"]]

# ---------------------------
# 내장함수: type( 변수명 ) -> 저장 데이터의 타입 확인
# ---------------------------
print(f"type(data1) : {type(datas1)}, {datas1}")
print(f"type(data2) : {type(datas2)}, {datas2}")
print(f"type(data3) : {type(datas3)}, {datas3}")

# ---------------------------
# 내장함수: len( 변수명 ) -> 데이터 개수 반환 함수
# ---------------------------
print(f"type(data1) : {len(datas1)}개, {datas1}")
print(f"type(data2) : {len(datas2)}개, {datas2}")
print(f"type(data3) : {len(datas3)}개, {datas3}")

# ---------------------------
# 내장함수: max( 변수명 ) -> 데이터/요소 중 최고값 데이터
#          min( 변수명 ) -> 데이터/요소 중 최소값 데이터
# ★ str 데이터는 문자 1개 1개의 코드값을 비교함!!
# ---------------------------
data2 = [7, 20, 1, -5, 10, 15]
data3 = ["Abc", "apple", "eung-ae", "zoo"]

print(f"max(data2) : {max(data2)}, min(data2) : {min(data2)}")
print(f"max(data3) : {max(data3)}, min(data3) : {min(data3)}")

# ---------------------------
# 내장함수: sum( 변수명 ) -> 데이터/요소들의 합계 반환 함수
# ★ sum() 함수는 수치 데이터만 가능함
# ---------------------------
print(f"sum(datas1) : {sum(datas1)}, {datas1}")
print(f"sum(data2) : {sum(data2)}, {data2}")
# print(f"sum(datas3) : {sum(datas3)}, {datas3}")