"""
위에서 아래로
"""

import sys

read = sys.stdin.readline

n = int(read())
num_list = sorted([int(read().rstrip()) for _ in range(n)], reverse=True)
print(num_list)
