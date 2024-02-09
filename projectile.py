import pygame
from os import path


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speedx, speedy, model):
        super().__init__()
        self.img_dir_fire = path.join(path.dirname(__file__), "assets/img/fire")
        if model == "yellow":
            self.image = pygame.image.load(
                path.join(self.img_dir_fire, "hit_1_yellow.png")
            )
        if model == "blue":
            self.image = pygame.image.load(
                path.join(self.img_dir_fire, "hit_1_blue.png")
            )
        self.imageW = self.image.get_width()
        self.imageH = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.imageW, self.imageH))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.damage = 100

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x > 2000:
            self.kill()
