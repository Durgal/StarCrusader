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
from gameplay import Gameplay


HEIGHT = 900
WIDTH = 900
FPS = 60


def main():
    """ Main Program """
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()

    # Screen initialization
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Star Crusader")

    # Initialize gameplay
    game = Gameplay(screen)

    # Start game clock
    clock = pygame.time.Clock()

    # End loop condition
    loop = True

    # ======== Main Game Loop ========
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False

        # Check for level change
        game.change_level()

        # Limit to 60 FPS
        game.set_fps(FPS,clock)

        # Checks for input based on player type (ship vs hero)
        game.get_input()

        # Update each sprite groups in current level
        game.update()

        # Render level
        game.render_level(clock.get_fps())

        # Update screen
        pygame.display.flip()


if __name__ == '__main__': main()
