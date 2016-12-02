#!/usr/bin/python

#########################################
# File:         sprite_functions.py
# Author:       Chris Granat
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Provides main
#               functionality
#               for sprite class
#########################################

import pygame

RED = (255, 0, 0)
YELLOW = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255,75, 255)

mFPS = 10


class Sprite(object):

    def __init__(self,file_name, w, h):
        self.sprite_sheet = pygame.image.load(file_name).convert()
        self.current_sprite = 0
        self.number_sprite = 4
        self.width = w
        self.height = h

    def get_image(self, x, y):
        image = pygame.Surface([self.width, self.height]).convert()
        image.blit(self.sprite_sheet, (x, y), (self.current_sprite*self.width, 0, self.width, self.height))
        image.set_colorkey(PINK)
        return image

    def flip_image(self):
        self.sprite_sheet = pygame.transform.flip(self.sprite_sheet, True, False)

    def animate(self, time):
        if time % mFPS == 0:
            if self.current_sprite >= self.number_sprite - 1:
                self.current_sprite = 0
            else:
                self.current_sprite += 1

    def get_center(self, x, y, width, height):
        return (x - width/2, y - height/2)

    def set_sprite(self, num):
        self.current_sprite = num

    def get_collision(self, x1, y1, w1, h1, x2, y2, w2, h2):
        if (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2):
            return True
        elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2):
            return True
        elif (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
            return True
        elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
            return True
        else:
            return False