"""
거스름돈
"""

import sys

n = int(sys.stdin.readline().rstrip())

# 잔돈
change = n
# 동전 개수
result = 0
# 동전 리스트
coin_list = [500, 100, 50, 10]


def math_coin(coin_value, init_n):
    share = init_n // coin_value
    change = init_n - (share * coin_value)
    return change, share


for i in coin_list:
    change, share = math_coin(i, change)
    result += share

print(result)