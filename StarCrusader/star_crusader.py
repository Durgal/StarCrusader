#!/usr/bin/python

import pygame
from pygame.locals import *
import level
from hero import Hero


RED = (255, 0, 0)
YELLOW = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

HEIGHT = 900
WIDTH = 900
FPS = 60


def main():
    """ Main Program """
    pygame.init()

    # Screen initialization
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Star Crusader")

    # Create Spaceship
    #player = Spaceship()

    # Create Hero
    player = Hero()

    # Set current level (Planet or Universe)
    current_level = level.Planet(player)
    player.level = current_level

    # Load current level sprites
    sprite_list = pygame.sprite.Group()
    sprite_list.add(player)

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
        clock.tick(FPS)

        # TODO: get user input here? Or perhaps per level... (ie universe vs planet)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move_left()
            if event.key == pygame.K_d:
                player.move_right()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_d and player.change_x > 0:
                player.stop()

        # Update game entities
        sprite_list.update()

        # Draw current level
        current_level.draw(screen)

        # Draw level entities
        sprite_list.draw(screen)

        # Update screen
        pygame.display.flip()



if __name__ == '__main__': main()
