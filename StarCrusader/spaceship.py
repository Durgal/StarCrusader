#!/usr/bin/python

import pygame
vec = pygame.math.Vector2

STARTING_POS_X = 400
STARTING_POS_Y = 400
ACCELERATE = 'accelerate'
ROTATE_LEFT = 'rotate_l'
ROTATE_RIGHT = 'rotate_r'
ACCELERATION_RATE = 15
ROTATION_RATE = 200
TERMINAL_VELOCITY = vec(5, 5)


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, dt, x=STARTING_POS_X, y=STARTING_POS_Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprites/spaceship.png')
        self.rect = self.image.get_rect()
        self.position = vec(x, y)
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)
        self.rect.center = self.position
        self.rotation = 0
        self.rot_speed = 0
        self.dt = dt

        self.orig_img = self.image
        self.orig_center = self.rect.center

    def get_event(self, event):
        self.rot_speed = 0
        if ACCELERATE == event:
            self.acceleration = vec(0, -ACCELERATION_RATE)
        if ROTATE_LEFT == event:
            self.rot_speed = ROTATION_RATE

            self.image = pygame.transform.rotate(self.orig_img, self.rotation)
            self.rect = self.image.get_rect(center=self.orig_center)

        if ROTATE_RIGHT == event:
            self.rot_speed = -ROTATION_RATE

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
            frames = font.render(str(fps), 1, (255, 255, 255))

            textpos1 = rot_angle.get_rect().move(120, 25)
            textpos2 = position.get_rect().move(120, 40)
            textpos3 = velocity.get_rect().move(120, 55)

            textpos4 = rot_angle1.get_rect().move(10, 25)
            textpos5 = position1.get_rect().move(10, 40)
            textpos6 = velocity1.get_rect().move(10, 55)

            textpos7 = frames.get_rect().move(10, 10)

            screen.blit(rot_angle, textpos1)
            screen.blit(position, textpos2)
            screen.blit(velocity, textpos3)

            screen.blit(rot_angle1, textpos4)
            screen.blit(position1, textpos5)
            screen.blit(velocity1, textpos6)

            screen.blit(frames, textpos7)

    def update(self):
        self.rotation = (self.rotation + self.rot_speed * self.dt) % 360
        self.velocity += self.acceleration.rotate(-self.rotation) * self.dt
        self.position += self.velocity
        self.acceleration = vec(0, 0)
        self.rect.center = self.position
        self.rot_speed = 0
