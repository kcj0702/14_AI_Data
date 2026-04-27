import pandas as pd

# 문제 1. Series 생성하기
# 다음 데이터를 이용하여 score라는 이름의 Series를 생성하세요.
# 인덱스는 학생 이름으로 지정하세요.
# 학생 점수
# 김민수 85
# 이서연 92
# 박지훈 78
# 최유진 95
score = pd.Series({'김민수':85, '이서연':92, '박지훈':78, '최유진':95}, dtype='int8')

# 문제 2. Series 속성 출력하기
# 문제 1에서 만든 score Series를 이용하여 다음 내용을 출력하세요.
# 1. Series의 값만 출력하세요.
print(score.values)
# 2. Series의 인덱스만 출력하세요.
print(score.index)
# 3. Series의 데이터 타입을 출력하세요.
print(score.dtype)
# 4. Series의 크기를 출력하세요.
print(score.shape)
# 5. Series의 차원을 출력하세요.
print(score.ndim)

# 문제 3. Series 원소 1개 선택하기
# 문제 1에서 만든 score Series에서 다음 값을 출력하세요.
# 1. 김민수의 점수를 출력하세요.
print(score['김민수'])
# 2. 최유진의 점수를 출력하세요.
print(score['최유진'])
# 3. 위치 기준으로 첫 번째 학생의 점수를 출력하세요.
print(score.iloc[0])
# 4. 위치 기준으로 마지막 학생의 점수를 출력하세요.
print(score.iloc[len(score)-1])

# 문제 4. Series 원소 여러 개 선택하기
# 문제 1에서 만든 score Series에서 다음 학생들의 점수를 선택하세요.
# 1. 김민수, 박지훈의 점수를 출력하세요.
print(score[['김민수', '박지훈']])
# 2. 이서연, 최유진의 점수를 출력하세요.
print(score[['이서연', '최유진']])
# 3. 위치 기준으로 첫 번째, 두 번째 학생의 점수를 출력하세요.
print(score.iloc[[0, 1]])
# 4. 위치 기준으로 두 번째 학생부터 마지막 학생까지의 점수를 출력하세요.
print(score.iloc[1:])

# 문제 5. DataFrame 생성하기
# 다음 데이터를 이용하여 students라는 이름의 DataFrame을 생성하세요.
# 딕셔너리를 사용하여 DataFrame을 생성하세요.
# 이름 나이 국어 영어 수학
# 김민수 20 85 90 88
# 이서연 21 92 87 95
# 박지훈 20 78 80 76
# 최유진 22 95 93 97
data = {'이름': ['김민수', '이서연', '박지훈', '최유진'], 
        '나이': [20, 21, 20, 22],
        '국어': [85, 92, 78, 95],
        '영어': [90, 87, 80, 93],
        '수학': [88, 95, 76, 97]}
students = pd.DataFrame(data)

# 문제 6. DataFrame 속성 출력하기
# 문제 5에서 만든 students DataFrame을 이용하여 다음 내용을 출력하세요.
# 1. 전체 데이터를 출력하세요.
print(students)
# 2. 행과 열의 개수를 출력하세요.
print(students.shape)
# 3. 컬럼 이름을 출력하세요.
print(students.columns)
# 4. 인덱스를 출력하세요.
print(students.index)
# 5. 각 열의 데이터 타입을 출력하세요.
print(students.dtypes)
# 6. 전체 데이터 개수를 출력하세요.
print(students.size)
# 7. 차원을 출력하세요.
print(students.ndim)

# 문제 7. DataFrame 열 1개 선택하기
# students DataFrame에서 다음 열을 선택하여 출력하세요.
# 1. 이름 열을 출력하세요.
print(students['이름'])
# 2. 국어 열을 출력하세요.
print(students['국어'])
# 3. 수학 열을 출력하세요.
print(students['수학'])

# 문제 8. DataFrame 열 여러 개 선택하기
# students DataFrame에서 다음 열들을 선택하여 출력하세요.
# 1. 이름, 나이 열을 출력하세요.
print(students[['이름', '나이']])
# 2. 이름, 국어, 영어 열을 출력하세요.
print(students[['이름', '국어', '영어']])
# 3. 국어, 영어, 수학 열을 출력하세요.
print(students[['국어', '영어', '수학']])

# 문제 9. DataFrame 행 1개 선택하기
# students DataFrame에서 위치 기준으로 다음 행을 선택하세요.
# 1. 첫 번째 행을 출력하세요.
print(students.iloc[0])
# 2. 두 번째 행을 출력하세요.
print(students.iloc[1])
# 3. 마지막 행을 출력하세요.
print(students.iloc[len(students.index)-1])

# 문제 10. DataFrame 행 여러 개 선택하기
# students DataFrame에서 위치 기준으로 다음 행들을 선택하세요.
# 1. 첫 번째 행부터 두 번째 행까지 출력하세요.
print(students.iloc[0:2])
# 2. 두 번째 행부터 마지막 행까지 출력하세요.
print(students.iloc[1:])
# 3. 첫 번째 행과 세 번째 행을 출력하세요.
print(students.iloc[[0, 3]])

