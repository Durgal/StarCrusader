#!/usr/bin/python

import pygame
from pygame.locals import *
import level
from hero import Hero
from spaceship import Spaceship
from spaceship import Camera
from asteroid import Asteroid


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
    pygame.init()

    # Screen initialization
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Star Crusader")

    #spaceship_group = pygame.sprite.Group()
    #asteroid_group = pygame.sprite.Group()

    # Set current level (Universe)
    #current_level = level.Universe(screen, spaceship_group, asteroid_group)

    # Set current level (Planet)
    current_level = level.Planet(screen)

    #sprite_list.add(player)

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

        # For Spaceship ... TODO: move this inside ship class or level if possible... low priority though
        dt = milliseconds / MS
        current_level.set_dt(dt)

        # Checks for input based on player type (ship vs hero)
        current_level.get_input()

        # Update each sprite groups and current level
        #spaceship_group.update()                #TODO: move these two functions to current_level.update()?
        #asteroid_group.update(spaceship_group)  #TODO: move these two functions to current_level.update()?
        current_level.update()

        screen.fill(BLACK)
        current_level.render_level()

        # Update screen
        pygame.display.flip()


if __name__ == '__main__': main()
