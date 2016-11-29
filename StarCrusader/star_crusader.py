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


def get_input(level_type, player):
    """ Input Function for both Universe and Planet Levels """
    if level_type == "universe":
        if pygame.key.get_pressed()[pygame.K_w] != 0:
            player.get_event('accelerate')
        if pygame.key.get_pressed()[pygame.K_a] != 0:
            player.get_event('rotate_l')
        if pygame.key.get_pressed()[pygame.K_d] != 0:
            player.get_event('rotate_r')

    if level_type == "planet": # TODO: this is just proof of concept
        if pygame.key.get_pressed()[pygame.K_a] != 0:
            player.move_left()
        if pygame.key.get_pressed()[pygame.K_d] != 0:
            player.move_right()


def main():
    """ Main Program """
    pygame.init()

    # Screen initialization
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Star Crusader")

    # Create Spaceship
    #player = Spaceship()
    #camera = Camera(WIDTH, HEIGHT)

    # Set current level (Universe)
    #current_level = level.Universe(player)

    # Create Hero
    player = Hero() # for planet

    # Set current level (Planet)
    current_level = level.Planet(player) # for planet
    player.level = current_level # for planet

    # Load current level sprites
    sprite_list = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    sprite_list.add(player)
    level.Universe(player).add_asteroids(asteroid_group)

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

        # Checks for input based on player type (ship vs hero)
        get_input(current_level.get_type(), player)  # TODO: Perhaps move to level...? (ie universe vs planet)

        # Update game entities
        sprite_list.update()
        asteroid_group.update()
        #camera.update(player)  # only for universe

        # Draw current level
        current_level.draw(screen)

        # Draw level entities
        sprite_list.draw(screen)

        # For Spaceship (comment out above draw function
        #dt = milliseconds / MS
        #player.set_dt(dt)

        #for asteroid in asteroid_group:
        #    screen.blit(asteroid.image, camera.apply(asteroid))

        #for sprite in sprite_list:
        #    screen.blit(sprite.image, camera.apply(sprite))

        #player.debugging(screen, clock.get_fps())

        # Update screen
        pygame.display.flip()


if __name__ == '__main__': main()
