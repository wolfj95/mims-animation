from turtle import Screen, clear
from parts import draw_triangle, customized_circle
from helpers import update_position, restore_state_when_finished, setup
import settings
import time

def draw_animation(num_frames, radius, speedfactor, color, sleeptime):
    for i in range(num_frames//2):
        new_size = radius + i*speedfactor
        customized_circle(new_size, color)
        screen.update()
        time.sleep(sleeptime)
        clear()

    max_size = radius + num_frames//2*speedfactor

    for j in range(num_frames//2):
        new_size = max_size - j*speedfactor
        customized_circle(new_size, color)
        screen.update()
        time.sleep(sleeptime)
        clear()

def main():
    for i in range(settings.NUMREPEATS):
        setup(settings.START_X,settings.START_Y)
        draw_animation(settings.NUMFRAMES, settings.RADIUS, settings.SPEEDFACTOR, settings.COLOR, settings.SLEEPTIME)
    input("Press enter...")

if __name__ == '__main__':
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)
    main()
