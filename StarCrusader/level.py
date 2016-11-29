#!/usr/bin/python

import pygame
import random
from asteroid import Asteroid

RED = (255, 0, 0)
YELLOW = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ASTEROID1 = 1
ASTEROID2 = 2
ASTEROID3 = 3
ASTEROID4 = 4
ASTEROID5 = 5
ASTEROID6 = 6
ASTEROID_IMAGE_COUNT = 6

CHUNK_SIZE = 900
CHUNK_HALF_SIZE = 450
RENDER_DISTANCE = 1
COORDS = 0
X_COORD = 0
Y_COORD = 1
ASTEROID_INDEX = 1


class Level:

    def __init__(self, player):

        self.background = None
        self.type = None
        self.player = player

    def draw(self, screen):

        screen.fill(BLACK)

        if self.background:
            screen.blit(self.background, (0,0))

    def get_type(self):

        return self.type


class Planet(Level):

    def __init__(self, player):

        Level.__init__(self, player)

        self.type = "planet"

        self.background = pygame.image.load("sprites/planet.png").convert()


class Universe(Level):
    def __init__(self, player, camera, sprite_group, screen):
        self.group = sprite_group
        Level.__init__(self, player)
        self.type = "universe"
        self.asteroid_image_set = []
        self.asteroid_damage_set = []
        self.load_asteroid_data()

        self.camera = camera
        self.spaceship = player
        self.screen = screen

        self.player_chunk = player.player_chunk
        self.current_rendered_chunks = []
        self.sprite_chunks = []
        self.player_chunk_coords = [0, 0]
        self.player_coords = [self.spaceship.rect.x, self.spaceship.rect.y]

        self.asteroid_set = []
        self.new_chunk = []

    def generate_asteroid(self, lower_x, upper_x, lower_y, upper_y):
        random_asteroid = random.randint(0, 5)
        return Asteroid(self.group, self.asteroid_image_set[random_asteroid], random.randint(lower_x, upper_x), random.randint(lower_y, upper_y), self.asteroid_damage_set[random_asteroid])

    def generate_chunk(self, chunk_x_coord, chunk_y_coord):
        chunk_already_exists = False
        for chunk in self.current_rendered_chunks:
            if (chunk_x_coord, chunk_y_coord) in chunk:
                chunk_already_exists = True

        if not chunk_already_exists:
            # self.new_chunk = self.asteroid_set
            for sprite in self.new_chunk:
                self.new_chunk.remove(sprite)

            self.current_rendered_chunks.append(((chunk_x_coord, chunk_y_coord), self.new_chunk))
            asteroid_count = random.randint(2, 7)

            for count in range(asteroid_count):
                self.new_chunk.append(self.generate_asteroid((chunk_x_coord * CHUNK_SIZE), ((chunk_x_coord * CHUNK_SIZE) + CHUNK_SIZE),
                                           (chunk_y_coord * CHUNK_SIZE), ((chunk_y_coord * CHUNK_SIZE) + CHUNK_SIZE)))

    def player_moved_chunks(self):
        player_moved_chunks = False

        if int(self.player_chunk.centerx % CHUNK_HALF_SIZE <= 30) and self.player_coords[X_COORD] not in range(self.player_chunk_coords[X_COORD] * CHUNK_SIZE, (self.player_chunk_coords[X_COORD] * CHUNK_SIZE) + CHUNK_SIZE):
            player_moved_chunks = True

        if int(self.player_chunk.centery % CHUNK_HALF_SIZE <= 30) and self.player_coords[Y_COORD] not in range(self.player_chunk_coords[Y_COORD] * CHUNK_SIZE, (self.player_chunk_coords[Y_COORD] * CHUNK_SIZE) + CHUNK_SIZE):
            player_moved_chunks = True

        return player_moved_chunks

    def update_current_chunk_coords(self):
        self.player_chunk_coords[X_COORD] = int(self.player_chunk.x / CHUNK_SIZE)
        self.player_chunk_coords[Y_COORD] = int(self.player_chunk.y / CHUNK_SIZE)

    def update_current_player_coords(self):
        self.player_coords[X_COORD] = self.spaceship.rect.x
        self.player_coords[Y_COORD] = self.spaceship.rect.y

    def generate_nearby_chunks(self):
        self.generate_chunk(self.player_chunk_coords[X_COORD], self.player_chunk_coords[Y_COORD])
        self.generate_chunk(self.player_chunk_coords[X_COORD] + RENDER_DISTANCE, self.player_chunk_coords[Y_COORD])
        self.generate_chunk(self.player_chunk_coords[X_COORD] - RENDER_DISTANCE, self.player_chunk_coords[Y_COORD])
        self.generate_chunk(self.player_chunk_coords[X_COORD], self.player_chunk_coords[Y_COORD] + RENDER_DISTANCE)
        self.generate_chunk(self.player_chunk_coords[X_COORD], self.player_chunk_coords[Y_COORD] - RENDER_DISTANCE)
        self.generate_chunk(self.player_chunk_coords[X_COORD] - RENDER_DISTANCE, self.player_chunk_coords[Y_COORD] + RENDER_DISTANCE)
        self.generate_chunk(self.player_chunk_coords[X_COORD] + RENDER_DISTANCE, self.player_chunk_coords[Y_COORD] - RENDER_DISTANCE)
        self.generate_chunk(self.player_chunk_coords[X_COORD] - RENDER_DISTANCE, self.player_chunk_coords[Y_COORD] - RENDER_DISTANCE)
        self.generate_chunk(self.player_chunk_coords[X_COORD] + RENDER_DISTANCE, self.player_chunk_coords[Y_COORD] + RENDER_DISTANCE)

    def remove_far_chunks(self):
        for chunk in self.current_rendered_chunks:
            chunk_already_removed = False
            if self.player_chunk_coords[X_COORD] - RENDER_DISTANCE > chunk[COORDS][X_COORD] or self.player_chunk_coords[X_COORD] + RENDER_DISTANCE < chunk[COORDS][X_COORD] and chunk_already_removed == False:
                for asteroid in chunk[ASTEROID_INDEX]:
                    asteroid.kill_asteroid()
                self.current_rendered_chunks.remove(chunk)
                chunk_already_removed = True

            if self.player_chunk_coords[Y_COORD] - RENDER_DISTANCE > chunk[COORDS][Y_COORD] or self.player_chunk_coords[Y_COORD] + RENDER_DISTANCE < chunk[COORDS][Y_COORD] and chunk_already_removed == False:
                for asteroid in chunk[ASTEROID_INDEX]:
                    asteroid.kill_asteroid()
                self.current_rendered_chunks.remove(chunk)
                chunk_already_removed = True

    def debugging(self):
        if pygame.font:
            font = pygame.font.Font("courbd.ttf", 12)

            player_coords1 = font.render(str(self.player_chunk_coords), 1, (255, 255, 255))
            player_coords = font.render('Player chunk coords: ', 1, (255, 255, 255))
            num_chunks1 = font.render(str(len(self.current_rendered_chunks)), 1, (255, 255, 255))
            num_chunks = font.render('Chunks rendered: ', 1, (255, 255, 255))
            num_sprites1 = font.render(str(len(self.group)), 1, (255, 255, 255))
            num_sprites = font.render('Sprites rendered: ', 1, (255, 255, 255))

            pc1_text = player_coords1.get_rect().move(150, 880)
            pc_text = player_coords.get_rect().move(10, 880)
            nc1_text = num_chunks1.get_rect().move(150, 865)
            nc_text = num_chunks.get_rect().move(10, 865)
            ns1_text = num_sprites1.get_rect().move(150, 850)
            ns_text = num_sprites.get_rect().move(10, 850)

            self.screen.blit(player_coords, pc_text)
            self.screen.blit(player_coords1, pc1_text)
            self.screen.blit(num_chunks, nc_text)
            self.screen.blit(num_chunks1, nc1_text)
            self.screen.blit(num_sprites, ns_text)
            self.screen.blit(num_sprites1, ns1_text)

    def update(self):
        self.update_current_player_coords()

        if 0 == len(self.current_rendered_chunks):
            self.generate_nearby_chunks()

        if self.player_moved_chunks():
            self.update_current_chunk_coords()
            self.generate_nearby_chunks()
            self.remove_far_chunks()

    def load_asteroid_data(self):
        image1 = pygame.image.load('Sprites/asteroid1.png')
        self.asteroid_image_set.append(image1)
        damage1 = 47
        self.asteroid_damage_set.append(damage1)
        image2 = pygame.image.load('Sprites/asteroid2.png')
        self.asteroid_image_set.append(image2)
        damage2 = 74
        self.asteroid_damage_set.append(damage2)
        image3 = pygame.image.load('Sprites/asteroid3.png')
        self.asteroid_image_set.append(image3)
        damage3 = 63
        self.asteroid_damage_set.append(damage3)
        image4 = pygame.image.load('Sprites/asteroid4.png')
        self.asteroid_image_set.append(image4)
        damage4 = 18
        self.asteroid_damage_set.append(damage4)
        image5 = pygame.image.load('Sprites/asteroid5.png')
        self.asteroid_image_set.append(image5)
        damage5 = 7
        self.asteroid_damage_set.append(damage5)
        image6 = pygame.image.load('Sprites/asteroid6.png')
        self.asteroid_image_set.append(image6)
        damage6 = 8
        self.asteroid_damage_set.append(damage6)