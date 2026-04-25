import os                                                   # 파일 읽기를 위한 패키지
import time                                                 # 출력 딜레이를 위한 패키지

# 전역 변수
PROBLEM_PATH = r'.\problem.txt'                             # 문제가 저장된 txt 경로
IMAGE_PATH = r'.\image.txt'                                 # 도트 이미지가 저장된 txt 경로

command_screen = ['#_INTRO', '#_CORRECT1', '#_CORRECT2', '#_CORRECT2', '#_CORRECT3', '#_CORRECT4']     # 이미지 출력 트리거 커맨드
command_car = ['#_CAR_LAYTON1', '#_CAR_LAYTON2', '#_CAR_HORIZONTAL1', '#_CAR_HORIZONTAL2', '#_CAR_VERTICAL1', '#_CAR_VERTICAL2', '#_CAR_NONE']      # 방해 차량 출력 트리거 커맨드

level = 'a'                                                   # 난이도
image_list = []                                             # 도트 이미지가 담길 리스트
cursor = [0, 0]                                             # 차량을 선택할 시, 차량 이동 시에 사용함, 이동시킬 차량의 좌표
temp_cursor = [0, 0]
car_num = 0                                                 # 선택된 차량 번호
temp_dir, temp_car_num = -1, -1
vec = [(0,1), (0,-1), (1,0), (-1,0)]                        # 위 아래 왼쪽 오른쪽의 방향 벡터
car_dir_idx = 0
move_cnt = 0                                                # 움직인 횟수
text = [
'                   혼잡한 주차장에서',
'                   자동차를 빼내려고 한다.', 
'                   ',
'                   자동차는 현재 놓여진 상태에서',
'                   앞뒤로만 움직일 수 있다고 한다.',
'                   ',
'                   키패드로 커서를 움직여 선택하고',
'                   자동차를 움직여서 출구까지 가져가 보자'
]

# ======================
#       함수 정의
# ======================
# 화면 출력을 위해 배치된 차량의 방향을 판별하는 함수
# 실행 시 판별하고 방향에 맞는 차량 이미지 커맨드가 포함된 중복 리스트 출력 
def image_dir(matrix:list):
    screen_matrix = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]  # 화면 표시 커맨드가 담길 리스트 초기화
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
def ispossible(key_pad:str):
    global matrix, cursor, car_num, car_dir_idx
    x, y = cursor
    car_dir = ''

    def get_safe(x, y, matrix):                                             # x+1, x-1, y+1, y-1이 행렬의 범위를 넘어가지 않도록 하는 내부 함수
        return matrix[x][y] if 0 <= x < len(matrix[0]) and 0 <= y < len(matrix) else None
    
    temp = [get_safe(x+dx, y+dy, matrix) for dx, dy in vec]          # wsda의 방향 순서대로 커서 주변 4칸의 값들의 리스트
    car_dir_idx = temp.index(car_num)
    car_dir = '82' if car_dir_idx == 0 or car_dir_idx == 1 else '64'        # 차량의 방향 판별
    if key_pad in car_dir:                                                     # 입력값 필터
        car_dir = key_pad
        car_dir_idx = '8264'.find(key_pad)
        
        if get_safe(x + vec[car_dir_idx][0], y + vec[car_dir_idx][1], matrix) == -1:  # 이동 방향의 장애물 체크
            # 커서 기준 1칸만 움직여도 될 때
            return 1
        elif (get_safe(x + vec[car_dir_idx][0], y + vec[car_dir_idx][1], matrix) == car_num) and (get_safe(x + 2 * vec[car_dir_idx][0], y + 2 * vec[car_dir_idx][1], matrix) == -1):
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
        elif key_pad == '0': 
            temp_cursor = cursor.copy()
            return cursor, 1                                    # 선택 취소 시 원래 커서 좌표 반환, 선택 완료 코드
        elif key_pad == '5':                                    # 선택 완료 시 커서 좌표 반환
            if matrix[temp_cursor[0]][temp_cursor[1]] >= 0:     # 아무 차량도 선택 안하는 경우 방지
                cursor = temp_cursor.copy()
                return cursor, 1                                # 커서 좌표와 선택 완료 코드 반환
    elif key_pad.strip().lower() == 'answer':
        print(problem[problem.index(f'#_ANSWER{level}')+1])

    temp_cursor[0] = len(matrix)-1 if temp_cursor[0] >= len(matrix) else temp_cursor[0] if temp_cursor[0] >= 0 else 0   # matrix 이탈 방지
    temp_cursor[1] = len(matrix)-1 if temp_cursor[1] >= len(matrix) else temp_cursor[1] if temp_cursor[1] >= 0 else 0   # matrix 이탈 방지

    return temp_cursor, 0                                       # 화면에 표시할 이동된 커서 위치, 선택 진행 중 코드 반환

