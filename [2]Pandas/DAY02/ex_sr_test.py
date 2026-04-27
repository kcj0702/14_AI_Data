# =============================================================
#                 Series 인스턴스 생성 및 이해
# =============================================================
# 데이터
data = ['Google', 1995, 'USA', True]

import pandas as pd
# [1] 위 데이터를 Series로 저장하세요
sr = pd.Series(data)
print(sr)

# [2] 생성된 Series 객체의 기본 속성 즉,
#     index, values, dtype, shape, ndim 값을 출력하세요.
print(f"sr.index : {sr.index}, sr.values : {sr.values}, sr.dtype : {sr.dtype}, sr.shape : {sr.shape}, sr.ndim : {sr.ndim}")

# [3] 생성된 Series 객체의 인덱스를 사명, 창립년도, 위치, 대기업여부로
#     변경해주세요.
sr.index = ['사명', '창립년도', '위치', '대기업여부']
print(sr)

# [4] 생성된 Series 객체에서 1995 데이터만 추출해서 출력하세요.
print(f"창립년도 : {sr['창립년도']}년")

# [5] 생성된 Series 객체에서 사명, 창립년도, 위치를 출력하세요.
# [5-1] 리스트 방식
print(sr[['사명', '창립년도', '위치']])

# [5-2] 슬라이싱 방식
print(sr["사명" : "위치"])