#!/usr/bin/python

#########################################
# File:         laser.py
# Author:       Chris Granat
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Provides main
#               functionality
#               for laser class
#########################################

import pygame

from Utilities.sprite_functions import Sprite


class Laser(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.type = "laser"
        self.sprite = Sprite("Sprites/Hero_Laser.png", 4, 44)
        self.initial_x = x
        self.initial_y = y
        self.speed = 0
        self.angle = 0

        self.image = self.sprite.get_image(0, 0)
        self.center_x = x - self.image.get_size()[0] / 2
        self.center_y = y - self.image.get_size()[1] / 2
        self.rect = self.image.get_rect()
        self.rect.x = self.center_x
        self.rect.y = self.center_y

    def get_pos(self):
        return(self.rect.x,self.rect.y)

    def set_direction(self, direction):
        if direction == "R":
            self.speed = .005
        else:
            self.speed = -.005