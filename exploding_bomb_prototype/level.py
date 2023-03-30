import pygame
from settings import tile_size
from tile import Tile
from player import Player
from bullet import Bullet

class Level:
    def __init__(self, level_data, surface):

        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.setup_level(level_data)
        self.explosions = pygame.sprite.Group()

    def setup_level(self,layout):
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index*tile_size
                y = row_index*tile_size
                if cell == "x":
                    tile = Tile((x,y), tile_size)
                    #self.tiles.add(tile)
                elif cell == "p":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    def run(self):
        self.player.update(self.tiles)
        self.tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.player.sprite.draw_bullets(self.display_surface)
        for bullet in self.player.sprite.bullets:
            bullet.explosions = pygame.sprite.Group()
            if pygame.time.get_ticks()-bullet.time>3000:
                bullet.spawn_explosions()
                print('this bomb has exploded')

                self.explosions.draw(self.display_surface)
                bullet.kill()


