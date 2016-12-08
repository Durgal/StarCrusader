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
        " Initialize file object "
        self.file = file
        self.create()
        self.i_file = open(file,'r+')
        self.data = self.i_file.readlines()

    def create(self):
        " Creates a file with given text attributes "
        file = open(self.file, 'w+')
        file.write('100'+'\n')
        file.write('100'+'\n')
        file.write('100'+'\n')
        file.write('0'+'\n')
        file.close()

    def readline(self, line):
        " Reads a given line number "
        return self.data[line]

    def writeline(self, line, text):
        " Writes text at a given line number "
        self.data[line] = str(text)+'\n'
        o_file = open(self.file, 'w+')
        o_file.writelines(self.data)

    def destroy(self):
        pass #TODO: remove text file