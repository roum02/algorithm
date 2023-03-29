"""
상하좌우
4사분면이라서, U가 -1
"""

import sys

read = sys.stdin.readline

n = int(read())
plan_list = read().split()

dictionary = {"L": [-1, 0], "R": [1, 0], "U": [0, -1], "D": [0, 1]}

y, x = 1, 1

for plan in plan_list:
    # 앞으로 나아갈 방향
    nx = x + dictionary[plan][0]
    ny = y + dictionary[plan][1]
    if n < nx or nx < 1 or n < ny or ny < 1:
        pass
    else:
        x = nx
        y = ny

print(y, x)