# 선택된 차량을 좌표 이동시키는 함수
# 실행 시 입력된 방향으로 좌표를 한 번만 이동
def move(key_pad:str):
    global cursor, matrix, car_num, vec, car_dir_idx, move_cnt, temp_cursor, temp_dir, temp_car_num
    car_num = matrix[cursor[0]][cursor[1]]
    if key_pad in '2468':
        temp = ispossible(key_pad)
        if temp:
            moved_x, moved_y = cursor[0] + temp * vec[car_dir_idx][0], cursor[1] + temp * vec[car_dir_idx][1]           # 움직일 x, y 좌표
            if (moved_x > len(matrix)) or (moved_y > len(matrix[0])) or (moved_x < 0) or (moved_y < 0):                 # 좌표 범위를 벗어나는지 체크
                return 1
            matrix[cursor[0] + (temp - 2) * vec[car_dir_idx][0]][cursor[1] + (temp - 2) * vec[car_dir_idx][1]] = -1     # 움직이고 난 후의 빈 공간
            matrix[moved_x][moved_y] = car_num                                                                          # 움직일 공간
            cursor = [cursor[0] + vec[car_dir_idx][0], cursor[1] + vec[car_dir_idx][1]]
            if not (car_dir_idx == temp_dir and car_num == temp_car_num):                                               # 움직인 횟수 카운트
                move_cnt += 1
            temp_dir = car_dir_idx
            temp_car_num = car_num
    elif key_pad == '0':            # 입력이 0(입력 취소)라면 취소 코드 반환
        return 0 
    if key_pad.strip().lower() == 'answer':
        print(problem[problem.index(f'#_ANSWER{level}')+1])
    temp_cursor = cursor.copy()
    return 1                        # 이상 없다면 정상 코드 반환

# 커맨드를 받아 이미지를 찾아주는 함수
# 실행 시 커맨드에 맞는 이미지 리스트를 반환
def image_find(command:str):
    for image_sep in image_list:
        if image_sep[0] == command:
            return image_sep
        
# 커맨드를 받아 화면을 출력해주는 함수
# 실행 시 커맨드에 맞는 화면을 출력
def print_screen(command:str):                                              # 인트로 화면, 정답 화면 출력
    if command in command_screen:
        for image in image_find(command)[1:]:
            print(image)

    elif command == '#_MATRIX':                                             # 현재 차량의 상태가 저장된 matrix를 변환하여 이미지로 출력
        temp1, temp2 = [], []
        for y in range(len(matrix[0])-1, -1, -1):
            for x in range(len(matrix)):
                temp1.append(image_find(image_dir(matrix)[x][y])[1:])       # screen_matrix(이미지 커맨드로만 구성된 matrix)를 이미지의 배열로 변환
            temp2.append(temp1)                                             # 3중 중첩 리스트
            temp1 =[]                                                       # 다음 for 문을 위한 temp1 초기화
        print(f"┏{'━'*(16*len(matrix))}┓")
        temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][2] = temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][2][:4] + '┌──────┐' + temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][2][12:]
        temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][3] = temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][3][:4] + '│  커  │' + temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][3][12:]
        temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][4] = temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][4][:4] + '│  서  │' + temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][4][12:]
        temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][5] = temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][5][:4] + '└──────┘' + temp2[len(matrix) - temp_cursor[1] - 1][temp_cursor[0]][5][12:]

        for n, line in enumerate(temp2):        # temp2 = [ 
            for i in range(len(line[0])):       # [ [ 1번 이미지1줄, ] [ 2번 이미지 1줄, ], ... , [ 6번 이미지 1줄, ] ], 
                print('┃', end='')              # [ [ 7번 이미지1줄, ] [ 8번 이미지 1줄, ], ... , [ 12번 이미지 1줄, ] ],
                for image in line:              # ]
                    print(image[i], end='')
                if not goal[1] <= len(matrix[0]) - n -1 < goal[1]+2 : print('┃', end='') 
                if n == 3: print(text[i])
                elif n == 4 and i == 1: print(f'                   움직인 횟수 : {move_cnt}')
                elif n == 4 and i == 4: print(f"                       8")
                elif n == 4 and i == 5: print(f"                       ↑")
                elif n == 4 and i == 6: print(f"                 4 ← 선택 5 → 6")
                elif n == 4 and i == 7: print(f"                       ↓")
                elif n == 5 and i == 0: print(f"            취소 0     2")
                elif n == 5 and i == 3: print('                   정답 보기 : ANSWER')
                elif n == 5 and i == 4: print('                   그만 두기 : STOP')
                else: print()
        print(f"┗{'━'*16*len(matrix)}┛")

    # matrix = [                                                  # 0 : 목표 차량, 1~ : 방해 차량, -1 : 빈 공간
    # [7, 7, 0, -1, 1, 1], 
    # [9, 8, 0, -1, 2, -1], 
    # [9, 8, 4, 4, 2, -1], 
    # [10, 5, 5, -1, -1, -1], 
    # [10, -1, -1, -1, -1, 3], 
    # [11, 11, 6, 6, -1, 3]
    # ]

