import pygame
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self, img, move):
        super().__init__()
        self.image = img
        self.move = move
        self.health = 100
        self.points = 10
        self.damage = 50
        self.body_damage = 50

    def is_alive(self):
        return self.health <= 0
