"""
숫자 카드 게임
-> 가장 높은 숫자 카드 한 장 뽑아야 한다
각 행 중 가장 낮은 카드를 뽑아야 함

이중 리스트 돌면서 가장 낮은 값들 비교
해당 값들 중 가장 높은 값이 정답
"""
import sys
read = sys.stdin.readline
n, m = map(int, read().split(' '))
card_lists = [list(map(int, read().split(' '))) for _ in range(n)]
min_list = []

for list in card_lists:
    min = 100000
    for i in list:
        if i < min:
            min = i
    min_list.append(min)

print(max(min_list))
