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
        self.file = file
        self.create()
        self.i_file = open(file,'r+')
        self.data = self.i_file.readlines()

    def create(self):
        file = open(self.file, 'w+')
        file.write('100'+'\n')
        file.write('100'+'\n')
        file.write('100'+'\n')
        file.write('0'+'\n')
        file.close()

    def readline(self, line):
        return self.data[line]

    def writeline(self, line, text):
        self.data[line] = str(text)+'\n'
        o_file = open(self.file, 'w+')
        o_file.writelines(self.data)