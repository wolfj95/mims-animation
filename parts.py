from turtle import setheading, color, begin_fill, left, forward, right, end_fill, circle
from helpers import restore_state_when_finished

import math

def draw_triangle(side_len, color_name):
    #This function draws an equilateral triangle
    with restore_state_when_finished():
        color(color_name)
        begin_fill()
        for i in range(3):
            forward(side_len)
            right(120)
        end_fill()

def customized_circle(size, color_name):
    color(color_name)
    begin_fill()
    circle(size)
    end_fill()
