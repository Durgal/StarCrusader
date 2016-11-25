#!/usr/bin/python

import pygame
from pygame.locals import *
from spaceship import Spaceship
from spaceship import Camera

HEIGHT = 800
WIDTH = 800
FPS = 60
MS = 1000.0

BLACK = (0, 0, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Star Crusader")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    spaceship = Spaceship()
    camera = Camera(WIDTH, HEIGHT)

    all_sprites.add(spaceship)

    running = True
    while running:
        milliseconds = clock.tick(FPS)
        dt = milliseconds / MS
        spaceship.set_dt(dt)
        fps = clock.get_fps()

        # events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        if pygame.key.get_pressed()[pygame.K_w] != 0:
            spaceship.get_event('accelerate')
        if pygame.key.get_pressed()[pygame.K_a] != 0:
            spaceship.get_event('rotate_l')
        if pygame.key.get_pressed()[pygame.K_d] != 0:
            spaceship.get_event('rotate_r')

        # update
        all_sprites.update()
        camera.update(spaceship)

        # render
        screen.fill(BLACK)
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))
        spaceship.debugging(screen, fps)
        pygame.display.flip()


if __name__ == '__main__': main()
