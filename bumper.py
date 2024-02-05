import pygame
from os import path


class Bumper(pygame.sprite.Sprite):
    def __init__(self, x, y, anim):
        super().__init__()
        self.anim = anim
        self.origin_image = anim[0]

        self.image = self.origin_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 3
        self.last_update = pygame.time.get_ticks()
        self.nb_anim = 0

    def update(self):
        self.anime()
        self.rect.x -= self.velocity
        if self.rect.x < -200:
            self.kill()

    def anime(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 180:
            self.last_update = now
            if self.nb_anim >= 7:
                self.nb_anim = 0
            new_image = self.anim[self.nb_anim]
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.nb_anim += 1
