#!/usr/bin/python

import pygame
from random import randint

ASTEROIDS = 0
ASTEROIDS_MIN = 10
ASTEROIDS_MAX = 30
ASTEROIDS_COUNT = 3
WHITE = 0
WHITE_SPRITES = 3
WHITE_COORDS = 1
GRAY = 1
GRAY_SPRITES = 0
GRAY_COORDS = 2
LIGHT_GRAY = 2
LIGHT_GRAY_SPRITES = 0
LIGHT_GRAY_COORDS = 3
X = 0
X_MIN = 0
X_MAX = 800
X_START_MIN = 200
X_START_MAX = 600
Y = 1
Y_MIN = 0
Y_MAX = 800
Y_START_MIN = 200
Y_START_MAX = 600


class Universe:
    def __init__(self, universe_file='Universe/universe_test.txt', *white_asteroids):
        self.__read_file__(universe_file)
        self._white_asteroids = []

        for count in range(WHITE_SPRITES):
            try:
                self._white_asteroids.append(pygame.image.load(white_asteroids[count]))

            except pygame.error as message:
                print("Can't load asteroid: ", white_asteroids[count])
                raise message

    def __read_file__(self, universe_file='Universe/universe_test.txt'):
        self._asteroids_data = []

        with open(universe_file) as self._universe_file:
            for line in self._universe_file:
                data = line.split()
                if data:
                    data = [int(i) for i in data]
                    self._asteroids_data.append(data)

    def draw_asteroids(self, screen):
        for count in range(self._asteroids_data[ASTEROIDS][WHITE]):
            screen.blit(self._white_asteroids[count % WHITE_SPRITES], (self._asteroids_data[WHITE_COORDS][X + count],
                                                                       self._asteroids_data[WHITE_COORDS][Y + count]))

    def create_random_universe(self, universe_file='Universe/universe_test.txt'):
        asteroids = []
        prev_x = 0
        prev_y = 0

        for count in range(ASTEROIDS_COUNT):
            asteroids.append(randint(ASTEROIDS_MIN, ASTEROIDS_MAX))

        with open(universe_file, 'w') as self._universe_file:
            for count in range(ASTEROIDS_COUNT):
                self._universe_file.write(str(asteroids[WHITE + count]))
                self._universe_file.write(' ')

            self._universe_file.write('\n')

            for x in range(ASTEROIDS_COUNT):
                for count in range(asteroids[WHITE + x]):
                    random_x = randint(X_MIN, X_MAX)
                    random_y = randint(Y_MIN, Y_MAX)

                    while X_START_MIN < random_x < X_START_MAX or prev_x - 60 < random_x < prev_x + 60:
                        random_x = randint(X_MIN, X_MAX)

                    while random_y > Y_START_MAX > random_y or prev_y - 60 < random_y < prev_y + 60:
                        random_y = randint(Y_MIN, Y_MAX)

                    self._universe_file.write(str(random_x))
                    self._universe_file.write(' ')
                    self._universe_file.write(str(random_y))
                    self._universe_file.write(' ')

                    prev_x = random_x
                    prev_y = random_y

                self._universe_file.write('\n')

            self._universe_file.close()
