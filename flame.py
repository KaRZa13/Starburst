import pygame
from os import path


class Flame(pygame.sprite.Sprite):
    def __init__(self, x, y, player) -> None:
        super().__init__()
        self.player = player
        self.img_dir_flame = path.join(path.dirname(__file__), "assets/img/effect")
        self.flame = pygame.image.load(path.join(self.img_dir_flame, "flame_1.png"))
        self.image = pygame.transform.scale(self.flame, (30, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
