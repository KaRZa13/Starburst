import pygame
import random
from os import path
from bumper import Bumper


class Game:
    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.pressed = {}
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

    def draw_text(self, text, size, x, y, surface):
        font_name = pygame.font.match_font("arial")
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x, y))
        surface.blit(text_surface, text_rect.center)

    def game_paused(self, WIDTH, HEIGHT, surface):
        game_paused = True
        self.draw_text("Game paused", 64, WIDTH/2 - 175, HEIGHT/2 - 25, surface)
        pygame.display.flip()
        while game_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_paused = False

    def spawn_bumper(self, all_sprites, bumpers):
        y = random.randint(80, 1000)
        color = random.choice(['blue', 'red', 'green'])
        bump = Bumper(2000, y, self.bumper_anim[color],)
        all_sprites.add(bump)
        bumpers.add(bump)

