"""
시각
=> 정수 n이 입력되면 00시 00분 00초 부터 n시 59분 59초까지
모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수

0~n 시에 3이 들어가는 경우의 수: for i in range(n+1): if i.find('3') != -1 : count += 1
"""

import sys

n = int(sys.stdin.readline())
count = 0

for hour in range(n + 1):
    for minute in range(0, 60):
        for sec in range(0, 60):
            # 더 간단한 로직으로 수정
            if '3' in str(hour) + str(minute) + str(sec):
                count += 1

print(count)
