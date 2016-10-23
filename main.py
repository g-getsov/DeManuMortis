import pygame
from colors import Colors
from player import Player
from os import linesep
from map.tile_set import TileSet
from map.tile_map import TileMap


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._background = None
        self._size = self.weight, self.height = 800, 600
        self._player = None
        self._clock = None
        self._tile_map = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._background = pygame.Surface(self._size)
        self._background.fill(Colors.BLACK)
        self._running = True
        self._clock = pygame.time.Clock()
        self._player = Player()
        tile_set = TileSet()
        tile_set.construct_tile_set("resources/tileset.png", 32, 32)
        self._tile_map = TileMap()
        self._tile_map.construct_tile_map(tile_set, "resources/map/level_one.txt")

    def on_render(self):
        self._display_surf.blit(self._background, (0, 0))
        self._tile_map.draw(self._display_surf)
        self._player.draw(self._display_surf)
        pygame.display.update()

    def on_loop(self):
        self._clock.tick(60)
        self._player.update()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            self.on_event()
            self.on_loop()
            self.on_render()
        quit_game()

    def on_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                if event.key == pygame.K_ESCAPE:
                    quit_game()
            return

        self._player.on_event(pygame.key.get_pressed())

    def print_stats(self):
        stat_message = "Player stats:"
        stat_message += linesep + "X pos: " + str(self._player._rect.x) + " X vel:" + str(self._player._velocity_x)
        stat_message += linesep + "Y pos: " + str(self._player._rect.y) + " Y vel:" + str(self._player._velocity_y)
        print(stat_message)


def quit_game():
    pygame.quit()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
