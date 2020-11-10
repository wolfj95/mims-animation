from turtle import Screen, clear, forward, penup, pendown
from parts import draw_triangle, customized_circle
from helpers import update_position, restore_state_when_finished, setup
import settings
import time

def animate_translate(num_frames, sidelen, color, sleeptime):
    for i in range(num_frames):
        if i < num_frames // 2:
            forward(1)
        if i > num_frames // 2:
            penup()
            forward(-1)
            pendown()
        draw_triangle(sidelen, color)
        screen.update()
        time.sleep(sleeptime)
        clear()

def main():
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)

    for i in range(settings.NUMREPEATS):
        setup(settings.START_X,settings.START_Y)
        animate(settings.NUMFRAMES, settings.SIDELEN, settings.COLOR, settings.SLEEPTIME)
    input("Press enter...")

if __name__ == '__main__':
    main()
