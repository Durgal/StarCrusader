#!/usr/bin/python

#########################################
# File:         asteroid.py
# Author:       Michael Souza
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Provides main
#               functionality
#               for asteroid class
#########################################

import pygame
import random
from Utilities.audio_functions import Audio

ASTEROID1 = 1
ASTEROID2 = 2
ASTEROID3 = 3
ASTEROID4 = 4
ASTEROID5 = 5
ASTEROID6 = 6

snd_explode = "Audio/explode.wav"

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, sprite_group, image, x, y, damage):
        self.group = sprite_group
        pygame.sprite.Sprite.__init__(self, self.group)
        self.x = x
        self.y = y

        self.image = image
        self.rect = self.image.get_rect()
        self.position = (self.x, self.y)
        self.rect.center = self.position
        self.dt = 0.017

        self.orig_center = self.rect.center
        self.orig_img = self.image
        self.rotation = 0
        self.rot_speed = random.randint(4, 20)

        self.damage = damage

        self.snd_explode = Audio(snd_explode)

    def set_dt(self, dt):
        self.dt = dt

    def rotate_sprite(self):
        self.image = pygame.transform.rotate(self.orig_img, self.rotation)
        self.rect = self.image.get_rect(center=self.orig_center)

    def kill_asteroid(self):
        self.kill()

    def update(self, spaceship_group, laser_group):
        if self.rot_speed % 2 == 0:
            self.rotation = (self.rotation + self.rot_speed * self.dt) % 360
        else:
            self.rotation = (self.rotation - self.rot_speed * self.dt) % 360
        self.rect.center = self.image.get_rect().center
        self.rotate_sprite()

        for sprite in spaceship_group:
            if pygame.sprite.collide_mask(self, sprite):
                self.kill_asteroid()
                sprite.collided(self.damage)
                self.snd_explode.play()

        for laser in laser_group:
            if pygame.sprite.collide_mask(self, laser):
                self.kill_asteroid()
                laser.collided()
                self.snd_explode.play()
