"""
단지번호붙이기
"""

import sys
from collections import deque

read = sys.stdin.readline
N = int(read())
matrix = [list(map(int, read().strip())) for _ in range(N)]

# 위 아래 오 왼
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(b, a, graph):
    queue = deque()
    queue.append((b, a))
    graph[b][a] = 0
    count = 1

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            elif graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))
                count += 1
    return count


cnt = []
for j in range(N):
    for i in range(N):
        if matrix[j][i] == 1:
            cnt.append(bfs(j, i, matrix))

cnt.sort()
print(len(cnt), *cnt, sep='\n')
