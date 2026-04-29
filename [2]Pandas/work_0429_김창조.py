def line(txt):
    a = ' ' + txt + ' '
    print(f"{a:=^60}")
# ======================================
# Part 3. 데이터 살펴보기 예제 
line('Part 3. 데이터 살펴보기 예제')

import pandas as pd
df = pd.DataFrame({'brand' : [ 'Yum', 'Yum', 'Indo', 'Indo', 'Indo' ], 
                   'style' : [ 'cup', 'cup', 'cup', 'pack', 'pack' ], 
                   'rating' : [4, 4, 3.5, 15, 5]})
print(df.describe(include='all'))
print(df.describe(include='object'))
print(df.describe(include='number'))
print(df.describe(include=['number', 'object']))

print(df['brand'].value_counts(normalize=True))

print(df.mean(numeric_only=True))

print("="*69)
# ======================================
# Part 5. 누락 데이터 처리 예제
line('Part 5. 누락 데이터 처리 예제')

df = pd.read_csv(r'C:\Users\KDT013\14_AI_Data\[2]Pandas\DATA\weather.csv')
print(df.head())

print(df['d1'].value_counts(dropna=False))
print(df.isnull().sum())

ser1 = pd.Series([1, 2, None])
print(ser1)     # dtype이 float64로 변환됨(NaN 때문)

ser1 = pd.Series([1, 2, None], dtype='Int64')
print(ser1)     # None이 NA로 처리되며, dtype이 Int64로 유지

print(df.dropna(axis=1, thresh=3))

print(df.dropna(axis=1, subset=3, how='any'))

print(df['d1'].fillna(df['d1'].mean()))

# print(df.value_counts(dropna=False).idxmax())     # 고유값이 인덱스명인 데이터 시리즈의 최대값의 인덱스 반환 => 최빈값

print(df.mode().loc[0, 'd1'])                       # 빈도로 정렬된 df에서 d1열의 최빈값

print(df.mode().ffill(axis=0))                      # 행 방향으로 행 전체 데이터 값의 결측값을 가장 드물게 나온 값으로 바꿈


print("="*69)
# ======================================
# Part 5. 누락 데이터 처리 예제
line('Part 5. 누락 데이터 처리 예제')

df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                   'c2':[1, 1, 1, 2, 2],
                   'c3':[1, 1, 2, 2, 2]})
print(df.duplicated())                              # 0행이 1행과 완전히 같음 => True

print(df.duplicated(keep='last'))

print(df.duplicated(keep=False))                    # 중복인 모든 행을 True

print(df.duplicated(subset='c2'))                   # df['c2'].duplicated()

print(df.drop_duplicates())

print(df.drop_duplicates(keep='last'))

print(df.drop_duplicates(keep=False))

print(df.drop_duplicates(subset=['c2', 'c3'], keep=False))

print("="*69)
# ======================================