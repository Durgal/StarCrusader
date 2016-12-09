#!/usr/bin/python

#########################################
# File:         universe_planet.py
# Author:       Michael
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Provides functionality
#               for the planets class
#########################################

import pygame
import random


class UniversePlanet(pygame.sprite.Sprite):
    def __init__(self, sprite_group, x, y, image):
        self.group = sprite_group
        pygame.sprite.Sprite.__init__(self, self.group)
        self.x = x
        self.y = y

        self.image = image
        self.rect = self.image.get_rect()
        self.position = (self.x, self.y)
        self.rect.center = self.position

    def update(self, spaceship_group, laser_group):
        for sprite in spaceship_group:
            if pygame.sprite.collide_mask(self, sprite):
                sprite.level = "planet"
