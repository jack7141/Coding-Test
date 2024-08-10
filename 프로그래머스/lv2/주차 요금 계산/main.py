import math
from collections import deque

"""
def solution(fees, records):
    answer = []
    for i in records:
        split_list = i.split()
        time = split_list[0].split(":")
        hour = int(time[0])
        min = int(time[1])
        split_list[0] = (hour * 60) + min
        answer.append(split_list)

    # 차량별 누적 시간을 저장할 딕셔너리
    vehicle_times = {}

    # 차량별 마지막 IN 시간을 저장할 딕셔너리
    vehicle_in_times = {}

    for time, vehicle_number, status in answer:
        if status == "IN":
            vehicle_in_times[vehicle_number] = time
        elif status == 'OUT':
            if vehicle_number in vehicle_in_times:
                in_time = vehicle_in_times.pop(vehicle_number)
                time_spent = time - in_time
                vehicle_times[vehicle_number] = vehicle_times.get(vehicle_number, 0) + time_spent

    for vehicle_number, in_time in vehicle_in_times.items():
        time_spent = 1439 - in_time  # 1439는 23:59를 분으로 표현한 것
        vehicle_times[vehicle_number] = vehicle_times.get(vehicle_number, 0) + time_spent

    result = []
    vehicle_times = dict(sorted(vehicle_times.items(), key=lambda x: x))
    for vehicle_number, in_time in vehicle_times.items():
        if in_time <= fees[0]:
            result.append(fees[1])
        else:
            fee = fees[1] + (math.ceil((in_time - fees[0]) / fees[2])) * fees[-1]
            result.append(fee)
    return result
"""


def solution(fees, records):

    # 차량별 누적 시간을 저장할 딕셔너리
    vehicle_times = {}

    # 차량별 마지막 IN 시간을 저장할 딕셔너리
    vehicle_in_times = {}

    # 시간 변환 및 기록 처리
    for record in records:
        time_str, vehicle_number, status = record.split()
        time = int(time_str[:2]) * 60 + int(time_str[3:])

        if status == "IN":
            vehicle_in_times[vehicle_number] = time
        else:
            time_spent = time - vehicle_in_times.pop(vehicle_number)
            vehicle_times[vehicle_number] = vehicle_times.get(vehicle_number, 0) + time_spent

    # OUT 없이 남아있는 차량 처리
    for vehicle_number, in_time in vehicle_in_times.items():
        vehicle_times[vehicle_number] = vehicle_times.get(vehicle_number, 0) + (1439 - in_time)

    # 요금 계산
    result = []
    for vehicle_number in sorted(vehicle_times):
        total_time = vehicle_times[vehicle_number]
        if total_time <= fees[0]:
            result.append(fees[1])
        else:
            fee = fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]
            result.append(fee)

    return result





test_cases = [
    [[180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]],
    [[120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]],
    [[1, 461, 1, 10], ["00:00 1234 IN"]],
]


for fees, records in test_cases:
    print(solution(fees, records))