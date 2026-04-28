# ========================================================================
# DataFrame에서 행/열 선택
# ========================================================================
# [1] 모듈 로딩
import pandas as pd

# [2] DataFrame 인스턴스 생성
dataDF1 = pd.DataFrame([[10, 20, 30, 40.],
                        [11, 22, 33, 44.]])

dataDF2 = pd.DataFrame([[10, 20, 30, 40.], [11, 22, 33, 44.]], columns=['영', '일', '이', '삼'], index=['row0', 'row1'])

# => 생성된 인스턴스 확인
print("\n=== dataDF1\n", dataDF1)
print("\n=== dataDF1\n", dataDF2)

# [3] 행 선택 ------------------------------------------------------------
# [3-1] 1개 행 선택
one_row = dataDF2.iloc[0]
print("\n=== one_row", one_row, sep='\n')

# [3-2] 2개 이상 행 선택 - 인덱스 리스트
two_row = dataDF2.iloc[[0, 1]]
print("\n=== two_row", two_row, sep='\n')

two_row = dataDF2.loc[['row0', 'row1']]
print("\n=== two_row", two_row, sep='\n')

# [3-3] 2개 이상 행 선택 - 인덱스 슬라이싱
two_row = dataDF2.iloc[0 : 1]
print("\n=== two_row", two_row, sep='\n')

two_row = dataDF2.loc['row0' : 'row1']
print("\n=== two_row", two_row, sep='\n')

