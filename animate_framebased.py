from turtle import  Screen, clear
from parts import draw_triangle
from helpers import update_position, setup
import settings
import time

def animate_framebased(num_frames, sidelen, color, sleeptime):
    for i in range(num_frames):
        if i == num_frames/4:
            draw_triangle(sidelen, color)
        if i == num_frames/2:
            update_position(100, 0)
            draw_triangle(sidelen, color)
        if i == 3*num_frames/4:
            update_position(200, 0)
            draw_triangle(sidelen, color)
        if i == num_frames:
            update_position(100, 0)
            draw_triangle(sidelen, color)
        screen.update()
        time.sleep(sleeptime)
    clear()


if __name__ == '__main__':
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)

    for i in range(settings.NUMREPEATS):
        setup(settings.START_X,settings.START_Y)
        animate_framebased(settings.NUMFRAMES, settings.SIDELEN, settings.COLOR, settings.SLEEPTIME)
    input("Press enter...")
