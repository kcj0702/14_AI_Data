# ====================================================
# 컨테이너 자료형 - [1] 순서있는 자료형 List

#  -> 다양한 내장함수 활용
# ====================================================
# list 생성하기 => 다양한 데이터
# ====================================================
datas1 = []
datas2 = [6, 123, 0.98]
datas3 = ["anaconda", "apple", "Abc", "zoo"]

# ---------------------------
# 내장함수: sorted( 변수명 ) -> 데이터/요소들 정렬 후 list로 반환 함수
# 
# ★ 항상 list로 반환
# ---------------------------
print(f"sorted(datas1) : {sorted(datas1)}, {datas1}")
print(f"sorted(datas2) : {sorted(datas2)}, {datas2}")
print(f"sorted(datas3) : {sorted(datas3)}, {datas3}")

print(f"내림차순 sorted(datas1) : {sorted(datas1, reverse=True)}, {datas1}")
print(f"내림차순 sorted(datas2) : {sorted(datas2, reverse=True)}, {datas2}")
print(f"내림차순 sorted(datas3) : {sorted(datas3, reverse=True)}, {datas3}")

# ---------------------------
# 내장함수: range( 시작값, 끝값+1, 간격 ) -> 데이터 범위 생성 후 반환 함수
# 
# ★ 많은 데이터 생성 시 사용하는 함수
#    -> 데이터 범위 객체/타입 생성
#    -> 데이터 범위 : 시작값 <= ~ < 끝값+1
# ex) 1부터 1000까지 OR 1 ~ 1000  ==> [1,2,3,4,5,6,7,8,9,... ,999,1000]
#                                ==> range(1,1001)
# ---------------------------
# 1~10까지 숫자 데이터 저장
# ---------------------------
datas1 = [1,2,3,4,5,6,7,8,9,10]
datas2 = range(1,11)        # 1이상 11미만

print(f"datas1 : {datas1}, {len(datas1)}개, type(datas1) : {type(datas1)}")
print(f"datas2 : {datas2}, {len(datas2)}개, type(datas2) : {type(datas2)}")

# ---------------------------
# 1~1000000000까지 숫자 데이터 저장
# ---------------------------
datas1 = [1,2,3,4,5,6,7,8,9,10]
datas2 = range(1,1000000001)        # 1이상 1000000001미만

print(f"datas1 : {datas1}, {len(datas1)}개, type(datas1) : {type(datas1)}")
print(f"datas2 : {datas2}, {len(datas2)}개, type(datas2) : {type(datas2)}")

# ---------------------------
# 1~30까지 숫자 중 3의 배수의 데이터 저장
# ---------------------------
datas1 = [3,6,9,12,15,18,21,24,27,30]
datas2 = range(3,31,3)        # 1이상 31미만

print(f"datas1 : {datas1}, {len(datas1)}개, type(datas1) : {type(datas1)}")
print(f"datas2 : {datas2}, {len(datas2)}개, type(datas2) : {type(datas2)}, {list(datas2)}")

# ---------------------------
# [퀴즈] 50 ~ 1까지 범위의 숫자를 출력하세요.
#        단, range()함수를 사용하세요.
# ---------------------------
li1 = list(range(50,0,-1))
for i in li1:
    print(i,end=" ")
