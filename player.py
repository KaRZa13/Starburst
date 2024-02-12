import pygame
from os import path
from projectile import Projectile
from flame import Flame


class Player(pygame.sprite.Sprite):
    def __init__(self, surface, all_sprites, player_projectiles, player_flames, shoot_sound):
        super().__init__()
        self.img_dir_player = path.join(path.dirname(__file__), "assets/img/player")
        self.player_img = pygame.image.load(path.join(self.img_dir_player, "ship.png"))
        self.player_imgR = pygame.image.load(path.join(self.img_dir_player, "ship_right.png"))
        self.player_imgL = pygame.image.load(path.join(self.img_dir_player, "ship_left.png"))
        self.surface = surface
        self.image = pygame.transform.scale(self.player_img, (75, 60))
        self.image.set_colorkey((0, 0, 0))
        self.all_projectiles = pygame.sprite.Group()
        self.health = 300
        self.max_health = 300
        self.shield = 100
        self.max_shield = 300
        self.velocity = 3
        self.power = 5
        self.score = 0
        self.shot_delay = 180
        self.rect = self.image.get_rect()
        self.rect.y = surface.get_rect().height / 2 - 20
        self.rect.x = surface.get_rect().width - 1900
        self.last_shot = pygame.time.get_ticks()
        self.all_sprites = all_sprites
        self.player_projectiles = player_projectiles
        self.player_flames = player_flames
        self.flame = Flame(self.rect.x, self.rect.y, self)
        self.shot_sound = shoot_sound
        self.body_damage = 100

    def create_flame(self, all_sprites):
        self.flame.rect.x = self.rect.x - 10
        self.flame.rect.y = self.rect.y + 20
        all_sprites.add(self.flame)
        self.player_flames.add(self.flame)

    def damage(self, damage):
        if self.health > 0:
            self.health -= damage

    def update_bar(self, surface):
        # Shield bar
        pygame.draw.rect(surface, (255, 255, 255), [8, 1028, self.max_health + 4, 14])
        pygame.draw.rect(surface, (60, 63, 60), [10, 1030, self.max_shield, 10])
        pygame.draw.rect(surface, (64, 171, 236), [10, 1030, self.shield, 10])
        # Health bar
        pygame.draw.rect(surface, (255, 255, 255), [8, 1048, self.max_health + 4, 14])
        pygame.draw.rect(surface, (60, 63, 60), [10, 1050, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [10, 1050, self.health, 10])

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            self.image = pygame.transform.scale(self.player_imgL, (75, 60))
            if self.rect.y > -25:
                self.rect.y -= self.velocity
        elif keys[pygame.K_s]:
            self.image = pygame.transform.scale(self.player_imgR, (75, 60))
            if self.rect.y < 1045:
                self.rect.y += self.velocity
        else:
            self.image = pygame.transform.scale(self.player_img, (75, 60))

        if keys[pygame.K_q] and self.rect.x > -30:
            self.rect.x -= self.velocity
        if keys[pygame.K_d] and self.rect.x < 1870:
            self.rect.x += self.velocity

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shot_delay:
            self.last_shot = now
            y_offsets = [[25], [5, 45], [5, 25, 45], [0, 20, 40, 60], [-15, 5, 25, 45, 65]]
            for i in range(1, 5):
                projectiles = [Projectile(self.rect.x + 75, self.rect.y + y, 10, 0)
                               for y in y_offsets[self.power - 1][:self.power]]
                self.all_sprites.add(projectiles)
                self.player_projectiles.add(projectiles)
                self.shot_sound.play()

    def reset_pos(self):
        self.rect.y = self.surface.get_rect().height / 2 - 20
        self.rect.x = self.surface.get_rect().width - 1900
