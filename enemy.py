import pygame
from os import path
from random import choice, randint
from math import sin


class Enemy(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.img_dir_enemy = path.join(path.dirname(__file__), "assets/img/enemy")
        self.enemies_color = ["bleu", "rouge", "vert", "jaune", "violet", "rose"]
        self.enemies_img = []
        for i in range(20):
            for color in self.enemies_color:
                enemy_file = f"{i + 1}-{color}.png"
                self.img = pygame.image.load(path.join(self.img_dir_enemy, enemy_file))
                self.enemies_img.append(self.img)
        self.health = 100
        self.points = 10
        self.damage = 50
        self.body_damage = 50
        self.rect_y = 0
        self.rect_x = 0
        self.speedx = 0
        self.speedy = 0
        self.angle = 0

    def is_alive(self) -> bool:
        return self.health < 0

    def update(self) -> None:
        move = choice(["line_up", "line_down", "diagonal",
                       "sin_x", "sin_up", "sin_down"])
        match move:
            case "line_up":
                self.rect_y = 1200
                self.rect_x = randint(250, 1800)
                self.speedx = 0
                self.speedy = -3
            case "line_down":
                self.rect_y = -200
                self.rect_x = randint(250, 1800)
                self.speedx = 0
                self.speedy = 3
            case "diagonal_up":
                self.rect_y = 1200
                self.rect_x = randint(950, 1920)
                self.speedx = -3
                self.speedy = -3
            case "diagonal_down":
                self.rect_y = -200
                self.rect_x = randint(950, 1920)
                self.speedx = -3
                self.speedy = -3
            case "sin_x":
                amplitude = 250
                frequency = 0.01
                self.rect_y = randint(150, 950)
                self.rect_x = 2000
                self.speedx = -3
                self.speedy = amplitude * sin(self.angle) + 300
                self.angle += frequency
            case "sin_up":
                amplitude = 250
                frequency = 0.01
                self.rect_y = 1200
                self.rect_x = randint(250, 1800)
                self.speedx = amplitude * sin(self.angle) + 300
                self.speedy = -3
                self.angle += frequency
            case "sin_down":
                amplitude = 250
                frequency = 0.01
                self.rect_y = -200
                self.rect_x = randint(250, 1800)
                self.speedx = amplitude * sin(self.angle) + 300
                self.speedy = 3
                self.angle += frequency
