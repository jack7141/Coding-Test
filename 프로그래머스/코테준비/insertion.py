

def solution(arr):
    # 삽입 정렬 원형
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
        print(i)
    return arr



def solution_1(arr):
    for end in range(1, len(arr)):
        i = end
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1




arr = [4, 3, 5, 1, 2]

"""
[4, 3, 5, 1, 2]
    ^
 ^

"""
print(solution_1(arr))


