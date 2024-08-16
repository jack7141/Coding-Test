from collections import deque


directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

import numpy as np
def solution(land):
    answer = 0
    n, m = len(land), len(land[0])

    # 방문배열
    visited = [[False] * m for _ in range(n)]
    # 각 열의 기름을 얼마나 추출할 수 있는지 세팅
    oil = [0] * m
    directions = [(0, 1), (1, 0),
                  (-1, 0), (0, -1)]

    def bfs(row, col):
        queue = deque()
        queue.append([row, col])
        visited[row][col] = True
        cnt = 1
        # bfs 탐색중 석유가 있는 열, 중복을 방지하기 위한 set
        oil_covered = {col}

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    cnt += 1
                    # 현재 석유를 발견한 열 추가
                    oil_covered.add(ny)

        # 각 열을 돌면서 석유량 추가
        for c in oil_covered:
            oil[c] += cnt

    # bfs 탐색
    # 행
    for i in range(n):
        # 열
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)

    answer = max(oil)

    return answer

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




## BFS 원형

"""
def dfs(x, y)
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                queue.append([nx, ny])


for x in range(n):
    for y in range(m):
        bfs(x, y)
        
"""
