"""
미로탈출
"""
import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split(" "))
matrix = [list(map(int, read().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 > ny or ny >= n or 0 > nx or nx >= m:
                continue
            if matrix[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))

    return visited[n-1][m-1]


print(bfs(0, 0))
