"""
최댓값
"""
import sys

read = sys.stdin.readline
numbers = [int(read()) for _ in range(9)]
max_num = 0
index = 0

for i in range(9):
    if numbers[i] > max_num:
        max_num = numbers[i]
        index = i + 1

print(max_num, index, sep='\n')