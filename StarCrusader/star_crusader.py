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


class Game:
    def __init__(self):
        self.spaceship_group = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()

    def get_input(self, level_type, player):
        """ Input Function for both Universe and Planet Levels """
        if level_type == "universe":
            if pygame.key.get_pressed()[pygame.K_w] != 0:
                player.get_event('accelerate')
            if pygame.key.get_pressed()[pygame.K_a] != 0:
                player.get_event('rotate_l')
            if pygame.key.get_pressed()[pygame.K_d] != 0:
                player.get_event('rotate_r')
            if pygame.key.get_pressed()[pygame.K_SPACE] != 0:
                player.get_event('shoot')

        if level_type == "planet":  # TODO: this is just proof of concept
            if pygame.key.get_pressed()[pygame.K_a] != 0:
                player.move_left()
            if pygame.key.get_pressed()[pygame.K_d] != 0:
                player.move_right()

def main():
    """ Main Program """
    pygame.init()

    game_state = "universe"

    # Screen initialization
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Star Crusader")

    spaceship_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    # Set current level (Universe)
    current_level = level.Universe(screen, spaceship_group, asteroid_group)

    # Create Hero
    # player = Hero() # for planet

    # Set current level (Planet)
    # current_level = level.Planet(player) # for planet
    # player.level = current_level # for planet

    # sprite_list.add(player)

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
        # For Spaceship (comment out above draw function
        dt = milliseconds / MS
        current_level.set_dt(dt)

        # Checks for input based on player type (ship vs hero)
        current_level.get_input()

        # Update each sprite groups and current level
        spaceship_group.update()
        asteroid_group.update(spaceship_group)
        current_level.update()

        screen.fill(BLACK)
        current_level.render_level()

        # Update screen
        pygame.display.flip()


if __name__ == '__main__': main()
