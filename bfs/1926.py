"""
1. 아이디어
- 2중 for => 값 1 && 방문X => BFS
- BFS 돌면서 그림 개수 +1, 최대값을 갱신

2. 시간복잡도
- BFS : O(V+E)
- V = mn = 500 * 500
- E = 4V
- V+E : 5 * 250000 = 1000만

3. 자료구조
- 그래프 전체 지도: int[][]
- 방문: bool[][]
- Queue(BFS)
"""

import sys

read = sys.stdin.readline
n, m = map(int, read().split())
map = [list(map(int, read().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

cnt = 0
maxv = 0

# 방향은 암기
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y,x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            # 그림 사이즈 넘어가면 안됨
            if 0<=ny<n and 0<=nx<m:
                # 만약 방문하지 않은 경우에는
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return rs

# 보통 이중 for 문은 y를 먼저 돌고 x를 도는 형식
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체 그림 갯수를 +1
            cnt += 1
            # BFS > 그림 크기
            # 최대값 갱신
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)