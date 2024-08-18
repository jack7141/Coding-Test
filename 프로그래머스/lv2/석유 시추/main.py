from collections import deque



import numpy as np
def solution(land):
    n, m = len(land), len(land[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = [[False] * m for _ in range(n)]
    answer = [0] * m
    def bfs(x, y):
        queue = deque([[x, y]])
        visited[x][y] = True
        oil_count = 1
        oil_covered = {y}
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and visited[nx][ny] == False:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    oil_count += 1
                    oil_covered.add(ny)

        for i in oil_covered:
            answer[i] += oil_count
        return True

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)



    return max(answer)

test_cases = [
    [[0, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0],
     [1, 1, 0, 0, 0, 1, 1, 0],
     [1, 1, 1, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0, 1, 1]],
    [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
]




for land in test_cases:
    print(solution(land))


