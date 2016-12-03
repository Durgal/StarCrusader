#!/usr/bin/python

#########################################
# Project:      Star Crusader
# Author:       Chris Granat
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Generates random star
#               field for planet background
#########################################

from random import randrange, choice


STAR_MAX = 25

class Star():
    def __init__(self, screen):
        "Initialize star field"
        self.stars = []
        for s in range(STAR_MAX):
            # star = [x,y,speed]
            star = [randrange(0,screen.get_width()-1),
                    randrange(0,screen.get_height()-1),
                    choice([1,2,3])]
            self.stars.append(star)


    def draw_stars(self, screen, speed):
        "Draw star field"
        for star in self.stars:
            star[0] += star[2]*speed*100
            if star[0] >= screen.get_width():   # For travelling right
                star[0] = 0
                star[1] = randrange(0,screen.get_width())
                star[2] = choice([1,2,3])
            elif star[0] <= 0:                  # For travelling left
                star[0] = screen.get_width()
                star[1] = randrange(0,screen.get_width())
                star[2] = choice([1,2,3])

            # Brightness of star depends on speed
            if star[2] == 1:
                color = (100,100,100)
            elif star[2] == 2:
                color = (190, 190, 190)
            elif star[2] == 3:
                color = (255, 255, 255)

            # Draw star with color at (x, y, w, h)
            screen.fill(color, (star[0], star[1], star[2], star[2]))