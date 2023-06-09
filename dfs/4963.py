"""
섬의 개수

=> 1은 땅, 0은 바다
=> 가로, 세로, 대각선 연결은 하나의 땅
=> 땅의 개수 구하기
"""

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(y, x):
    if -1 >= y or h <= y or -1 >= x or w <= x:
        return False
    if visited[y][x] == 0 and matrix[y][x] == 1:
        visited[y][x] = 1
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x + 1)
        dfs(y, x - 1)
        dfs(y + 1, x + 1)
        dfs(y + 1, x - 1)
        dfs(y - 1, x + 1)
        dfs(y - 1, x - 1)
        return True
    return False


while True:
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, read().split(" "))) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    count = 0

    for j in range(h):
        for i in range(w):
            if dfs(j, i):
                count += 1

    print(count)
