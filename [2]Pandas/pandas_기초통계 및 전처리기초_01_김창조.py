# ==============================================
#      Pandas 기초 통계 함수 + 결측치 + 중복값 처리 실습 문제 [1]
# ==============================================

# [사용 데이터 파일]
# - vgsales.csv

# [학습 범위]
# - 데이터 기본 확인
# - 기초 통계 함수
# - 결측치 확인 및 처리
# - 중복값 확인 및 처리
# - 정렬
# - 인덱스 정리

import pandas as pd
import numpy as np

num = 0
def split():
    global num
    num += 1
    print(f"{f' 문제 {num:0>2}번 ':-^90}")

# ==============================================
# 문제 1) vgsales.csv 파일을 읽어 DataFrame df를 생성하세요.
# ==============================================
split()
df = pd.read_csv('./DATA/vgsales.csv')
print(df.head(3))

# ==============================================
# 문제 2) df의 앞 5행과 마지막 2행 출력하세요.
# ==============================================
split()
print(df.head())
print(df.tail(2))

# ==============================================
# 문제 3) df의 행 개수와 열 개수를 확인하세요.
# 출력 예시:
# 행 개수:
# 열 개수:
# ==============================================
split()
print(f"행 개수: {df.shape[0]}")
print(f"열 개수: {df.shape[1]}")

# ==============================================
# 문제 4) df의 전체 정보를 확인하세요.
# ==============================================
split()
df.info()

# ==============================================
# 문제 5) df의 숫자형 컬럼에 대한 기초 통계 정보를 출력하세요.
# ==============================================
split()
print(df.describe(include='number'))

# ==============================================
# 문제 6) Global_Sales 컬럼의 평균값/최소값/최대값/중앙값/전체합계 
#           계산 후 출력하세요.
# ==============================================
split()
print(f"평균값 : {df['Global_Sales'].mean()}\n최소값 : {df['Global_Sales'].min()}\n최대값 : {df['Global_Sales'].max()}\n중앙값 : {df['Global_Sales'].mode()[0]}\n전체합계 : {df['Global_Sales'].sum()}")

# ==============================================
# 문제 7) Global_Sales 컬럼의 데이터 개수를 구하세요.
# ==============================================
split()
print('Global_Sales의 데이터 개수 :', df['Global_Sales'].size)

# ==============================================
# 문제 8) Year 컬럼의 평균값/중앙값/최빈값 구하세요.
# ==============================================
split()
print(f"Year 컬럼의 평균값 / 중앙값 / 최빈값 : {df['Year'].describe().loc['mean']} / {df['Year'].describe().loc['50%']} / {df['Year'].mode()[0]}")

# ==============================================
# 문제 9) Genre 컬럼에 어떤 장르 값들이 있는지 중복 없이 출력하세요.
# ==============================================
split()
print('Genre 컬럼의 종류', *list(df['Genre'].value_counts().index))

# ==============================================
# 문제 10) Genre 컬럼의 고유값 개수를 구하세요.
# ==============================================
split()
print('Genre 컬럼의 고유값 개수\n', df['Genre'].value_counts())

# ==============================================
# 문제 11) 전체 데이터에 결측치가 있는지 True/False 형태로 확인하세요.
# ==============================================
split()
print(df.isna())

# ==============================================
# 문제 12) 컬럼별 결측치 개수를 출력하세요.
#             전체 결측치 개수를 구하세요.
# ==============================================
split()
print('컬럼별 결측치 개수', df.isna().sum(), sep='\n')
print('전체 결측치 개수 :', df.isna().sum().sum())

# ==============================================
# 문제 13) 각 컬럼에 결측치가 전혀 없는지 확인하세요.
# ==============================================
split()
print('컬럼별 결측치가 전혀 없는지 여부 :', df.isna().sum() == 0, sep='\n')

# ==============================================
# 문제 14) 결측치가 하나라도 있는 행을 삭제한 후 df_drop 변수에 
#            저장하세요.
# ==============================================
split()
df_drop = df.dropna(how='any')
print(df_drop.head(3))

# ==============================================
# 문제 15) 결측치 삭제 전과 삭제 후의 행 개수를 비교하세요.
# 출력 예시:
# 삭제 전 행 개수:
# 삭제 후 행 개수:
# 삭제된 행 개수:
# ==============================================
split()
print('삭제 전 행 개수:', df.shape[0], '개')
print('삭제 후 행 개수:', df_drop.shape[0], '개')
print('삭제된 행 개수:', df.shape[0] - df_drop.shape[0], '개')

# ==============================================
# 문제 16) Publisher 컬럼의 결측치를 "Unknown"으로 채운 후 
#            df_fill_pub 변수에 저장하세요.
# ==============================================
split()
df_fill_pub = df['Publisher'].fillna("Unknown")
print(df_fill_pub.head())

# ==============================================
# 문제 17) Publisher 컬럼의 결측치가 제대로 처리되었는지 확인하세요.
# 출력 예시:
# 처리 전 Publisher 결측치 개수:
# 처리 후 Publisher 결측치 개수:
# ==============================================
split()
print('처리 전 Publisher 결측치 개수:', df['Publisher'].isna().sum(), '개')
print('처리 후 Publisher 결측치 개수:', df_fill_pub.isna().sum(), '개')

