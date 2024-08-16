

def solution(arr):
    # 선택 정렬 원형
    n = len(arr)
    for i in range(n):
        # 가장 작은 데이터의 인덱스
        min_idx = i
        for j in range(i + 1, n):
            # 최솟값 찾기
            if (arr[min_idx] > arr[j]):
                min_idx = j
        # 데이터 간의 자리 변경
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [4, 3, 5, 1, 2]

print(solution(arr))

n = len(arr)

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]