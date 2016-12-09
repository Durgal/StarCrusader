#!/usr/bin/python

#########################################
# File:         gameplay.py
# Author:       Chris Granat
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      handles loading
#               of levels and
#               saving player data
#########################################

import pygame
from Utilities.file_functions import File
import level

RED = (255, 0, 0)
YELLOW = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

HEIGHT = 900
WIDTH = 900
MS = 1000


class Gameplay:
    """ Generate Gamplay object """
    def __init__(self):

        # Screen initialization
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Star Crusader")

        # Games current level
        self.current_level = level.Planet(self.screen)

        # External file path saves player data
        path = "statistics.txt"
        self.file = File(path)

    def load_player_data(self):
        player = self.current_level.get_player()
        player.fuel = int(self.file.readline(0))
        player.health = int(self.file.readline(1))
        player.energy = int(self.file.readline(2))
        player.treasure = int(self.file.readline(3))

    def save_player_data(self):
        player = self.current_level.get_player()
        self.file.writeline(0, round(player.fuel))
        self.file.writeline(1, round(player.health))
        self.file.writeline(2, round(player.energy))
        self.file.writeline(3, round(player.treasure))

    def change_level(self):
        if self.current_level.get_type() == "universe":
            self.save_player_data()
            self.current_level = level.Universe(self.screen)
            self.load_player_data()
        if self.current_level.get_type() == "planet":
            self.save_player_data()
            self.current_level = level.Planet(self.screen)
            self.load_player_data()

    def set_fps(self,fps,clock):
        milliseconds = clock.tick(fps)
        dt = milliseconds / MS
        self.set_dt(dt)

    def set_dt(self,dt):
        self.current_level.set_dt(dt)

    def get_input(self):
        self.current_level.get_input()

    def update(self):
        self.current_level.update()

    def render_level(self,fps):
        self.screen.fill(BLACK)
        self.current_level.render_level(fps)

    def get_level(self):
        return self.current_level