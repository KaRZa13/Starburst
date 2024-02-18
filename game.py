import pygame
import random
from bumper import Bumper
from player import Player


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.bumper = Bumper()
        self.all_sprites = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()
        self.all_bumpers = pygame.sprite.Group()
        self.pressed = {}
        self.level = 1

    def render(self, background, background_rect, background_rel_x):
        self.screen.blit(background, (background_rel_x - background_rect.width, 0))
        self.screen.blit(background, (background_rel_x, 0))
        self.screen.blit(self.player.image, self.player.rect)
        self.player.all_projectiles.draw(self.screen)
        self.player.all_projectiles.update()
        self.all_sprites.draw(self.screen)
        self.player.update_bar(self.screen)
        self.player.create_flame(self.all_sprites)
        self.all_sprites.update()
        self.player.update()
        self.draw_text(f"Score : {self.player.score}", 20, 10, 10)
        self.draw_text(f"Health : {self.player.health}", 20, 10, 40)
        self.draw_text(f"Level : {self.level}", 20, 10, 70)

    def draw_text(self, text, size, x, y):
        font_name = pygame.font.match_font("arial")
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect.center)

    def game_paused(self, WIDTH, HEIGHT):
        game_paused = True
        self.draw_text("Game paused", 64, WIDTH / 2 - 175, HEIGHT / 2 - 25)
        pygame.display.flip()
        while game_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_paused = False

    def level(self):
        pass

    def spawn_bumper(self, velocity):
        bumper = Bumper()
        bumper.velocity = velocity
        self.all_sprites.add(bumper)
        self.all_bumpers.add(bumper)

    def spawn_enemies(self):
        pass


'''def spawn_enemy(self):
min_enemy = player.power * 2
max_enemy = player.power * 5
nb = random.randrange(min_enemy, max_enemy)
move = random.choice(["line", "line_up", "line_down", "diagonal", "sin_x", "sin_up", "sin_down"])
enemy = Enemy(img, move)'''
