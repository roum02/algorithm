"""
미로탈출
"""
import sys

read = sys.stdin.readline

n, m = map(int, read().split(" "))
map_list = [list(map(int, read().rstrip())) for _ in range(n)]

