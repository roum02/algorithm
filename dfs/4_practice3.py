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

for y in range(n):
    for x in range(m):
        # 0이고 방문하지 않았으면
        if visited_box[y][x] == 0 and ice_box[y][x] == 0:
            # 상하좌우를 돌면서 stack에 넣기
            # 리펙토링 생각해보기
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                # x, y가 얼음틀을 벗어나지 않는다면 stack에 넣기
                if 0 < ny < n and 0 < nx < m:
                    stack.append(ice_box[y][x])

