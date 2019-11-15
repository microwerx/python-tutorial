# This is a fun little program that illustrates
# Turtle Graphics

from turtle import *

forward(10)
left(90)
forward(10)
left(90)
forward(20)
left(90)
forward(30)
left(90)

speed(0)
for i in range(100):
    left(15)
    forward(i+10)
