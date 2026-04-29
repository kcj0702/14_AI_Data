# =========================================================
# 통계 관련 메서드들
# =========================================================
# [1] 모듈 로딩
import sys
sys.path.append(r'C:\Users\KDT013\14_AI_Data\[2]Pandas\User_Module')
import utils
import pandas as pd

# [2] 데이터 준비
DATA_FILE = '../DATA/iris.csv'

# [3] CSV >>> DataFrame 변환 저장
iris_df = pd.read_csv(DATA_FILE)

# [4] DataFrame의 기본정보 확인
utils.data_info(iris_df)

# => describe()/head()/tail() 메서드 결과는 저장 후 활용 가능
desc_df = iris_df.describe()
print(type(desc_df), desc_df, desc_df.columns, sep='\n')

# [5] 통계 관련 메서드들
# => DataFrame에 전체 컬럼별 데이터 수 반환 : count()
#    axis=0 : 각각의 행 단위 계산 => 결과 열
#    axis=1 : 각각의 열 단위 계산 => 결과 행
cnt_sr = iris_df.count()
print(f"axis=0 각 컬럼의 NA가 아닌 데이터 수 cnt_sr : \n{cnt_sr}")

cnt_sr = iris_df.count(axis=1)
print(f"axis=1 각 로우의 NA가 아닌 데이터 수 cnt_sr : \n{cnt_sr}")

# => 행의 모든 값이 동일한 개수 반환 : value_counts()
vcnt_sr = iris_df.value_counts()
print(f"{vcnt_sr}")

# => 특정 컬럼의 데이터 개수 반환 : value_counts()
vcnt_sr = iris_df.variety.value_counts()
vcnt_sr = iris_df['variety'].value_counts()
print(f"{vcnt_sr}")

vcnt_sr = iris_df['petal.width'].value_counts()
print(f"{vcnt_sr}")

# => 컬럼별 데이터/값의 종류 개수 즉, 고유값 반환 : unique()
# => DataFrame에는 없음 Series.unique()
# variety 컬럼의 데이터/값의 종류 => 고유값
ret = iris_df['variety'].unique()
print(f"variety 컬럼의 고유값 : {ret}, 원소 개수 : {len(iris_df['variety'])}개")
print(f"variety 컬럼의 고유값별 원소 개수 : \n{iris_df['variety'].value_counts()}개")

ret = iris_df['petal.width'].unique()
print(f"petal.width 컬럼의 고유값 : {ret}, 원소 개수 : {len(iris_df['petal.width'])}개")
print(f"petal.width 컬럼의 고유값별 원소 개수 : \n{iris_df['petal.width'].value_counts()}개")