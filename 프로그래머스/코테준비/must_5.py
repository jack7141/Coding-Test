"""
문제 6: 하위 배열의 주파수 계산 최적화
문제: 여러 쿼리에 대해 하위 배열의 최대값 빈도를 더욱 최적화합니다.

최종 해결 방법:
최종 솔루션은 O(n)O(n)O(n) 시간 내에 max_from 및 freq_of_max 배열을 구축하고 각 쿼리에 O(1)O(1)O(1)로 응답할 수 있도록 합니다.
"""


def frequencyOfMaxValue(numbers, q):
    n = len(numbers)

    # Arrays to store the maximum values and their frequencies from each index to the end
    max_from = [0] * n
    freq_of_max = [0] * n

    # Initialize the last element's maximum and frequency
    max_from[-1] = numbers[-1]
    freq_of_max[-1] = 1

    # Build the max_from and freq_of_max arrays from right to left
    for i in range(n - 2, -1, -1):
        if numbers[i] > max_from[i + 1]:
            max_from[i] = numbers[i]
            freq_of_max[i] = 1
        elif numbers[i] == max_from[i + 1]:
            max_from[i] = numbers[i]
            freq_of_max[i] = freq_of_max[i + 1] + 1
        else:
            max_from[i] = max_from[i + 1]
            freq_of_max[i] = freq_of_max[i + 1]

    # For each query, retrieve the precomputed maximum frequency
    result = [freq_of_max[query - 1] for query in q]

    return result


# Example usage
result = frequencyOfMaxValue([2, 2, 2], [1, 2, 3])
print(result)  # Output: [3, 2, 1]