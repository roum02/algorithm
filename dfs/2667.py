"""
단지번호붙이기
"""

import sys

read = sys.stdin.readline
N = int(read())
matrix = [list(map(int, read().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# def count_apartment(y, x):
#     stack = []

# 위 아래 오 왼
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

stack = []
apartment_count = 0

for y in range(N):
    for x in range(N):
        if matrix[y][x] != 0 and visited[y][x] == 0:
            stack.append((y, x))
            visited[y][x] = 1

            while stack:
                sy, sx = stack.pop()
                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dy[d]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    elif matrix[sy][sx] != 0 and visited[sy][sx] == 0:
                        stack.append((sy, sx))
                        visited[sy][sx] = 1





# print(apartment_count)