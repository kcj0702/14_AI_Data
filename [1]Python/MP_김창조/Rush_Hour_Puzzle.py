import os
import time

# 문제 정의
matrix = [[-1 for _ in range(6)] for _ in range(6)]         # 좌표 초기화 matrix[i][j] => i : x좌표, j : y좌표
matrix = [                                                  # 0 : 목표 차량, 1~ : 방해 차량, -1 : 빈 공간
    [7, 7, 0, -1, 1, 1], 
    [9, 8, 0, -1, 2, -1], 
    [9, 8, 4, 4, 2, -1], 
    [10, 5, 5, -1, -1, -1], 
    [10, -1, -1, -1, -1, 3], 
    [11, 11, 6, 6, -1, 3]
]
answer = (5, 2)

# 전역 변수
IMAGE_PATH = r'.\image.txt'                                 # 도트 이미지가 저장된 txt 경로
image_list = []                                             # 도트 이미지가 담길 리스트
screen_matrix = [[-1 for _ in range(6)] for _ in range(6)]  # 화면 표시 커맨드가 담길 리스트 초기화
cursor = [0, 0]                                             # 차량을 선택할 시, 차량 이동 시에 사용함, 이동시킬 차량의 좌표
temp_cursor = [0, 0]
car_num = 0                                                 # 선택된 차량 번호
temp_dir, temp_car_num = -1, -1
vec = [(0,1), (0,-1), (1,0), (-1,0)]                        # 위 아래 왼쪽 오른쪽의 방향 벡터
car_dir_idx = 0
move_cnt = 0                                                # 움직인 횟수

# ======================
#       함수 정의
# ======================
# 화면 출력을 위해 배치된 차량의 방향을 판별하는 함수
# 실행 시 판별하고 방향에 맞는 차량 이미지 커맨드가 포함된 중복 리스트 출력 
def image_dir(matrix:list):
    global screen_matrix
    for y in range(len(matrix[0])-1, -1, -1):
        for x in range(len(matrix)):
            next_x = int(x+1 < len(matrix))                             # 탐색시 슬라이싱 오류 방지
            next_y = int(y-1 > -1)                                      # 탐색시 슬라이싱 오류 방지
            if matrix[x][y-next_y] == -1 : screen_matrix[x][y-next_y] = '#_CAR_NONE'

            if  matrix[x][y] == -1:
                screen_matrix[x][y] = '#_CAR_NONE'

            elif matrix[x][y] == matrix[x+next_x][y] and next_x:        # 오른쪽과 번호가 같은 경우
                if matrix[x][y] == 0:                                   # 차량 번호가 0이라면 목표 차량
                    screen_matrix[x][y]   = '#_CAR_LAYTON1'
                    screen_matrix[x+next_x][y] = '#_CAR_LAYTON2'
                else:
                    screen_matrix[x][y]   = '#_CAR_HORIZONTAL1'         # 가로 차량1
                    screen_matrix[x+next_x][y] = '#_CAR_HORIZONTAL2'    # 가로 차량2

            elif matrix[x][y] == matrix[x][y-next_y] and next_y:        # 밑과 번호가 같은 경우
                screen_matrix[x][y]   = '#_CAR_VERTICAL1'               # 세로 차량1
                screen_matrix[x][y-next_y] = '#_CAR_VERTICAL2'          # 세로 차량2
    return screen_matrix


# 입력된 이동 방향과 차량의 방향, 장애물 유무로 이동 가능한지 판별하는 함수
# 실행 시 판별하고 코드값 반환
def ispossible(wasd:str):
    global matrix, cursor, car_num, car_dir_idx
    x, y = cursor
    car_dir = ''

    def get_safe(x, y, matrix):                                             # x+1, x-1, y+1, y-1이 행렬의 범위를 넘어가지 않도록 하는 내부 함수
        return matrix[x][y] if 0 <= x < len(matrix[0]) and 0 <= y < len(matrix) else None
    
    temp = [get_safe(x+dx, y+dy, matrix) for dx, dy in vec]          # wsda의 방향 순서대로 커서 주변 4칸의 값들의 리스트
    car_dir_idx = temp.index(car_num)
    car_dir = '82' if car_dir_idx == 0 or car_dir_idx == 1 else '64'        # 차량의 방향 판별
    if wasd in car_dir:                                                     # 입력값 필터
        car_dir = wasd
        car_dir_idx = '8264'.find(wasd)

        if matrix[x + vec[car_dir_idx][0]][y + vec[car_dir_idx][1]] == -1:  # 이동 방향의 장애물 체크
            # 커서 기준 1칸만 움직여도 될 때
            return 1
        elif (matrix[x + vec[car_dir_idx][0]][y + vec[car_dir_idx][1]] == car_num) and (matrix[x + 2 * vec[car_dir_idx][0]][y + 2 * vec[car_dir_idx][1]] == -1):
            # 커서 기준 2칸을 움직여야 할 때
            return 2
        else:
            return 0
    else: 
        return 0
    

