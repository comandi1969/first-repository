#import math

def power(x, n):
    return x ** n

def cubic(x):
    return x ** 3

def divide(x, y):
    if y == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    quotient = x // y
    reminder = x % y
    result = x / y
    return(f'몫:{quotient}, 나머지:{reminder}, 소수점:{result}')

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x -1)
