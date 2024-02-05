import pygame
import random
from os import path


class Bumper(pygame.sprite.Sprite):
    def __init__(self, x, y, anim):
        super().__init__()
        self.img_dir_enemy = path.join(path.dirname(__file__), "assets/img/enemy")
        self.bumper_anim = {'blue': [], 'red': [], 'green': []}
        for i in range(7):
            bumper_blue_file = f'bumper_blue_{i + 1}.png'
            bumper_red_file = f'bumper_red_{i + 1}.png'
            bumper_green_file = f'bumper_green_{i + 1}.png'
            img = pygame.image.load(path.join(self.img_dir_enemy, bumper_blue_file))
            self.bumper_anim['blue'].append(img)
            img = pygame.image.load(path.join(self.img_dir_enemy, bumper_red_file))
            self.bumper_anim['red'].append(img)
            img = pygame.image.load(path.join(self.img_dir_enemy, bumper_green_file))
            self.bumper_anim['green'].append(img)
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

    def spawn_bumper(self, all_sprites, bumpers):
        y = random.randint(80, 1000)
        color = random.choice(['blue', 'red', 'green'])
        bump = Bumper(2000, y, self.bumper_anim[color],)
        all_sprites.add(bump)
        bumpers.add(bump)
