#!/usr/bin/python

#########################################
# File:         item.py
# Author:       Chris Granat
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Provides main
#               functionality
#               for item class
#########################################

import pygame

from Utilities.sprite_functions import Sprite


class Item(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.type = "item"
        self.sprite = Sprite("Sprites/Item_Parent.png", 36, 36)
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


class Fuel(Item):

    def __init__(self, x, y):

        super().__init__(x, y)
        self.sub_type = "fuel"
        self.sprite = Sprite("Sprites/Item_Fuel.png", 36, 36)
        self.image = self.sprite.get_image(0, 0)

class Health(Item):

    def __init__(self, x, y):

        super().__init__(x, y)
        self.sub_type = "health"
        self.sprite = Sprite("Sprites/Item_Health.png", 36, 36)
        self.image = self.sprite.get_image(0, 0)

class Energy(Item):

    def __init__(self, x, y):

        super().__init__(x, y)
        self.sub_type = "treasure"
        self.sprite = Sprite("Sprites/Item_Energy.png", 36, 36)
        self.image = self.sprite.get_image(0, 0)

class Treasure(Item):

    def __init__(self, x, y):

        super().__init__(x, y)
        self.type = "treasure"
        self.sprite = Sprite("Sprites/Item_Treasure.png", 36, 36)
        self.image = self.sprite.get_image(0, 0)