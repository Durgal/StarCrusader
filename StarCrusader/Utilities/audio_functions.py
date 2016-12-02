#!/usr/bin/python

#########################################
# File:         audio_functions.py
# Author:       Chris Granat
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Provides main
#               functionality
#               for audio class
#########################################

import pygame


class Audio():

    def __init__(self, file):
        self.audio = pygame.mixer.Sound(file)

    def play(self):
        if not pygame.mixer.get_busy():
            self.audio.play()

    def stop(self):
        self.audio.stop()