#!/usr/bin/python

#########################################
# File:         hero.py
# Author:       Chris Granat
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Provides main
#               functionality
#               for hero class
#########################################

import pygame
from sprite_functions import Sprite


STARTING_POS_X = 450
STARTING_POS_Y = 655


class Hero(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.sprite = Sprite("Sprites/Hero_Sheet.png")
        self.sprite_stopped = Sprite("Sprites/Hero.png")
        self.angle = 0
        self.velocity = 0
        self.gravity = 0
        self.on_ground = True
        self.direction = "R"

        self.image = self.sprite.get_image(0, 0, 44, 44)
        self.center_x = STARTING_POS_X - self.image.get_size()[0] / 2
        self.center_y = STARTING_POS_Y - self.image.get_size()[1] / 2
        self.rect = self.image.get_rect()
        self.rect.x = self.center_x
        self.rect.y = self.center_y

    def get_pos(self):
        return(self.rect.x,self.rect.y)

    def move(self, time, direction):
        old_direction = self.direction

        if old_direction != direction:
            self.sprite.flip_image()

        self.image = self.sprite.get_image(0, 0, 44, 44)
        self.sprite.animate(time)
        self.direction = direction

    def jump(self):
        self.velocity = 0

    def stop(self ,time):
        if self.sprite.current_sprite != 0:
            self.sprite.animate(time)
        else:
            self.image = self.sprite_stopped.get_image(0, 0, 44, 44)

    def update(self):
        if self.velocity < 0:
            self.falling = True



        self.velocity += self.gravity
        self.rect.y -= self.velocity