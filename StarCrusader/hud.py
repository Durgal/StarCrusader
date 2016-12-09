#!/usr/bin/python

#########################################
# File:         hud.py
# Author:       Michael Souza
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Displays the player's
#               vitals
#########################################

import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)

HUD_X = 450
HUD_Y = 30
RECT_WIDTH = 114
RECT_HEIGHT = 21
RECT_TOP = 20
FUEL_RECT_LEFT = 145
HEALTH_RECT_LEFT = 344
ENERGY_RECT_LEFT = 539
MIN_INPUT = 1
FUEL_CAPACITY = 100
HEALTH_CAPACITY = 100
ENERGY_CAPACITY = 100
LOW_AMOUNT = 25
INITIALIZE = 0


class Hud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprites/hud.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = HUD_X
        self.rect.centery = HUD_Y
        self.treasure = INITIALIZE
        self.fuel_width = RECT_WIDTH
        self.health_width = RECT_WIDTH
        self.energy_width = RECT_WIDTH
        self.fuel_rect = pygame.Rect(FUEL_RECT_LEFT, RECT_TOP, self.fuel_width, RECT_HEIGHT)
        self.health_rect = pygame.Rect(HEALTH_RECT_LEFT, RECT_TOP, self.health_width, RECT_HEIGHT)
        self.energy_rect = pygame.Rect(ENERGY_RECT_LEFT, RECT_TOP, self.energy_width, RECT_HEIGHT)
        self.draw_fuel = False
        self.draw_health = False
        self.draw_energy = False

    def update(self, fuel, health, energy, treasure):
        self.treasure = treasure

        if MIN_INPUT >= fuel:
            self.draw_fuel = False
        else:
            self.draw_fuel = True
            self.fuel_width = int((fuel/FUEL_CAPACITY) * RECT_WIDTH)
            self.fuel_rect = pygame.Rect(FUEL_RECT_LEFT, RECT_TOP, self.fuel_width, RECT_HEIGHT)

        if MIN_INPUT >= health:
            self.draw_health = False
        else:
            self.draw_health = True
            self.health_width = int((health/HEALTH_CAPACITY) * RECT_WIDTH)
            self.health_rect = pygame.Rect(HEALTH_RECT_LEFT, RECT_TOP, self.health_width, RECT_HEIGHT)

        if MIN_INPUT >= energy:
            self.draw_energy = False
        else:
            self.draw_energy = True
            self.energy_width = int((energy/ENERGY_CAPACITY) * RECT_WIDTH)
            self.energy_rect = pygame.Rect(ENERGY_RECT_LEFT, RECT_TOP, self.energy_width, RECT_HEIGHT)

    def draw_hud(self, screen):
        screen.blit(self.image, self.rect)

        if self.draw_fuel:
            if LOW_AMOUNT >= self.fuel_width:
                pygame.draw.rect(screen, RED, self.fuel_rect)
            else:
                pygame.draw.rect(screen, WHITE, self.fuel_rect)
        if self.draw_health:
            if LOW_AMOUNT >= self.health_width:
                pygame.draw.rect(screen, RED, self.health_rect)
            else:
                pygame.draw.rect(screen, WHITE, self.health_rect)
        if self.draw_energy:
            if LOW_AMOUNT >= self.energy_width:
                pygame.draw.rect(screen, RED, self.energy_rect)
            else:
                pygame.draw.rect(screen, WHITE, self.energy_rect)

        if pygame.font:
            font = pygame.font.Font("courbd.ttf", 17)
            treasure = font.render(str(self.treasure), 1, WHITE)
            textpos = treasure.get_rect().move(760, 21)
            screen.blit(treasure, textpos)
