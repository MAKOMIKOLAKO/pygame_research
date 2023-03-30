import pygame
from bullet import Bullet
from support import import_folder
class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.animations = {}
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.bullets = pygame.sprite.Group()
        self.firing = False
        self.fire_sound = pygame.mixer.Sound('sounds/explode.mp3')
        self.status="idle"

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]

    def import_character_assets(self):
        character_path = "avatar/"
        self.animations = {"idle":[], "run_right":[], "run_left":[]}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_status(self):
        if self.direction.x == 0:
            self.status = 'idle'
        elif self.direction.x > 0:
            self.status = 'run_right'
        elif self.direction.x < 0:
            self.status = 'run_left'

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.x = 0
            self.direction.y = 0

        if keys[pygame.K_SPACE] and not self.firing:
            self.fire()
            self.firing = True
        elif not keys[pygame.K_SPACE] and self.firing:
            self.firing = False

    def horizontal_movement_collision(self, tiles):
        # Function to handle horizontal collisions
        self.rect.x += self.direction.x * self.speed


        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = tile.rect.right
                elif self.direction.x > 0:
                    self.rect.right = tile.rect.left

    def vertical_movement_collision(self, tiles):
        # Function to handle vertical collisions
        self.rect.y += self.direction.y * self.speed # Changes vertical position of avatar, increased by speed (set in settings)
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = tile.rect.top
                elif self.direction.y < 0:
                    self.rect.top = tile.rect.bottom
    def fire(self):
        bullet = Bullet((self.rect.centerx, self.rect.centery), self.direction.x)
        self.bullets.add(bullet)
        pygame.mixer.Sound.play(self.fire_sound)

    def draw_bullets(self, surface):
        self.bullets.draw(surface)


    def update(self, tiles):
        self.get_input()
        self.horizontal_movement_collision(tiles)
        self.vertical_movement_collision(tiles)
        self.bullets.update()
        self.get_status()
        self.animate()





