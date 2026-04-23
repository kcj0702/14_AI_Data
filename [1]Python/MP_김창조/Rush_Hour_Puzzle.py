import os

# 테스트 (레이튼 문제)
matrix = [[-1 for _ in range(6)] for _ in range(6)]         # 좌표 초기화 matrix[i][j] => i : x좌표, j : y좌표
matrix = [
    [7, 7, 0, -1, 1, 1], 
    [9, 8, 0, -1, 2, -1], 
    [9, 8, 4, 4, 2, -1], 
    [10, 5, 5, -1, -1, -1], 
    [10, -1, -1, -1, -1, 3], 
    [11, 11, 6, 6, -1, 3]
]

# 전역 변수
cursor = [0, 0]                                             # 차량을 선택할 시, 차량 이동 시에 사용함, 이동시킬 차량의 좌표

# ======================
#       함수 정의
# ======================
# 이동시킬 차량의 좌표를 이동시키는 함수
# 실행 시 입력된 방향으로 좌표를 한 번만 이동
def select(key_pad:str):                                    # 함수의 매개변수로 키패드의 숫자(str)를 받음
    global cursor
    temp = cursor.copy()                                    # 현재 위치 복사 
    if len(key_pad) == 1 and key_pad.isdecimal():           # 응답 필터
        if key_pad == '8': temp[1] += 1                     # ↑
        elif key_pad == '4': temp[0] -= 1                   # ←
        elif key_pad == '6': temp[0] += 1                   # →
        elif key_pad == '2': temp[1] -= 1                   # ↓ 
        elif key_pad == '0': return cursor                  # 선택 취소 시 원래 커서 좌표 반환
        elif key_pad == '5':                                # 선택 완료 시 커서 좌표 반환
            cursor = temp.copy()
            return cursor 

    temp = [n if n >= 0 else len(matrix[0]) if n > len(matrix[0]) else 0 for n in temp]     # matrix 이탈 방지

    return temp                                             # 화면에 표시할 이동된 커서 위치

# 선택된 차량을 좌표 이동시키는 함수
# 실행 시 입력된 방향으로 좌표를 한 번만 이동
def move(wasd:str):
    