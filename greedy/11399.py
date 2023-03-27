"""
ATM

1. 아이디어
1) 적은 사람일수록 앞자리 배치
2) sum += i * n - i
"""

import sys
read = sys.stdin.readline
# 사람의 수
n = int(read())
# 각 사람이 돈을 인출하는데 걸리는 시간
time_list = list(map(int, read().split(' ')))
time_list.sort()

sum = 0
for i in range(n):
    sum += time_list[i] * (n-i)

print(sum)