import pygame
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(
        self, img, x, y, move, amplitude, target_x, target_y, max_width, max_height
    ):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.start_x = x
        self.start_y = y
        self.target_x = target_x
        self.target_y = target_y
        self.move = move
        self.angle = 0
        self.amplitude = amplitude
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery
        self.velocity = 5
        self.max_width = max_width
        self.max_height = max_height
        self.health = 100
        self.points = 10
        self.damage = 50
        self.body_damage = 50

    def update(self):
        if self.move == "sin_x":
            self.move_sin_x()
            if (
                self.rect.bottom >= self.max_height
                or self.rect.left <= 0
                or self.rect.right >= self.max_width
            ):
                self.kill()

        # if self.move == "sin_up":

    def move_sin_x(self):
        if self.angle >= 360:
            self.angle = 0
        self.rect.centery += 3
        self.rect.centerx = self.center_x + self.amplitude * math.cos(self.angle)
        self.angle += 6

    def is_alive(self):
        return self.health <= 0
