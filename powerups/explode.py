import pygame

class Explode(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('radius.png')
        self.rect = self.image.get_rect(center=pos)
        self.time = pygame.time.get_ticks()

    """def update(self):
        if pygame.time.get_ticks()-self.time>3000:
            self.kill()"""
