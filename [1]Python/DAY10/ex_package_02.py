# ======================================================================
#                       파이썬 표준 모듈 및 패키지
# ======================================================================
# 날짜/시간 모듈들
# -> date     모듈
# -> time     모듈
# -> datetime 모듈
# ======================================================================
# ----------------------------------------------------------------------
# 모듈 로딩
# ----------------------------------------------------------------------
import datetime             # 날짜시간 모듈
import time                 # 시간 모듈

# ----------------------------------------------------------------------
# 모듈 사용
# ----------------------------------------------------------------------
print('현재 시간 time()     :', time.time())
print('현재 시간 ctime()    :', time.ctime(time.time()))

current = time.ctime(time.time())
print(current, type(current))

print()

print('현재 날짜시간 now()   :', datetime.datetime.now())
print('현재 날짜시간 today() :', datetime.datetime.today())

current = datetime.datetime.now()
print(f"시간 : {current.hour}시, 분 : {current.minute}분, 초 : {current.second}초")

# => 원하는 날짜에 관련된 datetime 타입 생성
d_day = datetime.datetime(2026, 12, 31, hour=23)
print(d_day)