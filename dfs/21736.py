"""
헌내기는 친구가 필요해
=> 벽을 만나지 않는 이상 계속 전진

1) I를 먼저 찾음
2) matrix를 벗어나지 않는 한도 안에서 I 이동
3) 벽을 만나지 않으면 이동 가능
4) P를 만나면 count +1
"""

import sys

read = sys.stdin.readline
N, M = map(int, read().split(" "))
matrix = [list(read().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
count = 0
stack = []

# 위 아래 오 왼
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for n in range(N):
    for m in range(M):
        if matrix[n][m] == 'I':
            stack.append((n, m))
            visited[n][m] = 1

while stack:
    y, x = stack.pop()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        elif matrix[ny][nx] == 'O' and visited[ny][nx] == 0:
            stack.append((ny, nx))
            visited[ny][nx] = 1
        elif matrix[ny][nx] == 'P' and visited[ny][nx] == 0:
            count += 1
            stack.append((ny, nx))
            visited[ny][nx] = 1

print(count if count > 0 else "TT")
