from itertools import combinations

def solution(nums):
    answer = 0

    def is_prime_number(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    for i in list(combinations(nums, 3)):
        if is_prime_number(sum(i)):
            answer += 1

    return answer


problems = [
    [1,2,3,4],
    [1,2,7,6,4]
]
for n in problems:
    print(solution(n))


# reversed를 통한 역순 검색