# ==============================================
# 문제 18) Year 컬럼의 결측치를 Year 컬럼의 평균값으로 채우세요.
# [조건] 평균값은 정수로 변환해서 사용하세요.
# ==============================================
split()
idx_NA = df['Year'][df['Year'].isna()].index
print(df.loc[idx_NA, 'Year'])
print(df.loc[idx_NA, 'Year'].fillna(int(df['Year'].mean())))

# ==============================================
# 문제 19) Year 컬럼의 결측치를 Year 컬럼의 중앙값으로 채우세요.
# [조건] 중앙값은 정수로 변환해서 사용하세요.
# ==============================================
split()
print(df.loc[idx_NA, 'Year'].fillna(int(df['Year'].median())))

# ==============================================
# 문제 20) Year 컬럼의 결측치를 Year 컬럼의 최빈값으로 채우세요.
# ==============================================
split()
print(df.loc[idx_NA, 'Year'].fillna(int(df['Year'].mode()[0])))

# ==============================================
# 문제 21) Year와 Publisher 컬럼의 결측치를 모두 처리한 df_fill 변수 만들기
# [조건]
# 1. 원본 df를 복사해서 사용하기
# 2. Publisher 결측치는 "Unknown"으로 채우기
# 3. Year 결측치는 최빈값으로 채우기
# ==============================================
split()
idx_NA_P = list(df['Publisher'][df['Publisher'].isna()].index)
idx_NA_Y = list(df['Year'][df['Year'].isna()].index)
print(df.loc[idx_NA_P + idx_NA_Y].head(5))

print()

df_fill = df.copy()
df_fill['Publisher'] = df_fill['Publisher'].fillna("Unknown")
df_fill['Year'] = df_fill['Year'].fillna(df_fill['Year'].mode()[0])
print(df_fill.loc[idx_NA_P + idx_NA_Y].head(5))

# ==============================================
# 문제 22) 전체 행 기준으로 중복 데이터가 있는지 확인하세요.
#            전체 행 기준 중복 데이터 개수를 구하세요.
# ==============================================
split()
print(df[df.duplicated(keep=False)])
print('전체 행 기준 중복 데이터 개수 :', df.duplicated().sum())

# ==============================================
# 문제 23) Name 컬럼 기준으로 중복된 데이터가 있는지 확인하세요.
#             Name 컬럼 기준으로 중복된 데이터 개수를 구하세요.
# ==============================================
split()
print(df['Name'][df['Name'].duplicated(keep=False)])
print('Name 컬럼 기준으로 중복된 데이터 개수 :', df['Name'].duplicated().sum())

# ==============================================
# 문제 24) Name, Platform, Year 컬럼을 기준으로 중복 여부를 확인하세요.
#             Name, Platform, Year 기준으로 중복된 데이터 개수를 구하세요.
# ==============================================
split()
print(df[df[['Name', 'Platform', 'Year']].duplicated(keep=False)])
print('Name, Platform, Year 기준으로 중복된 데이터 개수 :', df[['Name', 'Platform', 'Year']].duplicated().sum())

# ==============================================
# 문제 25) 전체 행 기준으로 중복을 제거한 후 df_no_dup_all 변수에 저장하세요.
#            전체 행 기준 중복 제거 전후의 행 개수를 비교하세요.

# 출력 예시:
# 중복 제거 전 행 개수:
# 중복 제거 후 행 개수:
# 제거된 행 개수:
# ==============================================
split()
df_no_dup_all = df.drop_duplicates()
print('중복 제거 전 행 개수:', len(df), '개')
print('중복 제거 후 행 개수:', len(df_no_dup_all), '개')
print('제거된 행 개수:', len(df) - len(df_no_dup_all), '개')

# ==============================================
# 문제 26) Name 컬럼 기준으로 중복을 제거한 후 df_no_dup_name 변수에 저장하세요.
#            Name, Platform, Year 기준으로 중복을 제거한 후 df_no_dup_game 변수에 저장하세요.
# ==============================================
split()
df_no_dup_name = df.drop_duplicates(subset='Name')
print('Name 컬럼 기준으로 중복된 데이터 개수 :', df['Name'].duplicated().sum())
df_no_dup_game = df.drop_duplicates(subset=['Name', 'Platform', 'Year'])
print('Name, Platform, Year 기준으로 중복된 데이터 개수 :', df[['Name', 'Platform', 'Year']].duplicated().sum())

# ==============================================
# 문제 27) Name, Platform, Year 기준으로 중복 제거 후 인덱스를 0부터 다시 설정하세요.
# ==============================================
split()
df_no_dup_name.reset_index(drop=True, inplace=True)
df_no_dup_game.reset_index(drop=True, inplace=True)
print(df_no_dup_name.tail(3))
print()
print(df_no_dup_game.tail(3))

# ==============================================
# 문제 28) 중복 제거 전후의 인덱스 차이를 확인하세요.
# ==============================================
split()
print('원본 df의 인덱스 범위 :', df.index, end='\n\n')
print('df_no_dup_name의 인덱스 범위 :', df_no_dup_name.index, end='\n\n')
print('df_no_dup_game의 인덱스 범위 :', df_no_dup_game.index, end='\n\n')