import pygame
from colors import Colors


class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Projectile, self).__init__()
        self._width = 8
        self._height = 8
        self._velocity_x = 0
        self._velocity_y = 0
        self.image = pygame.Surface((self._width, self._height))
        self.image.fill(Colors.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._initial_speed = 3

    def fire(self, vel_x, vel_y):
        self._velocity_x = vel_x * 1.5
        self._velocity_y = vel_y * 1.5

    def update(self):
        self.rect = self.rect.move(self._velocity_x, self._velocity_y)

    def on_collision(self, target):
        pass
