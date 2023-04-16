"""
바이러스
1) 보균자와 연관되어 있는 애들 queue 저장
2) queue 없어질 동안 계속 감염된 애들 queue에 저장
3) 토탈 카운트 세기
=> 시간 많이 걸릴 것 같긴 함..

2. hash로 정렬할 수 있지 않을까?

1) 1과 연관된 애들을 queue에 넣기
2) q에서 하나 빼서 그거랑 관련된 애들 또 q에 넣기
3) q 가 비었으면 토탈 count
"""

import sys
from collections import deque

read = sys.stdin.readline
computers = int(read())
# 컴퓨터 쌍의 개수
n = int(read())
networks = [list(map(int, read().split(" "))) for _ in range(n)]


def solution(carrier):
    queue = deque()
    queue.append(carrier)
    while queue:
       x = queue.popleft()



solution(1)
