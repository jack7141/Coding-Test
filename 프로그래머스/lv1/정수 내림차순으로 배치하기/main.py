def solution(n):
    n = [i for i in str(n)]
    n.sort(reverse=True)
    # map에는 리스트가 들어가야한다
    return int(''.join(map(str, n)))

n = 118372
result = solution(n)
assert result == 873211