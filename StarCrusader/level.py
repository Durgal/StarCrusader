#!/usr/bin/python

import pygame

RED = (255, 0, 0)
YELLOW = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Level():

    def __init__(self, player):

        self.background = None
        self.type = None
        self.player = player

    def draw(self, screen):

        screen.fill(BLACK)

        if self.background:
            screen.blit(self.background, (0,0))

    def get_type(self):

        return self.type


class Planet(Level):

    def __init__(self, player):

        Level.__init__(self, player)

        self.type = "planet"

        self.background = pygame.image.load("sprites/planet.png").convert()


class Universe(Level):

    def __init__(self, player):

        Level.__init__(self, player)

        self.type = "universe"
