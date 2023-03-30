import pygame

class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__() # Inherits properties of pygame.sprite.Sprite

        self.image = pygame.Surface((size,size)) # Dimensions of tile
        self.image.fill("grey") # Tile is filled with grey
        self.rect = self.image.get_rect(topleft=pos)


