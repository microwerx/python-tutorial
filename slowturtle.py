# This is the slow version of the fibonacci turtle
# The asymptotics for this program is O(1.618^n)

from turtle import *
from math import *

def fib(n):
    if n <= 0:
        return 0
    elif n < 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

speed(0)
for x in range(35):
    forward(10 * log(1 + fib(x)))
    left(45)
