import serial                      # 시리얼 통신을 위한 라이브러리
import serial.tools.list_ports     # 시리얼 포트 검색을 위한 라이브러리
import time                        # 시간 관련 라이브러리
import random                      # 랜덤 숫자 생성을 위한 라이브러리
import threading                   # 스레드 사용을 위한 라이브러리(시리얼, input() 동시 처리)

# ports = serial.tools.list_ports.comports()   # 시리얼 포트 검색
# for p in ports:
#     print(p.device, p.description, p.hwid)


PORT = 'COM8'                                  # 포트 변경 필요
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=1)     # ser 시리얼 객체 생성
time.sleep(2)                                  # 보드 리셋 대기
print("serial connected")


menu = [                                       # 메뉴 코드와 이름을 매핑
    [
        {"code": "Main1", "name": "2인분", "price": 28000},
        {"code": "Main2", "name": "3인분", "price": 42000},
        {"code": "Main3", "name": "4인분", "price": 56000},
    ],
    [
        {"code": "Extra1", "name": "고기 추가", "price": 8000},
        {"code": "Extra2", "name": "야채 추가", "price": 1000},
        {"code": "Extra3", "name": "면 추가", "price": 1000},
    ],
    [
        {"code": "Side", "name": "물만두", "price": 5000},
    ],
    [
        {"code": "Bever1", "name": "콜라", "price": 2000},
        {"code": "Bever2", "name": "사이다", "price": 2000},
        {"code": "Bever3", "name": "참이슬", "price": 4000},
    ]
]

table_number = [1,2,3,4,5,6,7,11,12,13,14,15,16,21,22,23,24,25,26]  # 테이블 번호 리스트
orders = []                                                         # 주문 리스트 초기화 
payment_list = []                                                   # 결제 완료 리스트 초기화
total_sales = 0                                                     # 총 매출액 초기화
pay = 0                                                             # 받을 금액 초기화
received = 0                                                        # 받은 금액 초기화
first_order = True                                                  # 첫 주문 여부 초기화 DELETE 명령어로 주문 삭제 시 첫 주문 판별
table_status = []
for _ in range(19): 
    table_status.append(0)                                          # 테이블 상태 초기화 (0: 빈 테이블)

def ordercode(table_num):
    global orders, table_status, menu, table_number, payment_list, first_order, extra_num
    orders_temp = []
    if table_status[table_number.index(table_num)] == 0:            # 빈 테이블인 경우
        first_order = True
        main_random = random.choice(menu[0])
        orders.append({table_num:main_random})           # 주문 리스트에 메인 메뉴 추가
        orders_temp.append(main_random)                  # 테이블 번호와 메인 메뉴를 딕셔너리로 orders_temp에 추가
        for _ in range(random.randint(0, 3)):
            extra_random = random.randint(1, 3)
            orders_temp.append(menu[extra_random][random.randint(0, len(menu[extra_random]) - 1)])    # 추가 메뉴에서 랜덤으로 선택 (0~3개)
        table_status[table_number.index(table_num)] = orders_temp   # [0,0,[{},{},{},{}],0...,0]
        
    else:                                                           # 추가 주문인 경우 메인 메뉴는 없음
        first_order = False
        extra_num = random.randint(1, 3)
        for _ in range(extra_num):
            extra_random = random.randint(1, 3)
            orders.append({table_num:random.choice(menu[extra_random])})             # 주문 리스트에 추가 메뉴 추가
            orders_temp.append(menu[extra_random][random.randint(0, len(menu[extra_random]) - 1)])
        table_status[table_number.index(table_num)].extend(orders_temp)

def center_text(text, total_width):                                 # 텍스트를 중앙에 정렬하는 함수
    text_length = 0
    for char in text:
        if char == ' ':            # 공백
            text_length += 1
        elif char.isdigit():       # 0-9
            text_length += 1
        elif '가' <= char <= '힣': # 한글 유니코드 2칸으로 계산
            text_length += 2
        else:                      # 영문/기호 등
            text_length += 1
    space = (total_width - text_length) // 2
    return ' ' * space + text + ' ' * (total_width - text_length - space)

