#!/usr/bin/python

import pygame
from pygame.locals import *
from spaceship import *
from universe import Universe


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Star Crusader")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    white_asteroid1 = 'Sprites/whiteAsteroid1.png'
    white_asteroid2 = 'Sprites/whiteAsteroid2.png'
    white_asteroid3 = 'Sprites/whiteAsteroid3.png'

    universe = Universe('Universe/universe_test.txt', white_asteroid1, white_asteroid2, white_asteroid3)
    spaceship = Spaceship()

    universe.create_random_universe()
    universe.__read_file__('Universe/universe_test.txt')

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        if pygame.key.get_pressed()[pygame.K_w] != 0:
            spaceship.update()

        screen.blit(background, (0, 0))
        universe.draw_asteroids(screen)
        spaceship.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()
