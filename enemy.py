import pygame
from os import path
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self, move):
        super().__init__()
        self.img_dir_enemy = path.join(path.dirname(__file__), "assets/img/enemy")
        self.enemies_color = ["bleu", "rouge", "vert", "jaune", "violet", "rose"]
        self.enemies_img = []
        for i in range(20):
            for color in self.enemies_color:
                enemy_file = f"{i + 1}-{color}.png"
                self.img = pygame.image.load(path.join(self.img_dir_enemy, enemy_file))
                self.enemies_img.append(self.img)
        self.move = move
        self.health = 100
        self.points = 10
        self.damage = 50
        self.body_damage = 50

    def is_alive(self):
        return self.health <= 0
