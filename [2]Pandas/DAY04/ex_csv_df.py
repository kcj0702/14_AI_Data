# =========================================================
# CSV 데이터 파일 >>> DataFrame 변환 로딩
# =========================================================
# [1] 모듈 로딩
import pandas as pd

# [2] 데이터 준비
DATA_FILE = '../DATA/iris.csv'

# [3] CSV >>> DataFrame 변환 저장
iris_df = pd.read_csv(DATA_FILE)

# [4] DataFrame의 기본정보 확인
# 요약정보 출력
print("\n 요약 정보 ---")
iris_df.info()

# => 실제 데이터 확인
print("\n실제 데이터 ---\n", iris_df.head(2), iris_df.tail(2), sep='\n')

# => 컬럼별 통계 정보 확인
print("\n수치 컬럼별 정보 ---\n", iris_df.describe(), sep='\n')
print("\n모든 컬럼별 정보 ---\n", iris_df.describe(include='all'), sep='\n')

# => describe()/head()/tail() 메서드 결과는 저장 후 활용 가능
desc_df = iris_df.describe()
print(type(desc_df), desc_df, desc_df.columns, sep='\n')