import numpy as np
def solution(m, n, board):
    column = 5
    row = len(board)
    answer = 0
    s = [list(i) for i in board]
    s = np.array(s)
    return answer


test_cases = [
    [4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]],
    [6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]
]


for m, n, board in test_cases:
    print(solution(m, n, board))