"""
그룹 단어 체커
"""

import sys

read = sys.stdin.readline

N = int(read())
count = 0


def checker(text):
    dictionary = {}
    prep = []
    for i in text:
        prep.append(i)
        if len(prep) > 1 and prep[-2] == i:
            prep.pop()

    for j in prep:
        if j in dictionary.keys():
            return False
        else:
            dictionary[j] = 1
    return True


for _ in range(N):
    if checker(read()):
        count += 1


print(count)
