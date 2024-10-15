"""
문제 4: 우선순위 재지정
문제: 상대 순서를 유지하고 최대값을 최소화하면서 우선순위 값을 다시 할당합니다.
"""
def reassignedPriorities(arr):
    distinct_values = sorted(set(arr))
    priority_map = {value: i + 1 for i, value in enumerate(distinct_values)}
    reassigned = [priority_map[value] for value in arr]
    return reassigned

# Example usage
result = reassignedPriorities([1, 4, 8, 4])
print(result)  # Output: [1, 2, 3, 2]