def solution(num):
    answer = 0
    while num != 1:
        if num == 1:
            return answer
        if answer > 500:
            return -1
        if num % 2 == 0:
            num = num // 2
            answer += 1
        else:
            num = num * 3 + 1
            answer += 1
    return answer

num = 6
print(solution(num))