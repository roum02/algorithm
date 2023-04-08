"""
재귀적으로 구현한 팩토리얼
n! = 1 * 2 * .... * (n-1)
"""

answer = 1


def factorial_recursive(n):
    global answer
    # 종료조건
    if n == 0:
        return
    else:
        answer *= n
        factorial_recursive(n - 1)


# factorial_recursive(3)
# print(answer)

"""
수정된 버전
"""


def factorial_recursive2(n):
    if n <= 1:
        return 1
    return n * factorial_recursive2(n - 1)
