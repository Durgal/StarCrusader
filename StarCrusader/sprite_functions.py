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

dFPS = 10


class Sprite(object):

    def __init__(self,file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
        self.current_sprite = 0
        self.number_sprite = 4

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (x, y), (self.current_sprite*width, 0, width, height))
        image.set_colorkey(BLACK)
        return image

    def flip_image(self):
        self.sprite_sheet = pygame.transform.flip(self.sprite_sheet, True, False)

    def animate(self, time):
        if time % dFPS == 0:
            if self.current_sprite >= self.number_sprite - 1:
                self.current_sprite = 0
            else:
                self.current_sprite += 1

    def get_center(self, x, y, width, height):
        return (x - width/2, y - height/2)

    def set_sprite(self, num):
        self.current_sprite = num