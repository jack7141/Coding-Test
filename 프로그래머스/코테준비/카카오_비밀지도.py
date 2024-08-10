# Link: https://school.programmers.co.kr/learn/courses/30/lessons/17681
from collections import deque


def solution(n, t, m, p):
    ACTION_MAP = {
        2: lambda x: bin(x)[2:],
        8: lambda x: oct(x)[2:],
        16: lambda x: hex(x)[2:],
    }
    answer = ''
    for i in range(m):
        print(ACTION_MAP[n](i).zfill(t))
    return ACTION_MAP[n](t).zfill(t)

test = [
    [2, 4, 2, 1],
    [16, 16, 2, 1],
    [16, 16, 2, 2],
]
for n, t, m, p in test:
    print(solution(n, t, m, p))