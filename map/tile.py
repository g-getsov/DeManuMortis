import pygame


class Tile(pygame.sprite.Sprite):

    def __init__(self, image):
        super(Tile, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

        self.is_solid = False

    def on_collision(self):
        pass
