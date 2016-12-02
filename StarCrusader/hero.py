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
        self.sprite = Sprite("Sprites/Hero_Sheet.png", 44, 44)
        self.sprite_stopped = Sprite("Sprites/Hero.png", 44, 44)
        self.angle = 0
        self.velocity = 0
        self.gravity = -.25
        self.collision = False
        self.on_ground = False
        self.falling = False
        self.move_speed = 0
        self.direction = "R"

        self.image = self.sprite.get_image(0, 0)
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

        self.image = self.sprite.get_image(0, 0)
        self.sprite.animate(time)
        self.direction = direction

        if (direction == "R"):
            self.move_speed = -.5
        else:
            self.move_speed = .5

    def jump(self):
        if self.on_ground == True:
            self.velocity = 6

    def stop(self ,time):
        self.move_speed = 0
        if self.sprite.current_sprite != 0:
            self.sprite.animate(time)
        else:
            self.image = self.sprite_stopped.get_image(0, 0)

    def update(self, object, ground):
        if self.velocity < 0:
            self.falling = True

        collision = self.collision = self.sprite.get_collision(self.rect.x, self.rect.y, self.sprite.width, self.sprite.height, ground.rect.x, ground.rect.y, ground.sprite.width, ground.sprite.height)

        if collision == False:
            self.on_ground = False

        # if player touches ground stop
        if collision == True:
            if self.falling == True:
                self.falling = False
                self.on_ground = True
                self.velocity = 0

        # fall if on ground, else snap to position
        if self.on_ground == False:
            self.velocity += self.gravity
        else:
            self.rect.y = self.center_y

        self.rect.y -= self.velocity


