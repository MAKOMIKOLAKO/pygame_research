import pygame
from explode import Explode
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('bomb (1).png')
        self.rect = self.image.get_rect(center=pos)
        self.time = pygame.time.get_ticks()
        self.pos = pos
        #self.explosions = pygame.sprite.Group()

    def spawn_explosions(self):
        counter = 0
        for i in range(4):
            explosion = Explode((self.pos[0] + counter, self.pos[1]))
            counter+=64
            self.explosions.add(explosion)
