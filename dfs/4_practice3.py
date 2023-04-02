"""
음료수 얼려 먹기 dfs
1. 아이디어
1) stack에 인접한 상하좌우 0 넣기
2) 하나씩 꺼내면서 해당 원소의 상하좌우 중 0인 값 && 방문하지 않은 원소 stack에 넣기
3) 방문 횟수 += 1
"""

import sys

read = sys.stdin.readline
n, m = map(int, read().split(" "))
ice_box = [list(map(int, read().strip())) for _ in range(n)]
# 방문을 체크
visited_box = [[0 for _ in range(m)] for _ in range(n)]
stack = []

# 오른쪽 왼쪽 위쪽 아래쪽
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for j in range(n):
    for i in range(m):
        # 0이고 방문하지 않았으면 방문하고 stack에 넣기, 방문 처리 하기
        if visited_box[j][i] == 0 and ice_box[j][i] == 0:
            visited_box[j][i] = 1
            stack.append((j, i))
            print("초기", stack)
        # stack 값을 하나씩 꺼내면서 상하좌우를 돌기
        if stack:
            y, x = stack.pop()
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                # x, y가 얼음틀을 벗어나지 않는다면 stack에 해당 좌표 값 넣기
                if 0 <= ny < n and 0 <= nx < m and visited_box[ny][nx] == 0 and ice_box[ny][nx] == 0:
                    visited_box[ny][nx] = 1
                    stack.append((ny, nx))
            print("마지막", stack)