def display_table():                                                # 테이블 상태를 표시하는 함수
    first = []
    second = []
    third = []
    forth = []
    for table_num in range(0, 19):
        if table_status[table_num] == 0:
            first.append("빈 테이블")
            second.append("")
            third.append("")
            forth.append("")
        else:
            first.append(table_status[table_num][0]['name'])
            second.append(table_status[table_num][1]['name']) if len(table_status[table_num]) > 1 else second.append("")
            third.append(table_status[table_num][2]['name']) if len(table_status[table_num]) > 2 else third.append("")
            forth.append(table_status[table_num][3]['name']) if len(table_status[table_num]) > 3 else forth.append("")
    print("\n\n")

    for i in range(0, 5, 2):
        print(f"┌{'─' * 4}{i+22:02d}{'─' * 5}┐{' ' * 4}┌{'─' * 4}{i+21:02d}{'─' * 5}┐{' ' * 8}┌{'─' * 4}{i+12:02d}{'─' * 5}┐{' ' * 4}┌{'─' * 4}{i+11:02d}{'─' * 5}┐{' ' * 8}┌{'─' * 4}{i+2:02d}{'─' * 5}┐{' ' * 4}┌{'─' * 4}{i+1:02d}{'─' * 5}┐")
        print(f"│{center_text(first[i+14], 11)}│{" " * 4}│{center_text(first[i+13], 11)}│{" "* 8}│{center_text(first[i+8], 11)}│{" " * 4}│{center_text(first[i+7], 11)}│{" " * 8}│{center_text(first[i+1], 11)}│{" " * 4}│{center_text(first[i], 11)}│")
        print(f"│{center_text(second[i+14], 11)}│{" " * 4}│{center_text(second[i+13], 11)}│{" "* 8}│{center_text(second[i+8], 11)}│{" " * 4}│{center_text(second[i+7], 11)}│{" " * 8}│{center_text(second[i+1], 11)}│{" " * 4}│{center_text(second[i], 11)}│")
        print(f"│{center_text(third[i+14], 11)}│{" " * 4}│{center_text(third[i+13], 11)}│{" "* 8}│{center_text(third[i+8], 11)}│{" " * 4}│{center_text(third[i+7], 11)}│{" " * 8}│{center_text(third[i+1], 11)}│{" " * 4}│{center_text(third[i], 11)}│")
        print(f"│{center_text(forth[i+14], 11)}│{" " * 4}│{center_text(forth[i+13], 11)}│{" "* 8}│{center_text(forth[i+8], 11)}│{" " * 4}│{center_text(forth[i+7], 11)}│{" " * 8}│{center_text(forth[i+1], 11)}│{" " * 4}│{center_text(forth[i], 11)}│")
        print(f"└{'─' * 11}┘{' ' * 4}└{'─' * 11}┘{' ' * 8}└{'─' * 11}┘{' ' * 4}└{'─' * 11}┘{' ' * 8}└{'─' * 11}┘{' ' * 4}└{'─' * 11}┘")
        #  15 14		 9  8		2 1
        #  17 16		11 10		4 3
        #  19 18		13 12		6 5
		# 		                      7
    print(f"{' ' * 93}┌{'─' * 4}{7:02d}{'─' * 5}┐")
    print(f"{' ' * 93}│{center_text(first[18], 11)}│")
    print(f"{' ' * 93}│{center_text(second[18], 11)}│")
    print(f"{' ' * 93}│{center_text(third[18], 11)}│")
    print(f"{' ' * 93}│{center_text(forth[18], 11)}│")
    print(f"{' ' * 93}└{'─' * 11}┘")

def display_total_sales():                                          # 총 매출액을 표시하는 함수
    for payment in payment_list:
        global total_sales
        total_sales += payment['price']
    print("\n┏━━━━━ 총 매출액 ━━━━━┓")
    print(f"┃{center_text(f'{total_sales:,}원', 21)}┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━┛")

def display_command():                                              # 결제 메뉴와 주문 순서 메뉴를 표시하는 함수
    print(" ===== 명령 메뉴 =====")
    print("   1. 결제")
    print("   2. 주문 순서")
    print("   3. 금일 판매 내역")
    print("   4. 종료")
    print(" =====================")

