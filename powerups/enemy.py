import pygame, random

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        self.rect.x += random.randint(-5,5)
        self.rect.y += random.randint(-5,5)
