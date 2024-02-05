import pygame
import random
from os import path
from bumper import Bumper


class Game:
    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.pressed = {}

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