# 문제 11. DataFrame 행 선택하기
# students DataFrame에서 이름 열을 인덱스로 설정한 새로운 DataFrame을 만드세요.
# 그다음 새로운 DataFrame에서 다음 행을 선택하세요.
idx = data['이름']
del data['이름']
students_new = pd.DataFrame(data, index=idx)

# 1. 김민수 행을 출력하세요.
print(students_new.loc['김민수'])
# 2. 최유진 행을 출력하세요.
print(students_new.loc['최유진'])
# 3. 김민수, 박지훈 행을 출력하세요.
print(students_new.loc[['김민수', '박지훈']])
# 4. 이서연부터 최유진까지 출력하세요.
print(students_new.loc['이서연':'최유진'])

# 문제 12. DataFrame에서 특정 행과 열 선택하기
# 이름 열을 인덱스로 설정한 DataFrame을 이용하여 다음 값을 출력하세요.
# 1. 김민수의 국어 점수를 출력하세요.
print(students_new.loc['김민수']['국어'])
# 2. 이서연의 수학 점수를 출력하세요.
print(students_new.loc['이서연']['수학'])
# 3. 박지훈의 영어 점수를 출력하세요.
print(students_new.loc['박지훈']['영어'])
# 4. 최유진의 나이를 출력하세요.
print(students_new.loc['최유진']['나이'])

# 문제 13. DataFrame에서 여러 행과 여러 열 선택하기
# 이름 열을 인덱스로 설정한 DataFrame을 이용하여 다음 데이터를 선택하세요.
# 1. 김민수, 이서연의 국어와 영어 점수를 출력하세요.
print(students_new.loc[['김민수', '이서연']][['국어', '영어']])
# 2. 박지훈, 최유진의 영어와 수학 점수를 출력하세요.
print(students_new.loc[['박지훈', '최유진']][['영어', '수학']])
# 3. 전체 학생의 국어, 영어, 수학 점수를 출력하세요.
print(students_new[['국어', '영어', '수학']])
# 4. 김민수부터 박지훈까지의 나이와 국어 점수를 출력하세요.
print(students_new.loc['김민수':'박지훈'][['나이', '국어']])

# 문제 14. DataFrame에서 특정 위치의 값 선택하기
# students DataFrame을 이용하여 위치 기준으로 다음 값을 출력하세요.
# 선택할 값                     설명
# 첫 번째 학생의 이름           0행 0열
print(students.iloc[0].iloc[0])
# 두 번째 학생의 영어 점수      1행 3열
print(students.iloc[1].iloc[3])
# 세 번째 학생의 수학 점수      2행 4열
print(students.iloc[2].iloc[4])
# 네 번째 학생의 나이           3행 1열
print(students.iloc[3].iloc[1])

# 문제 15. 종합 문제
# 다음 데이터를 이용하여 products DataFrame을 생성한 뒤, 아래 문제를 해결하세요.
# 상품명    가격        재고    카테고리
# 노트북    1200000     5       전자제품
# 마우스    25000       30      전자제품
# 의자      85000       12      가구
# 책상      150000      7       가구
# 키보드    45000       20      전자제품
product_data = {'상품명': ['노트북', '마우스', '의자', '책상', '키보드'],
                '가격': [1200000, 25000, 85000, 150000, 45000],
                '재고': [5, 30, 12, 7, 20],
                '카테고리': ['전자제품', '전자제품', '가구', '가구', '전자제품']}
products = pd.DataFrame(product_data)

# 1. 전체 DataFrame을 출력하세요.
print(products)
# 2. DataFrame의 행과 열 개수를 출력하세요.
print(f'행 : {products.shape[0]}, 열 : {products.shape[1]}')
# 3. 컬럼 이름을 출력하세요.
print(products.columns)
# 4. 상품명 열만 출력하세요.
print(products['상품명'])
# 5. 상품명, 가격 열을 출력하세요.
print(products[['상품명', '가격']])
# 6. 첫 번째 행을 출력하세요.
print(products.iloc[0])
# 7. 마지막 행을 출력하세요.
print(products.iloc[len(products.index)-1])
# 8. 두 번째 행부터 네 번째 행까지 출력하세요.
print(products.iloc[1:4])
# 9. 상품명을 인덱스로 설정한 products2를 만드세요.
idx = product_data['상품명']
del product_data['상품명']
products2 = pd.DataFrame(product_data, index=idx)
# 10. products2에서 노트북 행을 출력하세요.
print(products2.loc['노트북'])
# 11. products2에서 마우스의 가격을 출력하세요.
print(products2.loc['마우스']['가격'])
# 12. products2에서 의자, 책상의 가격과 재고를 출력하세요.
print(products2.loc[['의자', '책상']][['가격', '재고']])