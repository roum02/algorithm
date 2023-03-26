"""
큰 수의 법칙
1. 아이디어
: m번 더해서 가장 큰 수를 만들되, k번 초과하여 더해질 수 없다

k번 동안 리스트 중 가장 큰 수를 더하고
k번이 초과되면 그 다음 큰 수를 더한다
-> 이거 m번 반복
"""
import sys
read = sys.stdin.readline
n, m, k = map(int, read().split(' '))
numbers = list(map(int, read().split(' ')))
numbers.sort(reverse=True)
sum_value = 0
n = 0


for i in range(m):
    if n < k:
        sum_value += numbers[0]
        n += 1
    else:
        sum_value += numbers[1]
        n = 0

print(sum_value)