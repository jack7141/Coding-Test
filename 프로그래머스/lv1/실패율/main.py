from itertools import combinations
from collections import Counter

def solution(dartResult):
    answer = 0
    return answer


problems = [
    [5, [2, 1, 2, 6, 2, 4, 3, 3]],
    [4, [4, 4, 4, 4, 4]]
]
for N, stages in problems:
    print(solution(N, stages))


# reversed를 통한 역순 검색