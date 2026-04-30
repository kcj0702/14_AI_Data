# ==================================================
# 중복데이터 검사 및 처리
# --------------------------------------------------
# -> 검사 : DataFrame.duplicated() True/False 반환
# -> 처리 : DataFrame.drop_duplicates()
# ==================================================
# 모듈 로딩
import sys
sys.path.append(r'C:\Users\KDT013\14_AI_Data\[2]Pandas\User_Module')
import utils
import pandas as pd
import numpy as np 

# DF 생성
df = pd.DataFrame({'brand' : [ 'Yum', 'Yum', 'Indo', 'Indo', 'Indo' ], 
                   'style' : [ 'cup', 'cup', 'cup', 'pack', 'pack' ], 
                   'rating' : [4, 4, 3.5, 15, 5]})
# DF 출력
utils.data_info(df)

# --------------------------------------------------
# 중복 데이터 검사
# --------------------------------------------------
# => 행 단위로 중복 여부 검사 후 True/False 반환
dup_df = df.duplicated()

print(dup_df)

# => 중복 데이터 개수 확인
print(dup_df.sum())

# --------------------------------------------------
# 중복 데이터 처리 => 삭제
# --------------------------------------------------
print(df)
print(f"\n[중복 데이터 삭제] df.drop_duplicates() ===\n{df.drop_duplicates()}")

print(df)
print(f"\n[중복 데이터 삭제] df.drop_duplicates('brand') ===\n{df.drop_duplicates(subset='brand')}")