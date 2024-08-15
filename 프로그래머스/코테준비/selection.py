def solution(arr):
    # 선택 정렬 원형
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr = [4, 3, 5, 1, 2]

print(solution(arr))
