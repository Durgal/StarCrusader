#!/usr/bin/python

#########################################
# File:         file_functions.py
# Author:       Chris Granat
# Date:         12/09/16
# Class:        Open Source
# Assignment:   Final Project
# Purpose:      Provides functionality
#               to read and write to
#               external text files
#########################################


class File():

    def __init__(self, file):
        self.file = open(file,'r+')

    def readline(self, line):
        for line in iter(self.file):
            print (line)

    def write(self, text):
        self.file.write(text)