#!/usr/bin/python

import pygame
import random


ASTEROID1 = 1
ASTEROID2 = 2
ASTEROID3 = 3
ASTEROID4 = 4
ASTEROID5 = 5
ASTEROID6 = 6


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.image = self.random_asteroid()
        self.rect = self.image.get_rect()
        self.position = (self.x, self.y)
        self.rect.center = self.position
        self.dt = 0.017

        self.orig_center = self.rect.center
        self.orig_img = self.image
        self.rotation = 0
        self.rot_speed = random.randint(4, 20)

    @staticmethod
    def random_asteroid():
        random_asteroid = random.randint(1, 6)

        if ASTEROID1 == random_asteroid:
            image = pygame.image.load('Sprites/asteroid1.png')
        if ASTEROID2 == random_asteroid:
            image = pygame.image.load('Sprites/asteroid2.png')
        if ASTEROID3 == random_asteroid:
            image = pygame.image.load('Sprites/asteroid3.png')
        if ASTEROID4 == random_asteroid:
            image = pygame.image.load('Sprites/asteroid4.png')
        if ASTEROID5 == random_asteroid:
            image = pygame.image.load('Sprites/asteroid5.png')
        if ASTEROID6 == random_asteroid:
            image = pygame.image.load('Sprites/asteroid6.png')

        return image

    def set_dt(self, dt):
        self.dt = dt

    def rotate_sprite(self):
        self.image = pygame.transform.rotate(self.orig_img, self.rotation)
        self.rect = self.image.get_rect(center=self.orig_center)

    def update(self):
        if self.rot_speed % 2 == 0:
            self.rotation = (self.rotation + self.rot_speed * self.dt) % 360
        else:
            self.rotation = (self.rotation - self.rot_speed * self.dt) % 360
        self.rect.center = self.image.get_rect().center
        self.rotate_sprite()
