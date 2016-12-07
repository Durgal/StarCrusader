#!/usr/bin/python

#########################################
# File:         ship_landed.py
# Author:       Chris Granat
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Landed spaceship class
#########################################

import pygame

from Utilities.sprite_functions import Sprite


class Ship_Landed(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.type = "ship"
        self.sprite = Sprite("Sprites/Spaceship_Planet.png", 270, 270)
        self.initial_x = x
        self.initial_y = y
        self.speed = 0
        self.angle = 0

        self.image = self.sprite.get_image(0, 0)
        self.center_x = x - self.image.get_size()[0] / 2
        self.center_y = y - self.image.get_size()[1] / 2
        self.rect = self.image.get_rect()
        self.center = self.rect.center
        self.rect.x = self.center_x
        self.rect.y = self.center_y

        self.orig_center = self.rect.center
        self.orig_img = self.image
        self.rotation = 0

    def get_pos(self):
        return(self.rect.x,self.rect.y)

    def rotate(self, angle):
        self.rotation = angle
        self.image = pygame.transform.rotate(self.orig_img, self.rotation)
        self.rect = self.image.get_rect(center=self.rect.center)