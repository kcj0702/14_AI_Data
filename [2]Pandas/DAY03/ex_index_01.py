# ============================================================
#             인덱스 관련 메서드들 (1) set_index()
# ------------------------------------------------------------
# 인덱스 목적 : 1행/관측값 추출하기 위한 용도
#               유일한 값, 반드시 값이 존재해야함
# ============================================================
# [1] 모듈 로딩
import pandas as pd

# [2] DataFrame 인스턴스 생성
data = {'A':[10, 20, 30],
        'B':[ 8, 11,  7],
        'C':[ 9,  5,  8],
        'D':[11,  7,  4]}

df = pd.DataFrame(data)
print("====== df ======", df, sep='\n')

# [3] 특정 컬럼 => 행 인덱스로 설정
#     df.set_index(컬럼)
cdf = df.set_index('A')
print("\n====== df ======", df, sep='\n')
print("\n====== cdf ======", cdf, sep='\n')
print("새 인덱스", cdf.index)
print("0번 원소\n", cdf.loc[10], sep='')

# => df.set_index([컬럼, 컬럼...])
# => 멀티인덱스
cdf = df.set_index(['A', 'B'])
print("\n====== df ======", df, sep='\n')
print("\n====== cdf ======", cdf, sep='\n')
print(cdf.index)
print("0번 원소\n", cdf.loc[(10, 8)], sep='')