import pygame
from tile import Tile


class TileSet:

    def __init__(self):
        self.tiles = []

    def construct_tile_set(self, image_path, tile_widht, tile_height):
        image = self.load_set_image(image_path)
        self.deconstruct_set_image(image, tile_widht, tile_height)

    # deconstructs the tileset into individual tiles reading it from left to right
    def deconstruct_set_image(self, image, tile_width, tile_height):

        image_width = image.get_width()
        image_height = image.get_height()

        # template
        subsurface_template = pygame.Surface((tile_width, tile_height))
        subsurface_rect = subsurface_template.get_rect()

        pos_x = 0
        pos_y = 0

        while ((pos_y + 1) * tile_height) < image_height:

            while ((pos_x + 1) * tile_width) < image_width:

                tile = Tile(image.subsurface(subsurface_rect))
                self.tiles.append(tile)
                pos_x += 1
                subsurface_rect = subsurface_rect.move(tile_width, 0)

            subsurface_rect = subsurface_rect.move(-tile_width*pos_x, tile_height)
            pos_x = 0
            pos_y += 1

    @staticmethod
    def load_set_image(image_path):
        image = pygame.image.load_extended(image_path)
        return image

    def get_tile(self, tile_index):
        return self.tiles[tile_index]
