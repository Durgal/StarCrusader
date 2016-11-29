#!/usr/bin/python

import pygame
import math
from sprite_functions import Sprite


STARTING_POS_X = 450
STARTING_POS_Y = 655


class Hero(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        sprite = Sprite("sprites/Hero.png")
        self.change_x = 0
        self.change_y = 0
        self.direction = 0
        self.image = sprite.get_image(0, 0, 48, 48)
        self.rect = self.image.get_rect()
        self.rect.x = STARTING_POS_X - self.image.get_size()[0]/2
        self.rect.y = STARTING_POS_Y - self.image.get_size()[1]/2


    def get_pos(self):
        return(self.rect.x,self.rect.y)

    def update(self):

        self.rect.x += self.change_x
        self.rect.y += self.change_y


    def move_left(self):

        self.change_x = -1


    def move_right(self):

        self.change_x = 1


    def stop(self):

        self.change_x = 0

