"""
왕실의 나이트
1) x, y축 범위 벗어나는지 체크
2) 2가지 경우의 수로 이동해보기
3) 이동 가능한 count 출력
"""

import sys

location = sys.stdin.readline()
x, y = (ord(location[0]) - 96), int(location[1])
count = 0


def search(current_x, current_y, dx, dy):
    global count
    for i in range(4):
        nx = current_x + dx[i]
        ny = current_y + dy[i]
        if 0 < nx <= 8 and 0 < ny <= 8:
            count += 1
    return count


search(x, y, [2, 2, -2, -2], [1, -1, 1, -1])
search(x, y, [1, -1, 1, -1], [2, 2, -2, -2])
print(count)