import pygame
from os import path
from projectile import Projectile
from flame import Flame


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.img_dir_player = path.join(path.dirname(__file__), "assets/img/player")
        self.snd_dir = path.join(path.dirname(__file__), "assets/sounds")
        self.shoot_sound = pygame.mixer.Sound(path.join(self.snd_dir, "shoot_player.wav"))
        self.shoot_sound.set_volume(0.1)
        self.player_img = pygame.image.load(path.join(self.img_dir_player, "ship.png"))
        self.player_imgR = pygame.image.load(path.join(self.img_dir_player, "ship_right.png"))
        self.player_imgL = pygame.image.load(path.join(self.img_dir_player, "ship_left.png"))
        self.image = pygame.transform.scale(self.player_img, (75, 60))
        self.all_projectiles = pygame.sprite.Group()
        self.player_projectiles = pygame.sprite.Group()
        self.player_flames = pygame.sprite.Group()
        self.health = 300
        self.max_health = 300
        self.shield = 100
        self.max_shield = 300
        self.velocity = 5
        self.power = 5
        self.score = 0
        self.shot_delay = 180
        self.rect = self.image.get_rect()
        self.rect.y = 540
        self.rect.x = 20
        self.last_shot = pygame.time.get_ticks()
        self.flame = Flame(self.rect.x, self.rect.y, self)
        self.body_damage = 100

    def create_flame(self, all_sprites) -> None:
        self.flame.rect.x = self.rect.x - 10
        self.flame.rect.y = self.rect.y + 20
        all_sprites.add(self.flame)
        self.player_flames.add()

    def damage(self, damage) -> None:
        if self.health > 0:
            self.health -= damage

    def update_bar(self, surface) -> None:
        # Shield bar
        pygame.draw.rect(surface, (255, 255, 255), [8, 1028, self.max_health + 4, 14])
        pygame.draw.rect(surface, (60, 63, 60), [10, 1030, self.max_shield, 10])
        pygame.draw.rect(surface, (64, 171, 236), [10, 1030, self.shield, 10])
        # Health bar
        pygame.draw.rect(surface, (255, 255, 255), [8, 1048, self.max_health + 4, 14])
        pygame.draw.rect(surface, (60, 63, 60), [10, 1050, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [10, 1050, self.health, 10])

    def update(self) -> None:
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

    def shoot(self) -> None:
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shot_delay:
            self.last_shot = now
            y_offsets = [[25], [5, 45], [5, 25, 45], [0, 20, 40, 60], [-15, 5, 25, 45, 65]]
            for y in y_offsets[self.power - 1][:self.power]:
                projectile = Projectile(self.rect.x + 75, self.rect.y + y, 10, 0)
                self.all_projectiles.add(projectile)
                self.player_projectiles.add(projectile)
            self.shoot_sound.play()

    def reset_pos(self) -> None:
        self.rect.y = 540
        self.rect.x = 20
