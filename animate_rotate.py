from turtle import Screen, clear, right
from parts import draw_triangle
from helpers import update_position, setup
import settings
import time

def draw_animation(num_frames, sidelen, color, sleeptime):
    for i in range(num_frames):
        if i < num_frames//3:
            right(1)
            draw_triangle(sidelen, color)
        if i > num_frames//3 and i < 2*num_frames//3:
            right(5)
            draw_triangle(sidelen,color)
        if i > 2*num_frames//3:
            right(i)
            draw_triangle(sidelen, color)
        screen.update()
        time.sleep(sleeptime)
        clear()


def main():
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)

    for i in range(settings.NUMREPEATS):
        setup(settings.START_X,settings.START_Y)
        draw_animation(settings.NUMFRAMES, settings.SIDELEN, settings.COLOR, settings.SLEEPTIME)
    input("Press enter...")
if __name__ == '__main__':
    main()
