# ==================================================
# 결측치 처리 - 치환
# --------------------------------------------------
# DataFrame.fillna()
# 
# ==================================================
# 모듈 로딩
import sys
sys.path.append(r'C:\Users\KDT013\14_AI_Data\[2]Pandas\User_Module')
import utils
import pandas as pd
import numpy as np 

# DF 생성
df = pd.DataFrame( [[np.nan, 2, np.nan, 0], 
                    [3, 4, np.nan, 1], 
                    [np.nan, np.nan, np.nan, np.nan], 
                    [np.nan, 3, np.nan, 4]], 
                    columns=list("ABCD")) 
# DF 출력
utils.data_info(df)

# --------------------------------------------------
# 결측치 치환 : fillna()
# --------------------------------------------------
# [1] 기본 설정값으로 결측치 치환
print(df)
print(f"\n[모든 결측치 0으로 채우기] df.fillna(0) ===\n{df.fillna(0)}")

# [2] 컬럼마다 특정 값으로 결측치 채우기
print(df)
print(f"\n[컬럼마다 특정 값으로 결측치 채우기] df.fillna() ===\n{df.fillna({'A':7, 'B':0, 'C':90, 'D':-1})}")

# [3] 이전 행의 값으로 결측치 채우기
print(df)
print(f"\n[이전 행의 값으로 결측치 채우기] df.ffill() ===\n{df.ffill()}")

# [4] 다음 행의 값으로 결측치 채우기
print(df)
print(f"\n[다음 행의 값으로 결측치 채우기] df.ffill() ===\n{df.bfill()}")

print(df)
print(f"\n[다음 열의 값으로 결측치 채우기] df.ffill(axis=1) ===\n{df.bfill(axis=1)}")

print(df)
print(f"\n[보간법으로 결측치 채우기] df.ffill(axis=1) ===\n{df.interpolate('linear')}")
print(f"\n[보간법으로 결측치 채우기] df.ffill(axis=1) ===\n{df.interpolate('linear', limit_direction='both')}")
