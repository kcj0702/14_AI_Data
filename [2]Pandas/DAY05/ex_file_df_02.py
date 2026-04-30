# ================================================================
#               File ===> DataFrame으로 변환 로딩
# 
# 관련 함수들 : pandas.read_파일포맷()
#               pandas.read_csv() / .read_excel() / .read_json()
# ================================================================
# [기억] DataFrame = 행인덱스 + 열이름인덱스 + 데이터
# [규칙] 파일의 첫 번째 줄의 데이터 ==> 열이름/컬럼이름으로 설정
# ================================================================
# ----------------------------------------------------------------
# [1] 모듈 로딩 및 데이터 선정
# ----------------------------------------------------------------
import pandas as pd
import sys
sys.path.append(r'C:\Users\KDT013\14_AI_Data\[2]Pandas\User_Module')
from utils import *

# 데이터 파일
DATA_FILE1 = '../DATA/학생관리부.xlsx'

# ----------------------------------------------------------------
# [2] CSV >>> DataFrame 로딩 및 기본 형태 확인
# ----------------------------------------------------------------
# DataFrame으로 로딩
excel_df = pd.read_excel(DATA_FILE1, header=2)      # 0, 1번 행 자동 버려짐

# 기본 정보 확인
print_df('특정 행 header 설정', excel_df)
print('컬럼이름 인덱스 ->', excel_df.columns)

# ----------------------------------------------------------------
# [3] CSV >>> DataFrame 로딩 및 기본 형태 확인
# ----------------------------------------------------------------
# DataFrame으로 로딩
# 특정 컬럼 => 행 인덱스 설정 : index_col 매개변수
excel_df = pd.read_excel(DATA_FILE1, header=2, index_col='이름')      # 0, 1번 행 자동 버려짐

# 기본 정보 확인
print_df('특정 행 header 설정', excel_df)
print('컬럼이름 인덱스 ->', excel_df.columns)

# ----------------------------------------------------------------
# [4] CSV >>> DataFrame 로딩 및 기본 형태 확인
# ----------------------------------------------------------------
# DataFrame으로 로딩
# 엑셀 파일에서 로딩할 시트 설정 : sheet_name = 정수/문자열
# excel_df = pd.read_excel(DATA_FILE1, header=2, sheet_name=1, usecols=[1, 2, 3, 4, 5, 6])
excel_df = pd.read_excel(DATA_FILE1, header=2, sheet_name=1, usecols=range(1,7))

# 기본 정보 확인
print_df('두 번째 시트 설정', excel_df)
print('컬럼이름 인덱스 ->', excel_df.columns)
print('행 인덱스 ->', excel_df.index)
