# ====================================================================
# 반복가능한 타입의 원소에 인덱스를 제공해주는 내장함수
# * enumerate()
# * 사용 : for ~ in 반복문에서 요소/원소 인덱스 필요한 경우 사용
# ====================================================================
datas = ['Good', 2026, 'Happy', '좋은날']

# 원소 중 str 타입이 아닌 것은 str 타입으로 변환 후 저장
# for d in datas:
#     if not isinstance(d, str):
#         str(d)

for idx in range(len(datas)):
    if not isinstance(datas[idx], str):
        datas[idx] = str(datas[idx])

# for ~ in 반복에서 원소의 번호를 부여하는 내장함수
for cnt, d in enumerate(datas):
    if not isinstance(d, str):
        datas[cnt] = d

# print(isinstance(2026, str))
# print(isinstance(2026, int))
# print('int' in str(type(2026)))
# print('str' in str(type(2026)))