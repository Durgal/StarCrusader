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

from Utilities.sprite_functions import Sprite
from laser import Laser
from Utilities.audio_functions import Audio

STARTING_POS_X = 450
STARTING_POS_Y = 655

#Audio
snd_jump = "Audio/jump.wav"

PLAYER_SPEED = .0015

class Hero(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.sprite = Sprite("Sprites/Hero_Sheet.png", 44, 44)
        self.sprite_stopped = Sprite("Sprites/Hero.png", 44, 44)
        self.sprite_shoot_l = Sprite("Sprites/Hero_Shoot_L.png", 44, 44)
        self.sprite_shoot_r = Sprite("Sprites/Hero_Shoot_R.png", 44, 44)
        self.angle = 0
        self.velocity = 0
        self.gravity = -.25
        self.collision_entity = None
        self.collision = False
        self.on_ground = False
        self.falling = False
        self.laser_timer = 0
        self.laser_cooldown = 300
        self.move_speed = 0
        self.direction = "R"

        self.fuel = 0
        self.health = 0
        self.energy = 0
        self.treasure = 0

        self.image = self.sprite.get_image(0, 0)
        self.center_x = STARTING_POS_X - self.image.get_size()[0] / 2
        self.center_y = STARTING_POS_Y - self.image.get_size()[1] / 2
        self.rect = self.image.get_rect()
        self.rect.x = self.center_x
        self.rect.y = self.center_y

        #self.snd_jump = Audio(snd_jump)

    def get_pos(self):
        return(self.rect.x,self.rect.y)

    def get_x(self):
        return(self.rect.x + self.image.get_size()[0] / 2)

    def get_y(self):
        return(self.rect.y + self.image.get_size()[1] / 2)

    def move(self, time, direction):
        old_direction = self.direction

        if old_direction != direction:
            self.sprite.flip_image()

        self.image = self.sprite.get_image(0, 0)
        self.sprite.animate(time)
        self.direction = direction

        if (direction == "R"):
            self.move_speed = -PLAYER_SPEED
        else:
            self.move_speed = PLAYER_SPEED

    def shoot(self, direction, laser_list):
        if self.move_speed == 0:
            if direction == "R":
                self.image = self.sprite_shoot_r.get_image(0, 0)
            else:
                self.image = self.sprite_shoot_l.get_image(0, 0)

        time = pygame.time.get_ticks()
        if time - self.laser_timer >= self.laser_cooldown:
            self.laser_timer = time
            laser = Laser(self.get_x(), self.get_y())
            laser_list.add(laser)
            laser.set_direction(self.direction)

    def jump(self):
        if self.on_ground == True:
            #self.snd_jump.play()
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

        self.collision = self.sprite.get_collision(self.rect.x, self.rect.y, self.sprite.width, self.sprite.height, ground.rect.x, ground.rect.y, ground.sprite.width, ground.sprite.height)

        if not self.collision:
            self.on_ground = False

        # if player touches ground stop
        if self.collision:
            if self.falling == True:
                self.falling = False
                self.on_ground = True
                self.velocity = 0

        # fall if not on ground, else snap to position
        if not self.on_ground:
            self.velocity += self.gravity
        else:
            self.rect.y = self.center_y

        self.rect.y -= self.velocity

    def collision_check(self, object):
        if self.sprite.get_collision(self.rect.x, self.rect.y, self.sprite.width, self.sprite.height, object.rect.x, object.rect.y, object.sprite.width, object.sprite.height):
            self.collision_entity = object.type

