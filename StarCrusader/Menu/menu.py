#!/usr/bin/python

#########################################
# Project:      Star Crusader
# Author:       Verity Cook
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Display interactive menu
#########################################

import pygame, sys
from pygame.locals import *



class Title:

    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = title_font.render(self.text, True, self.get_color())

    def get_color(self):
        return (245, 245, 245)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos


class MenuOption:
    hovered = False

    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            if self.text == "HIGH SCORES":
                return (218, 165, 32)
            else:
                return (110, 0, 0)
        else:
            return (160, 25, 25)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos


pygame.init()
screen = pygame.display.set_mode((900, 900))
title_font = pygame.font.Font(None, 70)
titles = [Title("STAR CRUSADER", (250, 100))]
menu_font = pygame.font.Font(None, 51) #changed to 51 to commit
options = [MenuOption("PLAY GAME", (250, 200)),  MenuOption("HIGH SCORES", (250, 250)),
           MenuOption("EXIT", (250, 300))]


loop = True

while loop:
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False

    pygame.event.pump()
    screen.fill((0, 0, 0))
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
        option.draw()
    for title in titles:
        title.draw()

    pygame.display.update()