def payment(table_num, received_amount):
    global pay, received
    menu_item = {}
    received = received_amount
    if table_status[table_number.index(table_num)] == 0:            # 빈 테이블인 경우
        print("빈 테이블입니다. 주문이 없습니다.")
        return
    
    for item in table_status[table_number.index(table_num)]:
        pay += item['price']                                        # 받을 금액 계산
        if item['name'] not in menu_item:                           # 결제된 메뉴와 수량 저장
            menu_item[item['name']] = (1, item['price'])
        else:
            quantity, price = menu_item[item['name']]
            menu_item[item['name']] = (quantity + 1, price)
    
    print("==== 상품명 ===== 단가 ==== 수량 ===== 금액 ===")
    for menu_name, (quantity, price) in menu_item.items():
        print(f"{center_text(menu_name, 15)}{center_text(f'{price:,}', 10)}{center_text(f'{quantity}', 10)}{center_text(f'{quantity * price:,}', 12)}")                         # 결제할 메뉴와 수량 출력
   
    if received > pay:
        change = received - pay
        table_status[table_number.index(table_num)] = 0                                     # 0: 빈 테이블로 변경
        for order in orders:
            if table_num in order:
                del order[table_num]                                                        # 주문 리스트에서 해당 테이블의 주문 삭제
            else: None
        payment_list.append({"table_num": table_num, "menu_item": menu_item, "price": pay}) # 결제 완료 리스트에 추가
        print(f"결제가 완료되었습니다. 거스름돈: {change:,}원")
    elif received == pay:
        table_status[table_number.index(table_num)] = 0                                     # 0: 빈 테이블로 변경
        payment_list.append({"table_num": table_num, "menu_item": menu_item, "price": pay}) # 결제 완료 리스트에 추가
        print("결제가 완료되었습니다. 감사합니다.")
    else:
        print(f"받은 금액이 부족합니다. 추가금 {pay - received:,}원을 결제해주십시오.")     # 결제 완료 처리로 간주
        table_status[table_number.index(table_num)] = 0                                     # 0: 빈 테이블로 변경
        payment_list.append({"table_num": table_num, "menu_item": menu_item, "price": pay}) # 결제 완료 리스트에 추가

running = True

display_table()                                                                  # 테이블 상태 표시
display_total_sales()                                                              # 총 매출액 표시
display_command()                                                                  # 명령 메뉴 표시    

def read_serial():
    global running
    while running:
        line = ser.readline().decode('utf-8', errors='ignore')                                  # 시리얼 포트에서 한 줄 수신
        if line:
            print(line) 
            parts = line.split(',')
            if parts[0] == 'TABLE':
                last_line = line
                table_num = int(parts[1])                                                        # 테이블 번호 추출
                ordercode(table_num)                                                             # 주문 코드 생성 및 주문 리스트에 저장
                display_table()                                                                  # 테이블 상태 표시
                display_total_sales()                                                              # 총 매출액 표시
                display_command()                                                                  # 명령 메뉴 표시

            elif line == 'DELETE\r\n':
                if last_line == 'DELETE\r\n':
                    print("이미 삭제 명령이 처리되었습니다.")
                    continue
                if first_order: 
                    table_status[table_number.index(table_num)] = 0                              # 0: 빈 테이블로 변경
                else:
                    for _ in range(extra_num):
                        del table_status[table_number.insdex(table_num)][-1]
                del orders[-1]
                last_line = line
                display_table()                                                                  # 테이블 상태 표시
                display_total_sales()                                                              # 총 매출액 표시
                display_command()                                                                  # 명령 메뉴 표시

t = threading.Thread(target=read_serial, daemon=True)
t.start()


while True:
    command = int(input("명령을 입력하세요: "))
    if command == 1:
        table_num = int(input("결제할 테이블 번호를 입력하세요: "))
        received_amount = int(input("받은 금액을 입력하세요: "))
        payment(table_num, received_amount)
        display_table()                                                                  # 테이블 상태 표시
        display_total_sales()                                                              # 총 매출액 표시
        display_command()                                                                  # 명령 메뉴 표시
    elif command == 2:
        print("주문 순서:")
        for order in orders:
            for table_num, menu_item in order.items():
                print(f"테이블 {table_num}: {menu_item['name']}")
    elif command == 3:
        print("금일 판매 내역:")
        for payment in payment_list:
            print(f"테이블 {payment['table_num']}: {payment['menu_item']} - {payment['price']:,}원")
    elif command == 4:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 명령입니다. 다시 입력해주세요.")


running = False
ser.close()