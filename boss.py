import pygame
from projectile import *
import math


class Boss(pygame.sprite.Sprite):
    def __init__(self, surface, all_sprites, boss_projectiles, shoot_sound, player):
        super().__init__()
        self.img_dir_boss = path.join(path.dirname(__file__), "assets/img/enemy")
        self.player_img = pygame.image.load(path.join(self.img_dir_boss, "9-rose.png"))
        self.image = pygame.transform.scale(self.player_img, (75, 60))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.y = surface.get_rect().height / 2
        self.rect.x = surface.get_rect().width / 2
        self.all_projectiles = pygame.sprite.Group()
        self.all_sprites = all_sprites
        self.boss_projectiles = boss_projectiles
        self.shot_sound = shoot_sound
        self.health = 1000
        self.player = player
        self.velocity = 2
        self.damage = 50
        self.shoot_delay = 500
        self.last_shoot_time = pygame.time.get_ticks()

    def update(self):
        self.shoot(self.player)

    def move(self):
        self.rect.x += self.velocity

    def shoot(self, player):
        now = pygame.time.get_ticks()
        if now - self.last_shoot_time > self.shoot_delay:
            # Calcul de l'angle entre le boss et le joueur
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            angle = math.atan2(dy, dx)

            # Création du projectile et ajout à un groupe de sprites
            speedx = math.cos(angle) * 5  # Vitesse horizontale du projectile
            speedy = math.sin(angle) * 5  # Vitesse verticale du projectile
            new_projectile = Projectile(
                self.rect.centerx, self.rect.centery, speedx, speedy, "yellow"
            )
            self.all_projectiles.add(new_projectile)

            # Jouer le son de tir
            self.shot_sound.play()

            # Mise à jour du temps du dernier tir
            self.last_shoot_time = now
