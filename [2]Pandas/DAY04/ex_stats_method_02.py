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
# utils.data_info(iris_df)

# [5] 통계 관련 메서드들
# 평균, 중앙값, 최빈값, 최소, 최대, 표준편차
mean_sr = iris_df.mean(numeric_only=True)
print(f"mean_sr => \n{mean_sr}")

median_sr = iris_df.median(numeric_only=True)
print(f"median_sr => \n{median_sr}")

mode_sr = iris_df.mode(numeric_only=True)
print(f"mode_sr => \n{mode_sr}")

min_sr = iris_df.min(numeric_only=True)
print(f"min_sr => \n{min_sr}")

max_sr = iris_df.max(numeric_only=True)
print(f"max_sr => \n{max_sr}")

std_sr = iris_df.std(numeric_only=True)
print(f"std_sr => \n{std_sr}")

# => 상관계수 계산 후 DataFrame
# => 
corr_df = iris_df.corr(numeric_only=True)
print(f"corr_sr => \n{corr_df}")