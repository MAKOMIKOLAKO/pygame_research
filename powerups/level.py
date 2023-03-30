import pygame, random
from settings import tile_size, screen_width, screen_height
from tile import Tile
from player import Player
from bullet import Bullet
from enemy import Enemy
import time


class Level:
    def __init__(self, level_data, surface):

        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.explosions = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.setup_level(level_data)

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
        for i in range(3):
            enemy = Enemy((random.randint(300, screen_width), random.randint(0, screen_height)))
            self.enemies.add(enemy)


    def run(self):
        self.player.update(self.tiles)
        self.tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.enemies.draw(self.display_surface)
        self.player.sprite.draw_bullets(self.display_surface)
        collided_with = pygame.sprite.spritecollide(self.player.sprite, self.enemies, True)
        if collided_with:
            start_time = time.time()
            self.player.sprite.speed *= 2
            while True:
                current_time = time.time()
                if current_time - start_time >= 5:
                    self.player.sprite.speed = 8
                    break
        for bullet in self.player.sprite.bullets:
            bullet.explosions = pygame.sprite.Group()
            if pygame.time.get_ticks()-bullet.time>3000:
                bullet.spawn_explosions()
                print('this bomb has exploded')
                self.explosions.draw(self.display_surface)
                bullet.kill()


