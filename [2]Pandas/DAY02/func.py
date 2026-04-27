# =========================================================
#       Series / DataFrame에서 자주 사용되는 함수들
# =========================================================

# ---------------------------------------------------------
# 함수기능 : Series/DataFrame 인스턴스 속성 출력 기능
# 함수이름 : print_info
# 매개변수 : obj        - Series/DataFrame 인스턴스
#          : obj_name   - 인스턴스 이름
# 결과처리 : 반환 X
# ---------------------------------------------------------
def print_info(obj, obj_name):
    print(f"\n--[{obj_name} 속성들]")
    print(f"index  : {obj.index}")      # 원소 식별 번호
    print(f"values : {obj.values}")     # 원소에 저장된 데이터들
    print(f"shape  : {obj.shape}")      # 1줄 시리즈의 형태 모양. 튜플로 표기
    print(f"ndim   : {obj.ndim}")       # 차원(1, 2, ... , N) 정보
    print(f"dtype  : {obj.dtype}")      # 원소의 데이터 타입 정보
    print(f"name   : {obj.name}")       # 부가/메타 정보로 이름
