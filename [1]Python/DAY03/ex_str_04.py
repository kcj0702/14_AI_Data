# =======================================
# 기본 + 컨테이너 자료형 - [3] str 타입
# 
# * str 전용 함수 즉, 메서드 => 다른 타입에 비해 아주 많음
# * str 메서드를 많이 알 수록 편해짐
# =======================================
# -------------------------
# str 생성
# -------------------------
msg = "good luck"
#      012345678
# -------------------------
# [4] 원소/요소 변경 후 반환 => replace(문자/문자열)
#       * 변환된 새로운 문자열 반환
#       * 원본 문자열 변경 안됨
# -------------------------
# "good luck" ---> 'Good Luck'
# 인덱스 기반 원소값 변경 미지원 => 메서드 제공
# msg[0] = 'G'

# replace(이전문자열, 새로운문자열) 메서드      # 모든 문자열 변경됨
msg = "good luck " * 3
new_msg = msg.replace("g","G").replace("l", "L")
print(f"msg => {msg}")
print(f"new_msg => {new_msg}")

# replace(이전문자열, 새로운문자열, 개수) 메서드
msg = "good luck " * 3
new_msg = msg.replace("g","G", 1).replace("l", "L", 1)
print(f"msg => {msg}")
print(f"new_msg => {new_msg}")

# -------------------------
# [5] 1개의 str ---> 여러개 str 분리 : split 메서드
#   * 공백문자 기준으로 분리
#   * 메서드 사용 시 분리 기준 문자/문자열 설정 가능
#   * 리스트에 여러개 분리된 str 담아서 반환
# -------------------------
data = "Happy New Year 2026"

ret = data.split()
print(f"data : {data}, type(data) : {type(data)}, {len(data)}개")
print(f"ret : {ret}, type(ret) : {type(ret)}, {len(ret)}개")

ret = data.split("-")
print(f"\ndata : {data}, type(data) : {type(data)}, {len(data)}개")
print(f"ret : {ret}, type(ret) : {type(ret)}, {len(ret)}개")

# -------------------------
# [6] 여러개 str ---> 1개 str 연결 : join 메서드
#   * 연결문자 지정
# -------------------------
# => 여러개 str 분리
ret = data.split()

# => 1개 str 연결
new_data = "-".join(ret)
print(ret, new_data, sep="\n")
