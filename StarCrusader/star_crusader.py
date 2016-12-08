#!/usr/bin/python

#########################################
# Project:      Star Crusader
# Author:       Group 6
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Main game loop
#########################################

import pygame
from pygame.locals import *
import level


RED = (255, 0, 0)
YELLOW = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

HEIGHT = 900
WIDTH = 900
FPS = 60
MS = 1000


def main():
    """ Main Program """
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()

    # Screen initialization
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Star Crusader")

    # Set current level (Universe)
    current_level = level.Universe(screen)

    # Set current level (Planet)
    #current_level = level.Planet(screen)

    # Clock manages how fast updates occur
    clock = pygame.time.Clock()

    # End loop condition
    loop = True

    # ======== Main Game Loop ========
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False

        # Limit to 60 FPS
        milliseconds = clock.tick(FPS)

        # For Spaceship
        dt = milliseconds / MS
        current_level.set_dt(dt)

        # Checks for input based on player type (ship vs hero)
        current_level.get_input()

        # Update each sprite groups and current level
        current_level.update()

        screen.fill(BLACK)
        current_level.render_level(clock.get_fps())

        # Update screen
        pygame.display.flip()


if __name__ == '__main__': main()
