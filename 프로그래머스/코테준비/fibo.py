


def soultion(n):
    if n < 2:
        return n
    cache = [0 for _ in range(n + 1)]
    cache[1] = 1

    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]
print(soultion(100))


def fibo(n, __cache = {0:0, 1:1}):
    if n in __cache:
        return __cache[n]

    __cache[n] = fibo(n-1) + fibo(n-2)
    return __cache[n]


print(fibo(5))