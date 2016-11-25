#!/usr/bin/python

import pygame

from sprite_functions import Sprite


class Hero(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.change_x = 0
        self.change_y = 0

        sprite = Sprite("sprites/Hero.png")

        self.image = sprite.get_image(0,0,48,48)

        self.rect = self.image.get_rect()


    def update(self):

        self.rect.x += self.change_x


    def move_left(self):

        self.change_x = -1


    def move_right(self):

        self.change_x = 1


    def stop(self):

        self.change_x = 0