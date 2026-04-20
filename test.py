import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def solution(signals):
    y_range = []
    frequency = []

    for signal in signals:
        frequency.append(sum(signal))
    limit = frequency[0]

    for i in frequency:
        limit = lcm(limit, i)

    for num, signal in enumerate(signals):
        start = signal[0] + 1
        end = signal[0] + signal[1] + 1
        y_temp = set()
        while end <= limit:
            y_temp.update(range(start, end))
            start += frequency[num]
            end += frequency[num]
        y_range.append(y_temp)

    ytime = y_range[0]
    for y in range(1, len(y_range)):
        ytime = ytime.intersection(y_range[y])

    if len(ytime) == 0:
        return -1
    else:
        return min(ytime)

print(solution([[2, 1, 2], [5, 1, 1]]))


def solution(schedules, timelogs, startday):
    answer = 0
    for timelog in timelogs:
        timelog.pop((6-startday) if startday <= 6 else 0)
        timelog.pop((6-startday) if startday <= 6 else -1)
    
    for i in range(len(schedules)):
        event = True
        if (schedules[i] + 10) % 100 >= 60:
            schedules[i] = ((schedules[i]//100+1)*100) + ((schedules[i]+50)%100/60)
        else:
            schedules[i] = (schedules[i]//100*100) + ((schedules[i]+10)%100/60)

        for time in timelogs[i]:
            if round(schedules[i],-2) + round(schedules[i]%1*60 ,0) < time:
                event = False

        if event:
            answer += 1
    
    return answer

print(solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 7))

def three(): 
    return 1, return 2, return 3