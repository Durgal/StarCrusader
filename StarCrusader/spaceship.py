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
vec = pygame.math.Vector2

STARTING_POS_X = 450
STARTING_POS_Y = 450
POSITION_X = 0
POSITION_Y = 1
WIDTH, HEIGHT = 900, 900
ACCELERATE = 'accelerate'
ROTATE_LEFT = 'rotate_l'
ROTATE_RIGHT = 'rotate_r'
SHOOT = 'shoot'
ACCELERATION_RATE = 4
ROTATION_RATE = 200
FUEL_CAPACITY = 100
FUEL_DEPLETION_RATE = 7
HEALTH_CAPACITY = 1000000
ENERGY_CAPACITY = 100
ENERGY_DEPLETION_RATE = 0
FIRE_RATE = 500
LASER_SPEED = vec(0, -7)
LASER_ROT_OFFSET = 90
LASER_DURATION = 0
LASER_OFFSET = vec(0, -20)


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, sprite_group, x=STARTING_POS_X, y=STARTING_POS_Y):
        self.group = sprite_group
        pygame.sprite.Sprite.__init__(self, self.group)
        self.image = pygame.image.load('Sprites/spaceship.png')
        self.rect = self.image.get_rect()
        self.position = vec(x, y)
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)
        self.rect.center = self.position
        self.rotation = 0
        self.rot_speed = 0
        self.dt = 0
        self.fuel = FUEL_CAPACITY
        self.health = HEALTH_CAPACITY
        self.energy = ENERGY_CAPACITY
        self.dead = False
        self.last_shot = 0

        self.orig_img = self.image
        self.orig_center = self.rect.center

        self.player_chunk = pygame.Rect(0, 0, WIDTH, HEIGHT)
        self.player_chunk.center = self.position

    def get_event(self, event):
        self.rot_speed = 0
        if 0 <= self.fuel or self.dead:
            if ACCELERATE == event:
                self.acceleration = vec(0, -ACCELERATION_RATE)
                self.deplete_fuel()
            if ROTATE_LEFT == event:
                self.rot_speed = ROTATION_RATE
                self.rotate_sprite()
            if ROTATE_RIGHT == event:
                self.rot_speed = -ROTATION_RATE
                self.rotate_sprite()
        if SHOOT == event:
            if 0 < self.energy:
                now = pygame.time.get_ticks()
                if now - self.last_shot > FIRE_RATE:
                    self.last_shot = now
                    direction = self.velocity.rotate(-self.rotation)
                    Laser(self.group, self.rect, direction, (self.rotation - LASER_ROT_OFFSET))
                    self.energy -= ENERGY_DEPLETION_RATE

    def deplete_fuel(self):
        self.fuel -= (FUEL_DEPLETION_RATE * self.dt)

    def collided(self, amount):
        self.health -= amount

    def check_death(self):
        if 0 >= self.health:
            self.kill()
            self.dead = True

        if self.dead:
            self.velocity = vec(0, 0)

    def set_dt(self, dt):
        self.dt = dt

    def rotate_sprite(self):
        self.image = pygame.transform.rotate(self.orig_img, self.rotation)
        self.rect = self.image.get_rect(center=self.orig_center)

    def debugging(self, screen, fps):
        if pygame.font:
            font = pygame.font.Font("courbd.ttf", 12)

            rot_angle = font.render(str(self.rotation), 1, (255, 255, 255))
            rot_angle1 = font.render('Angle: ', 1, (255, 255, 255))
            position = font.render(str(self.position), 1, (255, 255, 255))
            position1 = font.render('Position [x,y]: ', 1, (255, 255, 255))
            velocity = font.render(str(self.velocity), 1, (255, 255, 255))
            velocity1 = font.render('Velocity [x,y]: ', 1, (255, 255, 255))
            frames = font.render(str(int(fps)), 1, (255, 255, 255))
            fuel = font.render('Fuel: ', 1, (255, 255, 255))
            fuel1 = font.render(str(self.fuel), 1, (255, 255, 255))
            health = font.render('Health: ', 1, (255, 255, 255))
            health1 = font.render(str(self.health), 1, (255, 255, 255))
            energy = font.render('Energy: ', 1, (255, 255, 255))
            energy1 = font.render(str(self.energy), 1, (255, 255, 255))
            player_chunk = font.render(str(self.player_chunk), 1, (255, 255, 255))

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
            player_chunk_text = energy1.get_rect().move(120, 115)

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
            screen.blit(player_chunk, player_chunk_text)

    def update(self):
        self.rotation = (self.rotation + self.rot_speed * self.dt) % 360
        self.velocity += self.acceleration.rotate(-self.rotation) * self.dt
        self.position += self.velocity
        self.acceleration = vec(0, 0)
        self.rect.center = self.position
        self.rot_speed = 0

        self.check_death()
        self.player_chunk.centerx = self.position[POSITION_X]
        self.player_chunk.centery = self.position[POSITION_Y]


class Laser(pygame.sprite.Sprite):
    def __init__(self, sprite_group, spaceship_rect, direction, rotation):
        self.group = sprite_group
        pygame.sprite.Sprite.__init__(self, self.group)
        self.image = pygame.image.load('Sprites/laser.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.image.get_rect().center
        self.position = spaceship_rect.center
        self.velocity = direction
        self.rotation = rotation
        self.duration = 0

        self.orig_img = self.image
        self.orig_center = self.rect.center

        self.rotate_sprite()

    def rotate_sprite(self):
        self.image = pygame.transform.rotate(self.orig_img, self.rotation)
        self.rect = self.image.get_rect(center=self.orig_center)

    def collided(self, damage):
        self.kill()

    def update(self):
        self.position += self.velocity + LASER_SPEED
        self.rect.center = self.position


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)
        self.camera = pygame.Rect(x, y, self.width, self.height)
