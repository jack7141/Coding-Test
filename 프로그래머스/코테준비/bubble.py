

def solution(arr):
    # 버블 정렬 원형
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def solution_1(arr):
    # 버블 정렬 최적화 1
    for i in range(len(arr) - 1, 0, -1):
        swap = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break
    return arr


arr = [4, 3, 5, 1, 2]
print(solution_1(arr))
