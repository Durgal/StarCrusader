#!/usr/bin/python

#########################################
# File:         spaceship.py
# Author:       Michael Souza
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Provides main
#               functionality
#               for spaceship class
#########################################

import pygame
from Utilities.sprite_functions import Sprite
from Utilities.audio_functions import Audio
vec = pygame.math.Vector2

HALF = 2
STARTING_POS_X = 450
STARTING_POS_Y = 450
POSITION_X = 0
POSITION_Y = 1
WIDTH, HEIGHT = 900, 900
ACCELERATE = 'accelerate'
ROTATE_LEFT = 'rotate_l'
ROTATE_RIGHT = 'rotate_r'
ACCELERATION_RATE = 8
ROTATION_RATE = 200
FUEL_DEPLETION_RATE = 7
FUEL_CAPACITY = 100
ENERGY_DEPLETION_RATE = 10
ENERGY_CAPACITY = 100
FIRE_RATE = 200
HEALTH_CAPACITY = 100
LASER_SPEED = vec(0, -15)
LASER_ROT_OFFSET = 90
LASER_DURATION = 500
LASER_OFFSET = vec(0, -20)
MIN = 0
INITIALIZE = 0
FULL_ROTATION = 360
FUEL_ANIMATION_TIME = 2.5
SPRITE_W = 40
SPRITE_H = 65

