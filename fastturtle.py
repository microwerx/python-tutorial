# This program uses a faster version of the Fibonacci sequence
# which is O(n)

from turtle import *
from math import *

def fib(n):
    if n <= 0:
        return 0
    elif n < 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def fib2(n):
    if n <= 0:
        return 0
    elif n < 2:
        return 1
    f2 = 0
    f1 = 1
    for i in range(n-1):
        f = f1 + f2
        f2 = f1
        f1 = f
    return f

speed(0)
for x in range(100):
    forward(10 * log(1 + fib2(x)))
    left(45)
    print(x)

# test code
print('F(0) = ',fib2(0))
print('F(1) = ',fib2(1))
print('F(2) = ',fib2(2))
print('F(3) = ',fib2(3))
print('F(4) = ',fib2(4))
print('F(5) = ',fib2(5))
print('F(6) = ',fib2(6))
