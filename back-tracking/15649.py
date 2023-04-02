"""
n과 m(1)

"""
import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split(" "))
numbers = []

for i in range(1, n+1):
    numbers.append(i)

for perm in permutations(numbers, m):
    print(" ".join([str(x) for x in perm]))
