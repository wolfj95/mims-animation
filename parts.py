from turtle import setheading, color, begin_fill, left, forward, right, end_fill, circle
from helpers import restore_state_when_finished

import math

def draw_triangle(sideLength, colorname):
    #This function draws an equilateral triangle
    with restore_state_when_finished():
        color(colorname)
        begin_fill()
        for i in range(3):
            forward(sideLength)
            right(120)
        end_fill()


def customized_circle(size, colorname):
    color(colorname)
    begin_fill()
    circle(size)
    end_fill()
