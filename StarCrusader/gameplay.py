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

from Utilities.file_functions import File
import level

RED = (255, 0, 0)
YELLOW = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

MS = 1000


class Gameplay:
    """ Generate Gamplay object """
    def __init__(self, screen):

        self.screen = screen
        self.current_level = level.Universe(self.screen)

        path = "statistics.txt"
        self.file = File(path)

        #TODO: save and load player data functions

    def change_level(self):
        if self.current_level.get_type() == "universe":
            self.current_level = level.Universe(self.screen)
        if self.current_level.get_type() == "planet":
            self.current_level = level.Planet(self.screen)

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