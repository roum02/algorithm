"""
강의실 배정

1. 아이디어
시간 리스트를 받아서 시작 시간이 작은 숫자로 정렬

우선순위 queue에 회의의 끝 시간 넣기
if 다음 회의의 시작 시간이 같거나 크면 기존 회의실 : pop && push (가장 작은 원소 삭제) => 회의가 끝나는 시간이 업데이트 되기 때문
else 작으면 새로운 회의실에 넣기 push
"""

import sys
import heapq

read = sys.stdin.readline

# 수업의 개수
n = int(read())

# 시간 리스트 입력 받은 후 정렬
time_list = [list(map(int, read().split(' '))) for _ in range(n)]
time_list.sort(key=lambda x: x[0])

# 강의의 끝 시간이 입력될 queue
q = []
heapq.heappush(q, 0)

for class_time in time_list:
    # 기존 회의실 사용의 경우
    if q[0] <= class_time[0]:
        heapq.heappush(q, class_time[1])
        heapq.heappop(q)
    # 새로운 회의실 사용의 경우
    else:
        heapq.heappush(q, class_time[1])


print(len(q))
