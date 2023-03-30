import pygame as py, sys
from settings import * # * means bring all values from file
from level import Level
from player import Player
py.init() # Initialise Pygame
screen = py.display.set_mode((screen_width,screen_height)) # Screen dimensions, width/height
clock = py.time.Clock() # Ensures consistent performance across devices
level = Level(level_map, screen)
while True:
    # Will quit pygame when user clicks button to close window
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit() # Will quit pygame
            sys.exit() # 'sys' used to exit program
    screen.fill("black")
    level.run()
    py.display.update() # Will refresh screen for user

    clock.tick(fps) # Number of times the loop will run_right per second

