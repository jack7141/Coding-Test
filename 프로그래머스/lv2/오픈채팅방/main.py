
def solution(record):
    ACTION_MAP = {
        'Enter': '님이 들어왔습니다.',
        'Leave': '님이 나갔습니다.'
    }

    answer = []
    user_id_nickname = {}
    user_list = [_record.split() for _record in record]

    for user in user_list:
        if len(user) == 3:
            status, id, nickname = user
        elif len(user) == 2:
            status, id = user
            nickname = None

        if nickname:
            user_id_nickname[id] = nickname
        elif id not in user_id_nickname:
            user_id_nickname[id] = None
    for i in user_list:
        if i[0] == 'Change':
            continue
        answer.append(f"{user_id_nickname[i[1]]}{ACTION_MAP[i[0]]}")
    return answer



test_cases = [
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
]


for files in test_cases:
    print(solution(files))