snd_laser = "Audio/laser.wav"
snd_thrust = "Audio/thrust.wav"


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, sprite_group, laser_group, x=STARTING_POS_X, y=STARTING_POS_Y):
        self.group = sprite_group
        self.laser_group = laser_group
        pygame.sprite.Sprite.__init__(self, self.group)
        self.sprite = Sprite('Sprites/spaceship_sheet.png', SPRITE_W, SPRITE_H)
        self.sprite_stopped = Sprite('Sprites/spaceship.png', SPRITE_W, SPRITE_H)

        self.level = "none"
        self.position = vec(x, y)
        self.velocity = vec(INITIALIZE, INITIALIZE)
        self.acceleration = vec(INITIALIZE, INITIALIZE)
        self.rotation = INITIALIZE
        self.rot_speed = INITIALIZE
        self.dt = INITIALIZE
        self.dead = False
        self.last_shot = INITIALIZE
        self.is_accel = False

        self.fuel = FUEL_CAPACITY
        self.health = HEALTH_CAPACITY
        self.energy = ENERGY_CAPACITY
        self.treasure = INITIALIZE

        self.image = self.sprite.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.orig_img = self.image
        self.orig_center = self.rect.center

        self.player_chunk = pygame.Rect(INITIALIZE, INITIALIZE, WIDTH, HEIGHT)
        self.player_chunk.center = self.position

        self.snd_laser = Audio(snd_laser)
        self.snd_thrust = Audio(snd_thrust)

    def get_event(self, event):
        self.rot_speed = INITIALIZE
        if MIN <= self.fuel and not self.dead:
            if ACCELERATE == event:
                self.acceleration = vec(MIN, -ACCELERATION_RATE)
                self.deplete_fuel()
                self.image = self.sprite.get_image(0, 0)
                self.sprite.animate(pygame.time.get_ticks() * FUEL_ANIMATION_TIME)
                self.is_accel = True
                self.snd_thrust.play()

        if ROTATE_LEFT == event:
            self.rot_speed = ROTATION_RATE
            self.rotate_sprite()
        if ROTATE_RIGHT == event:
            self.rot_speed = -ROTATION_RATE
            self.rotate_sprite()

    def shoot_laser(self):
        if MIN < self.energy and not self.dead:
            now = pygame.time.get_ticks()
            if now - self.last_shot > FIRE_RATE:
                self.last_shot = now
                velocity = self.velocity + LASER_SPEED.rotate(-self.rotation)
                position = self.position
                rotation = self.rotation
                Laser(self.laser_group, position, velocity, rotation)
                self.energy -= ENERGY_DEPLETION_RATE
                self.snd_laser.play()

    def deplete_fuel(self):
        self.fuel -= (FUEL_DEPLETION_RATE * self.dt)

    def collided(self, amount):
        self.health -= amount

    def check_death(self):
        if MIN >= self.health:
            self.kill()
            self.dead = True

        if self.dead:
            self.velocity = vec(INITIALIZE, INITIALIZE)

    def set_dt(self, dt):
        self.dt = dt

    def rotate_sprite(self):
        self.image = pygame.transform.rotate(self.orig_img, self.rotation)
        self.rect = self.image.get_rect(center=self.orig_center)

    def debugging(self, screen, fps):
        if pygame.font:
            font = pygame.font.Font("courbd.ttf", 12)

            rot_angle = font.render(str(int(self.rotation)), 1, (255, 255, 255))
            rot_angle1 = font.render('Angle: ', 1, (255, 255, 255))
            position = font.render(str(self.position), 1, (255, 255, 255))
            position1 = font.render('Position [x,y]: ', 1, (255, 255, 255))
            velocity = font.render(str(self.velocity), 1, (255, 255, 255))
            velocity1 = font.render('Velocity [x,y]: ', 1, (255, 255, 255))
            frames = font.render(str(int(fps)), 1, (255, 255, 255))
            fuel = font.render('Fuel: ', 1, (255, 255, 255))
            fuel1 = font.render(str(int(self.fuel)), 1, (255, 255, 255))
            health = font.render('Health: ', 1, (255, 255, 255))
            health1 = font.render(str(self.health), 1, (255, 255, 255))
            energy = font.render('Energy: ', 1, (255, 255, 255))
            energy1 = font.render(str(self.energy), 1, (255, 255, 255))

            textpos1 = rot_angle.get_rect().move(120, 25)
            textpos2 = position.get_rect().move(120, 40)
            textpos3 = velocity.get_rect().move(120, 55)
            text_fuel1 = fuel1.get_rect().move(120, 70)
            text_health1 = health1.get_rect().move(120, 85)
            text_energy1 = energy1.get_rect().move(120, 100)
            textpos4 = rot_angle1.get_rect().move(10, 25)
            textpos5 = position1.get_rect().move(10, 40)
            textpos6 = velocity1.get_rect().move(10, 55)
            text_fuel = fuel.get_rect().move(10, 70)
            text_health = health.get_rect().move(10, 85)
            text_energy = energy.get_rect().move(10, 100)
            textpos7 = frames.get_rect().move(10, 10)

            screen.blit(rot_angle, textpos1)
            screen.blit(position, textpos2)
            screen.blit(velocity, textpos3)
            screen.blit(rot_angle1, textpos4)
            screen.blit(position1, textpos5)
            screen.blit(velocity1, textpos6)
            screen.blit(fuel, text_fuel)
            screen.blit(fuel1, text_fuel1)
            screen.blit(health, text_health)
            screen.blit(health1, text_health1)
            screen.blit(energy, text_energy)
            screen.blit(energy1, text_energy1)
            screen.blit(frames, textpos7)

    def update(self):
        self.rotation = (self.rotation + self.rot_speed * self.dt) % FULL_ROTATION
        self.velocity += self.acceleration.rotate(-self.rotation) * self.dt
        self.position += self.velocity
        self.acceleration = vec(INITIALIZE, INITIALIZE)
        self.rect.center = self.position
        self.rot_speed = INITIALIZE

        if self.is_accel is not True:
            self.image = self.sprite_stopped.get_image(0, 0)
            self.rect = self.image.get_rect()
            self.rect.center = self.position
            self.orig_img = self.image
            self.orig_center = self.rect.center
            self.rotate_sprite()
        else:
            self.image = self.sprite.get_image(0, 0)
            self.rect = self.image.get_rect()
            self.rect.center = self.position
            self.orig_img = self.image
            self.orig_center = self.rect.center
            self.rotate_sprite()

        self.check_death()
        self.player_chunk.centerx = self.position[POSITION_X]
        self.player_chunk.centery = self.position[POSITION_Y]
        self.is_accel = False


class Laser(pygame.sprite.Sprite):
    def __init__(self, sprite_group, position, velocity, rotation):
        self.group = sprite_group
        pygame.sprite.Sprite.__init__(self, self.group)
        self.image = pygame.image.load('Sprites/laser.png')
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.time_shot = pygame.time.get_ticks()
        self.velocity = velocity
        self.position = self.rect.center
        self.rotation = rotation + LASER_ROT_OFFSET

        self.orig_img = self.image
        self.orig_center = self.rect.center

        self.rotate_sprite()

    def rotate_sprite(self):
        self.image = pygame.transform.rotate(self.orig_img, self.rotation)
        self.rect = self.image.get_rect(center=self.orig_center)

    def collided(self):
        self.kill()

    def update(self):
        if pygame.time.get_ticks() - self.time_shot > LASER_DURATION:
            self.kill()

        self.position += self.velocity
        self.rect.center = self.position


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(INITIALIZE, INITIALIZE, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / HALF)
        y = -target.rect.centery + int(self.height / HALF)
        self.camera = pygame.Rect(x, y, self.width, self.height)
