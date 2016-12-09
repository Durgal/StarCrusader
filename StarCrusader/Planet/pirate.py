#!/usr/bin/python

#########################################
# File:         pirate.py
# Author:       Chris Granat
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Provides main
#               functionality
#               for pirate class
#########################################

import pygame
import random
from item import *
from Utilities.sprite_functions import Sprite



class Pirate(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.type = "enemy"
        self.sprite = Sprite("Sprites/Pirate_Sheet.png", 44, 44)
        self.initial_x = x
        self.initial_y = y
        self.angle = 0
        self.direction = "R"
        self.speed = .0005

        self.image = self.sprite.get_image(0, 0)
        self.center_x = x - self.image.get_size()[0] / 2
        self.center_y = y - self.image.get_size()[1] / 2
        self.rect = self.image.get_rect()
        self.rect.x = self.center_x
        self.rect.y = self.center_y

    def get_pos(self):
        return(self.rect.x,self.rect.y)

    def animate(self, time, direction):
        self.image = self.sprite.get_image(0, 0)
        self.sprite.animate(time)
        self.direction = direction

        self.x = self.rect.x
        self.y = self.rect.y

    def change_direction(self):
        if self.direction == "R":
            self.direction = "L"
            self.speed = -.0005
        else:
            self.direction = "R"
            self.speed = .0005

        self.sprite.flip_image()

    def collision_check(self, laser_list, entity_list):
        for laser in laser_list:
            if self.sprite.get_collision(self.rect.x, self.rect.y, self.sprite.width, self.sprite.height, laser.rect.x, laser.rect.y, laser.sprite.width, laser.sprite.height):
                laser.kill()
                self.die(entity_list)

    def die(self, entity_list):
        self.kill()
        item_list = [Fuel(self.x,self.y),Health(self.x,self.y),Energy(self.x,self.y),Treasure(self.x,self.y)]
        entity_list.add(random.choice(item_list))


class Pirate_Spawner:

    def __init__(self,x,y,direction):
        self.initial_x = x
        self.initial_y = y
        self.direction = direction
        self.spawn_rate = 5000
        self.spawn_timer = 0

    def create(self, entity_list):
            pirate = Pirate(self.initial_x, self.initial_y)
            entity_list.add(pirate)

            if self.direction == "L":
                pirate.change_direction()

    def update(self, entity_list):
        time = pygame.time.get_ticks()
        if time - self.spawn_timer >= self.spawn_rate:
            self.spawn_timer = time
            self.create(entity_list)