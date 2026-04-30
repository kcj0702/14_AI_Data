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
DATA_FILE1 = '../DATA/iris.csv'
DATA_FILE2 = '../DATA/iris_no_columns.csv'
DATA_FILE3 = '../DATA/iris_space.csv'

# ----------------------------------------------------------------
# [2] CSV >>> DataFrame 로딩 및 기본 형태 확인
# ----------------------------------------------------------------
# DataFrame으로 로딩
iris_df = pd.read_csv(DATA_FILE1)

# 기본 정보 확인
print_df('첫 번째 줄 컬럼명 있는 CSV', iris_df)
print('컬럼이름 인덱스 ->', iris_df.columns)

# ----------------------------------------------------------------
# [3] CSV >>> DataFrame 로딩 및 기본 형태 확인
# ----------------------------------------------------------------
# DataFrame으로 로딩
# 첫 번째 줄이 데이터 ==> 컬럼명 없는 CSV 파일
# 설정 필요 : header 매개변수 = None
iris_df = pd.read_csv(DATA_FILE2, header=None)

# 기본 정보 확인
print_df('첫 번째 줄 데이터 존재 CSV', iris_df)
print('컬럼이름 인덱스 ->', iris_df.columns)

# 컬럼 이름 속성 설정
iris_df.columns = ['받침 길이', '받침 너비', '꽃잎 길이', '꽃잎 너비', '품종']
print(iris_df.head(2))

# ----------------------------------------------------------------
# [4] CSV >>> DataFrame 로딩 및 기본 형태 확인
# ----------------------------------------------------------------
# DataFrame으로 로딩
# 첫 번째 줄이 데이터 ==> 컬럼명 없는 CSV 파일 : header 매개변수 설정
# 데이터 구분 문자    ==> 공백 1개 : sep 매개변수 설정
# 설정 필요 : header 매개변수 = None
iris_df = pd.read_csv(DATA_FILE3, header=None, sep=' ')

# 기본 정보 확인
print_df('첫 번째 줄 데이터 + 구분자 공백 1개 CSV', iris_df)
print('컬럼이름 인덱스 ->', iris_df.columns)

# 컬럼 이름 속성 설정
iris_df.columns = ['받침 길이', '받침 너비', '꽃잎 길이', '꽃잎 너비', '품종']
print(iris_df.head(2))

# ----------------------------------------------------------------
# [5] CSV >>> DataFrame 로딩 및 기본 형태 확인
# ----------------------------------------------------------------
# DataFrame으로 로딩
# 첫 번째 줄이 데이터         ==> header 매개변수 설정
# 데이터 구분 문자            ==> sep 매개변수 설정
# 설정 필요 : header 매개변수 ==> index_col 매개변수 설정
# 특정 컬럼을 행 인덱스로 설정 후 로딩
iris_df = pd.read_csv(DATA_FILE3, header=None, sep=' ', index_col=3)

# 기본 정보 확인
print_df('첫 번째 줄 데이터 + 구분자 공백 1개 + 컬럼 행 인덱스 설정', iris_df)
print('컬럼이름 인덱스 ->', iris_df.columns)
print('행 인덱스 ->', iris_df.index)

# ----------------------------------------------------------------
# [6] CSV >>> DataFrame 로딩 및 기본 형태 확인
# ----------------------------------------------------------------
# DataFrame으로 로딩
iris_df = pd.read_csv(DATA_FILE1, usecols=[0, 1, 4])

# 기본 정보 확인
print_df('0, 1, 4번 컬럼만 추출', iris_df)
print('컬럼이름 인덱스 ->', iris_df.columns)
print('DF 형태 정보    ->', iris_df.shape)

# ----------------------------------------------------------------
# [7] CSV >>> DataFrame 로딩 및 기본 형태 확인
# ----------------------------------------------------------------
# DataFrame으로 로딩
# skipfooter 매개변수 : 아래쪽 지정된 개수 데이터 로딩 X
# skiprows   매개변수 : 앞쪽 지정된 개수 데이터 로딩 X
iris_df = pd.read_csv(DATA_FILE1, skipfooter=30, skiprows=10, header=None)

# 기본 정보 확인
print_df('skipfooter 일부 행 제외한 데이터 추출', iris_df)
print('컬럼이름 인덱스 ->', iris_df.columns)
print('DF 형태 정보    ->', iris_df.shape)

# ----------------------------------------------------------------
# [8] CSV >>> DataFrame 로딩 및 기본 형태 확인
# ----------------------------------------------------------------
# 날짜/시간 컬럼 존재하는 데이터 파일
DATA_FILE1 = '../DATA/sample_data.csv'

# DataFrame으로 로딩
# 첫 번째 줄 -> 컬럼이름 데이터 OK
# 구분자     -> 쉼표/콤마 OK
# 날짜/시간 컬럼 ==> datetime64[ns] 형변환 후 로딩 : parse_dates=[컬럼명] 매개변수
csv_df = pd.read_csv(DATA_FILE1, parse_dates=['date'])

# 기본 정보 확인
print_df('데이터 로딩', csv_df)
print('컬럼이름 인덱스 ->', csv_df.columns)
print('DF 형태 정보    ->', csv_df.shape)
print('DF 컬럼 타입    ->', csv_df.dtypes.to_dict())