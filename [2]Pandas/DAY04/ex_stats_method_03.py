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
# => 상관계수 계산 후 DataFrame 반환 : corr()
# => 수치 데이터 기반 계산
# => 컬럼들의 관계성을 -1 ~ 1 범위로 반환
# => 목적
#    * 주제와 관련된 변수/속성/컬럼 여부 검사용
#    * 선택된 변수/속성/컬럼 중 비슷한 속성들 필터링용
corr_df = iris_df.corr(numeric_only=True)
print(f"corr_sr => \n{corr_df}")

# 타겟/주제에 해당하는 컬럼만 추출
print(corr_df['petal.length'].abs().sort_values(ascending=False))