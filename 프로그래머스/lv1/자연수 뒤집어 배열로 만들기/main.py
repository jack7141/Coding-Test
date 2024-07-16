def solution(n):
    return [int(i) for i in reversed(str(n))]

n = 12345
print(solution(n))


# reversed를 통한 역순 검색