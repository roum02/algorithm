"""
단지번호 붙이기
"""

import sys

read = sys.stdin.readline
N = int(read())
matrix = [list(map(int, read().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = 0


def dfs(y, x):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if visited[y][x] == 0:
        visited[y][x] = 1
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x + 1)
        dfs(y, x - 1)
        return True
    return False


for j in range(N):
    for i in range(N):
        if dfs(j, i):
            result += 1

print(result)
