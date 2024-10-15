"""
문제 3: 유효한 모음 순열 계산
문제: 특정 모음 배치 규칙이 주어지면 길이 n의 유효한 모음 순열의 수를 계산합니다.
"""
MOD = 10 ** 9 + 7


def countPerms(n):
    dp_a, dp_e, dp_i, dp_o, dp_u = 1, 1, 1, 1, 1

    for _ in range(2, n + 1):
        new_a = (dp_e + dp_i + dp_u) % MOD
        new_e = (dp_a + dp_i) % MOD
        new_i = (dp_e + dp_o) % MOD
        new_o = dp_i % MOD
        new_u = (dp_i + dp_o) % MOD

        dp_a, dp_e, dp_i, dp_o, dp_u = new_a, new_e, new_i, new_o, new_u

    return (dp_a + dp_e + dp_i + dp_o + dp_u) % MOD


# Example usage
n = 764
result = countPerms(n)
print(result)