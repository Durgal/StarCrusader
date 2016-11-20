#!/usr/bin/python

import pygame


SPACESHIP_CENTER_X = 365
SPACESHIP_CENTER_Y = 373


class Spaceship:
    def __init__(self, spaceship_sprite='Sprites/spaceship.png'):
        self._x = SPACESHIP_CENTER_X
        self._y = SPACESHIP_CENTER_Y

        try:
            self.spaceship_sprite = pygame.image.load(spaceship_sprite)

        except pygame.error as message:
            print("Can't load spaceship: ", spaceship_sprite)
            raise message

    def draw(self, screen):
        screen.blit(self.spaceship_sprite, (self._x, self._y))

    def update(self):
        self._y -= 1
