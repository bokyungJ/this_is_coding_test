# 5-5) 2가지 방식으로 구현한 팩토리얼 예제

# 1. 반복적으로 구현한 n!
def factorial_iterative(n):
    result=1
    # 1부터 n까지 차례대로 곱하기
    for i in range(1,n+1):
        result *= i
    return result

# 2. 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n<=1:
        return 1
    # n! = n * (n-1)! 그대로 구현하기
    return n * factorial_recursive(n-1)

print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))