# 이동시킬 차량의 좌표를 이동시키는 함수
# 실행 시 입력된 방향으로 좌표를 한 번만 이동
def select(key_pad:str):                                        # 함수의 매개변수로 키패드의 숫자(str)를 받음
    global cursor, temp_cursor

    if key_pad in '024568':                                     # 응답 필터
        if   key_pad == '8': temp_cursor[1] += 1                # ↑
        elif key_pad == '4': temp_cursor[0] -= 1                # ←
        elif key_pad == '6': temp_cursor[0] += 1                # →
        elif key_pad == '2': temp_cursor[1] -= 1                # ↓ 
        elif key_pad == '0': return cursor, 1                   # 선택 취소 시 원래 커서 좌표 반환, 선택 완료 코드
        elif key_pad == '5':                                    # 선택 완료 시 커서 좌표 반환
            if matrix[temp_cursor[0]][temp_cursor[1]] >= 0:     # 아무 차량도 선택 안하는 경우 방지
                cursor = temp_cursor.copy()
                return cursor, 1                                # 커서 좌표와 선택 완료 코드 반환

    temp_cursor[0] = len(matrix)-1 if temp_cursor[0] >= len(matrix) else temp_cursor[0] if temp_cursor[0] >= 0 else 0   # matrix 이탈 방지
    temp_cursor[1] = len(matrix)-1 if temp_cursor[1] >= len(matrix) else temp_cursor[1] if temp_cursor[1] >= 0 else 0   # matrix 이탈 방지

    return temp_cursor, 0                                       # 화면에 표시할 이동된 커서 위치, 선택 진행 중 코드 반환

# 선택된 차량을 좌표 이동시키는 함수
# 실행 시 입력된 방향으로 좌표를 한 번만 이동
def move(wasd:str):
    global cursor, matrix, car_num, vec, car_dir_idx, move_cnt, temp_cursor, temp_dir, temp_car_num
    car_num = matrix[cursor[0]][cursor[1]]
    if wasd in '2468':
        temp = ispossible(wasd)
        if temp:
            moved_x, moved_y = cursor[0] + temp * vec[car_dir_idx][0], cursor[1] + temp * vec[car_dir_idx][1]           # 움직일 x, y 좌표
            if (moved_x > len(matrix)) or (moved_y > len(matrix[0])) or (moved_x < 0) or (moved_y < 0):                 # 좌표 범위를 벗어나는지 체크
                return
            matrix[cursor[0] + (temp - 2) * vec[car_dir_idx][0]][cursor[1] + (temp - 2) * vec[car_dir_idx][1]] = -1     # 움직이고 난 후의 빈 공간
            matrix[moved_x][moved_y] = car_num                                                                          # 움직일 공간
            cursor = [cursor[0] + vec[car_dir_idx][0], cursor[1] + vec[car_dir_idx][1]]
            if not (car_dir_idx == temp_dir and car_num == temp_car_num):                                               # 움직인 횟수 카운트
                move_cnt += 1
            temp_dir = car_dir_idx
            temp_car_num = car_num
    temp_cursor = cursor.copy()

# 커맨드를 받아 화면을 출력해주는 함수
# 실행 시 필요한 이미지를 image.txt에서 받아와서 출력
def print_screen(command:str):
    with open(IMAGE_PATH, mode='r', encoding='utf-8') as f:
        for line in f:
            if line == command:
                image_list.append
            



for y in range(len(matrix[0])-1, -1, -1):
    for x in range(len(matrix)):
        print(f'{matrix[x][y]:>3}', end='')
    print()

# while True:
#     while True:
#         a = select(input('커서'))
#         print(a)
#         if a[1] == 1:
#             break
#     b = input('이동')
#     move(b)
#     print(move_cnt)
#     for y in range(len(matrix[0])-1, -1, -1):
#         for x in range(len(matrix)):
#             print(f'{matrix[x][y]:>3}', end='')
#         print()
#     if b == '그만':
#         break
