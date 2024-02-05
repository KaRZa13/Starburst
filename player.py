import pygame
from os import path
from projectile import Projectile
from flame import Flame


class Player(pygame.sprite.Sprite):
    def __init__(self, surface, all_sprites, players_projectiles, player_flames, shoot_sound):
        super().__init__()
        self.img_dir_player = path.join(path.dirname(__file__), "assets/img/player")
        self.player_img = pygame.image.load(path.join(self.img_dir_player, "ship.png"))
        self.player_imgR = pygame.image.load(path.join(self.img_dir_player, "ship_right.png"))
        self.player_imgL = pygame.image.load(path.join(self.img_dir_player, "ship_left.png"))
        self.image = pygame.transform.scale(self.player_img, (75, 60))
        self.image.set_colorkey((0, 0, 0))
        self.model_projectile = "blue"
        self.all_projectiles = pygame.sprite.Group()
        self.health = 300
        self.max_health = 300
        self.shield = 100
        self.max_shield = 300
        self.velocity = 5
        self.power = 3
        self.score = 0
        self.shot_delay = 180
        self.rect = self.image.get_rect()
        self.rect.y = surface.get_rect().height/2 - 20
        self.rect.x = surface.get_rect().width - 1900
        self.last_shot = pygame.time.get_ticks()
        self.all_sprites = all_sprites
        self.players_projectiles = players_projectiles
        self.player_flames = player_flames
        self.flame = Flame(self.rect.x, self.rect.y, self)
        self.shot_sound = shoot_sound

    def create_flame(self, all_sprites):
        self.flame.rect.x = self.rect.x - 10
        self.flame.rect.y = self.rect.y + 20
        all_sprites.add(self.flame)
        self.player_flames.add(self.flame)

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
            if self.model_projectile == "blue":
                if self.power == 1:
                    projectile1 = Projectile(self.rect.x + 75, self.rect.y + 25, 10, 0, self.model_projectile)
                if self.power == 2:
                    projectile1 = Projectile(self.rect.x + 75, self.rect.y + 5, 10, 0, self.model_projectile)
                    projectile2 = Projectile(self.rect.x + 75, self.rect.y + 45, 10, 0, self.model_projectile)
                if self.power == 3:
                    projectile1 = Projectile(self.rect.x + 75, self.rect.y + 5, 10, 0, self.model_projectile)
                    projectile2 = Projectile(self.rect.x + 75, self.rect.y + 25, 10, 0, self.model_projectile)
                    projectile3 = Projectile(self.rect.x + 75, self.rect.y + 45, 10, 0, self.model_projectile)
                if self.power == 4:
                    projectile1 = Projectile(self.rect.x + 75, self.rect.y + 0, 10, 0, self.model_projectile)
                    projectile2 = Projectile(self.rect.x + 75, self.rect.y + 20, 10, 0, self.model_projectile)
                    projectile3 = Projectile(self.rect.x + 75, self.rect.y + 40, 10, 0, self.model_projectile)
                    projectile4 = Projectile(self.rect.x + 75, self.rect.y + 60, 10, 0, self.model_projectile)
                if self.power == 5:
                    projectile1 = Projectile(self.rect.x + 75, self.rect.y - 15, 10, 0, self.model_projectile)
                    projectile2 = Projectile(self.rect.x + 75, self.rect.y + 5, 10, 0, self.model_projectile)
                    projectile3 = Projectile(self.rect.x + 75, self.rect.y + 25, 10, 0, self.model_projectile)
                    projectile4 = Projectile(self.rect.x + 75, self.rect.y + 45, 10, 0, self.model_projectile)
                    projectile5 = Projectile(self.rect.x + 75, self.rect.y + 65, 10, 0, self.model_projectile)

            if self.model_projectile == "yellow":
                if self.power == 1:
                    projectile1 = Projectile(self.rect.x + 75, self.rect.y + 25, 10, 0, self.model_projectile)
                if self.power == 2:
                    projectile1 = Projectile(self.rect.x + 75, self.rect.y + 5, 10, -2, self.model_projectile)
                    projectile2 = Projectile(self.rect.x + 75, self.rect.y + 45, 10, +2, self.model_projectile)
                if self.power == 3:
                    pass
                if self.power == 4:
                    pass
                if self.power == 5:
                    pass

            if self.power == 1:
                self.all_sprites.add(projectile1)
                self.players_projectiles.add(projectile1)

            if self.power == 2:
                self.all_sprites.add(projectile1)
                self.all_sprites.add(projectile2)
                self.players_projectiles.add(projectile1)
                self.players_projectiles.add(projectile2)

            if self.power == 3:
                self.all_sprites.add(projectile1)
                self.all_sprites.add(projectile2)
                self.all_sprites.add(projectile3)
                self.players_projectiles.add(projectile1)
                self.players_projectiles.add(projectile2)
                self.players_projectiles.add(projectile3)

            if self.power == 4:
                self.all_sprites.add(projectile1)
                self.all_sprites.add(projectile2)
                self.all_sprites.add(projectile3)
                self.all_sprites.add(projectile4)
                self.players_projectiles.add(projectile1)
                self.players_projectiles.add(projectile2)
                self.players_projectiles.add(projectile3)
                self.players_projectiles.add(projectile4)

            if self.power == 5:
                self.all_sprites.add(projectile1)
                self.all_sprites.add(projectile2)
                self.all_sprites.add(projectile3)
                self.all_sprites.add(projectile4)
                self.all_sprites.add(projectile5)
                self.players_projectiles.add(projectile1)
                self.players_projectiles.add(projectile2)
                self.players_projectiles.add(projectile3)
                self.players_projectiles.add(projectile4)
                self.players_projectiles.add(projectile5)

            self.shot_sound.play()