# =============================================================
#                           실행코드
# =============================================================

try:
    with open(IMAGE_PATH, mode='r', encoding='utf-8') as f:                 # 이미지 파일 읽어오기 시도
        _ = []                                                              # 각 명령어 분리할 임시 리스트
        once = True
        while True:
            image = f.readline()
            if not ((image.find('#_') >= 0) and (not once)) and image:      # 처음의 #_는 True, 이후 #_는 False
                _.append(image.strip('\n'))
                once = False
            elif not image:                                                 # 파일 끝에 도달하면 본 리스트에 추가 후 루프 종료
                image_list.append(_)
                break
            else:
                image_list.append(_)                                        # 본 리스트에 추가 후 변수 초기화
                _ = [image.strip('\n')] 
                once = True

    try:
        print_screen('#_INTRO')
        time.sleep(1.5)
        print(f'{"============ 문제 ============":^99}', f"{'1. 최소 이동 : 15':^95}", f"{'2. 최소 이동 : 15':^95}", f"{'3. 최소 이동 : 17':^95}", sep='\n')
        while (len(level) != 1) or (level not in '123'):
            level = input('                                            문제 선택 : ')
            if (len(level) != 1) or (level not in '123'):
                print('난이도 1 2 3 중 하나를 선택해주세요.')

        matrix = [[-1 for _ in range(6)] for _ in range(6)]                 # 좌표 초기화 matrix[i][j] => i : x좌표, j : y좌표
        # 문제 정의
        with open(PROBLEM_PATH, mode='r', encoding='utf-8') as p:
            problem = []                                                    # 각 명령어 분리할 임시 리스트
            problem = p.readlines()
            problem  = [i.strip('\n') for i in problem]
            matrix = [list(map(int, l.split(','))) for l in problem[problem.index(f'#_LEVEL{level}')+1 : problem.index(f'#_GOAL{level}')]]
            goal = tuple(map(int ,problem[problem.index(f'#_GOAL{level}')+1].split(',')))

        # for y in range(len(matrix[0])-1, -1, -1):
        #     for x in range(len(matrix)):
        #         print(f'{matrix[x][y]:>3}', end='')
        #     print()

        print('\n\n')
        print_screen('#_MATRIX')

        user_input = ''
        while matrix[goal[0]][goal[1]] != 0:                                # 목표 차량이 goal 지점에 들어오면 while 종료
            if user_input.strip().lower() == 'stop':
                break
            isselect = 0                                                    # 선택 중인지 아닌지 판별
            while not isselect:
                if user_input.strip().lower() == 'stop':
                    break
                user_input = input('커서 이동\n').strip()
                isselect = select(user_input)[1]
                print_screen('#_MATRIX')
            
            ismove = 1                                                      # 이동 중인지 아닌지 판별
            while ismove and matrix[goal[0]][goal[1]] != 0:                  # 입력이 '0'이라면 선택으로 돌아가기
                if user_input.strip().lower() == 'stop':
                    break
                user_input = input('차량 이동\n').strip()
                ismove = move(user_input)
                print_screen('#_MATRIX')

        if matrix[goal[0]][goal[1]] == 0 and user_input.strip().lower() != 'stop':
            print_screen('#_CORRECT1')
            time.sleep(1)
            print_screen('#_CORRECT2')
            time.sleep(1)
            print_screen('#_CORRECT3')
            time.sleep(1)
            print_screen('#_CORRECT4')

    except FileNotFoundError:
        print("""\n문제 파일이 삭제되었거나 이동되었습니다.
    문제 파일 혹은 경로를 확인해주세요.""")

except FileNotFoundError:                                                   # 이미지 파일 오류시 종료
    print('''\n이미지 파일이 삭제되었거나 이동되었습니다.
이미지 파일 혹은 경로를 확인해주세요.''')

except:
    print('\n문제가 발생했습니다. 프로그램을 종료합니다.')                  # 그 외 오류 발생 시 종료