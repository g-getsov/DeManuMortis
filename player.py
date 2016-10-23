import pygame
from colors import Colors
from projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.width = 32
        self.height = 32
        self.acceleration_x = 0.5
        self.acceleration_y = 0.5
        self.velocity_x = 0
        self.velocity_y = 0
        self.max_velocity = 8
        self.on_ground = True
        self.image = pygame.image.load_extended("resources/player.png")
        self.rect = self.image.get_rect()
        self.moved_on_x_axis = False
        self.moved_on_y_axis = False
        self.projectiles_group = pygame.sprite.Group()

    def on_event(self, keys):
        self.moved_on_x_axis = True
        self.moved_on_y_axis = True

        if keys[pygame.K_LEFT]:
            self.velocity_x -= self.acceleration_x
        elif keys[pygame.K_RIGHT]:
            self.velocity_x += self.acceleration_x
        else:
            self.moved_on_x_axis = False
        if keys[pygame.K_UP]:
            self.velocity_y -= self.acceleration_y
        elif keys[pygame.K_DOWN]:
            self.velocity_y += self.acceleration_y
        else:
            self.moved_on_y_axis = False

        if keys[pygame.K_SPACE]:
            self.attack()

    def attack(self):
        projectile = Projectile(self.rect.x, self.rect.y)
        projectile.fire(self.velocity_x, self.velocity_y)
        projectile.add(self.projectiles_group)

    def update(self):
        self.update_position()
        self.projectiles_group.update()

    def update_position(self):
        self.adjust_velocity()
        self.speed_degradation()
        self.rect = self.rect.move(self.velocity_x, self.velocity_y)

    def speed_degradation(self):
        if not self.moved_on_x_axis:
            if self.velocity_x > 0.0:
                self.velocity_x -= self.acceleration_x
            else:
                self.velocity_x += self.acceleration_x

        if not self.moved_on_y_axis:
            if self.velocity_y > 0.0:
                self.velocity_y -= self.acceleration_y
            else:
                self.velocity_y += self.acceleration_y

    def adjust_velocity(self):
        if -0.01 < self.velocity_x < 0.01:
            self.velocity_x = 0

        if -0.01 < self.velocity_y < 0.01:
            self.velocity_y = 0

        if self.velocity_x > self.max_velocity:
            self.velocity_x = self.max_velocity
        elif self.velocity_x < -self.max_velocity:
            self.velocity_x = -self.max_velocity

        if self.velocity_y > self.max_velocity:
            self.velocity_y = self.max_velocity
        elif self.velocity_y < -self.max_velocity:
            self.velocity_y = -self.max_velocity

    def draw(self, display_surface):
        self.rect.clamp_ip(display_surface.get_rect())
        display_surface.blit(self.image, (self.rect.x, self.rect.y))
        self.projectiles_group.draw(display_surface)
