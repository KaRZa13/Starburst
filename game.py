import pygame
import random
from bumper import Bumper
from enemy import Enemy


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
        self.draw_text("Game paused", 64, WIDTH / 2 - 175, HEIGHT / 2 - 25, surface)
        pygame.display.flip()
        while game_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_paused = False

    def spawn_bumper(self, all_sprites, bumpers, bumper_anim, velocity):
        y = random.randint(80, 1000)
        color = random.choice(["blue", "red", "green"])
        bump = Bumper(2000, y, bumper_anim[color])
        bump.velocity = velocity
        all_sprites.add(bump)
        bumpers.add(bump)

    def spawn_enemy(self, nb, enemies_img, player, all_sprites, enemies, WIDTH, HEIGHT):
        global x, y
        img = random.choice(enemies_img)
        move = random.choice(
            [
                "sin_x",
                "diagonal",
                "line_up",
                "line_down",
                "line_left",
                "sin_up",
                "sin_down",
            ]
        )
        player_y = player.rect.y
        player_x = player.rect.x

        if nb % 2 != 0:
            nb += 1

        if move == "sin_up":
            if random.random() > 0.8:
                move = "sin_up_line_left"
                x = 1900
                y = 1080
                for i in range(nb):
                    if i % 2:
                        x += img.get_height()
                    else:
                        x -= img.get_width()
                    amplitude = random.randrange(20, 100)

                    enemy = Enemy(
                        img, x, y, move, amplitude, player_x, player_y, WIDTH, HEIGHT
                    )
                    y -= img.get_height() * 2
                    all_sprites.add(enemy)
                    enemies.add(enemy)

        if move == "sin_down":
            if random.random() > 0.8:
                move = "sin_down_line_left"
                x = 1900
                y = 0
                for i in range(nb):
                    if i % 2:
                        x += img.get_height()
                    else:
                        x -= img.get_width()
                    amplitude = random.randrange(20, 100)

                    enemy = Enemy(
                        img, x, y, move, amplitude, player_x, player_y, WIDTH, HEIGHT
                    )
                    y += img.get_height() * 2
                    all_sprites.add(enemy)
                    enemies.add(enemy)

        if move == "line_up":
            amplitude = 0
            x = random.randint(1, 1950)
            y = 1200
            for i in range(nb):
                enemy = Enemy(
                    img, x, y, move, amplitude, player_x, player_y, WIDTH, HEIGHT
                )
                if i % 2:
                    x += img.get_width()
                else:
                    x -= img.get_width()
                y -= img.get_height() * 2
                all_sprites.add(enemy)
                enemies.add(enemy)

        if move == "line_down":
            amplitude = 0
            x = random.randint(1, 1950)
            y = -200
            for i in range(nb):
                enemy = Enemy(
                    img, x, y, move, amplitude, player_x, player_y, WIDTH, HEIGHT
                )
                if i % 2:
                    x += img.get_width()
                else:
                    x -= img.get_width()
                y += img.get_height() * 2
                all_sprites.add(enemy)
                enemies.add(enemy)

        if move == "line_left":
            amplitude = 0
            if nb <= 8:
                x = 2200
                y = random.randrange(150, 930)
            for i in range(nb):
                enemy = Enemy(
                    img, x, y, move, amplitude, player_x, player_y, WIDTH, HEIGHT
                )
                if i % 2:
                    y += img.get_width()
                else:
                    y -= img.get_width()
                x -= img.get_height() * 2
                all_sprites.add(enemy)
                enemies.add(enemy)

            if nb > 8:
                x1 = 2200
                x2 = 2200
                y1 = 400
                y2 = 700
                nb_line1 = 0
                nb_line2 = 0
                for i in range(nb):
                    if i % 2:
                        if nb_line1 % 2:
                            y1 -= img.get_height()
                        else:
                            y1 += img.get_height()
                            enemy = Enemy(
                                img,
                                x1,
                                y1,
                                move,
                                amplitude,
                                player_x,
                                player_y,
                                WIDTH,
                                HEIGHT,
                            )
                            nb_line1 += 1
                    else:
                        if nb_line2 % 2:
                            y2 -= img.get_height()
                        else:
                            y2 += img.get_height()
                            enemy = Enemy(
                                img,
                                x2,
                                y2,
                                move,
                                amplitude,
                                player_x,
                                player_y,
                                WIDTH,
                                HEIGHT,
                            )
                            nb_line2 += 1
                    x1 += img.get_width() * 2
                    x2 += img.get_width() * 2
                    all_sprites.add(enemy)
                    enemies.add(enemy)

        if move == "diagonal":
            amplitude = 0
            if nb <= 8:
                move = random.choice(["diagonal_up", "diagonal_down"])
                if move == "diagonal_up":
                    y = 0
                else:
                    y = 1080
                x = 2000

                for i in range(nb):
                    enemy = Enemy(
                        img, x, y, move, amplitude, player_x, player_y, WIDTH, HEIGHT
                    )
                    if y <= 0:
                        x += img.get_width() * 2
                    if y >= 1080:
                        y -= img.get_width() * 2
                    x -= img.get_width() * 2
                    all_sprites.add(enemy)
                    enemies.add(enemy)

            if nb > 8:
                x1 = 2000
                x2 = 2000
                y1 = 0
                y2 = 1080
                for i in range(nb):
                    if i % 2:
                        enemy = Enemy(
                            img,
                            x1,
                            y1,
                            "diagonal_up",
                            amplitude,
                            player_x,
                            player_y,
                            WIDTH,
                            HEIGHT,
                        )
                    else:
                        enemy = Enemy(
                            img,
                            x2,
                            y2,
                            "diagonal_down",
                            amplitude,
                            player_x,
                            player_y,
                            WIDTH,
                            HEIGHT,
                        )

                    y1 -= img.get_height() * 2
                    y2 += img.get_height() * 2
                    x1 -= img.get_width() + 10
                    x2 -= img.get_width() + 10
                    all_sprites.add(enemy)
                    enemies.add(enemy)

        if move == "sin_x":
            if nb <= 8:
                y = random.randrange(100, 980)
                x = 2200
                amplitude = 50
                for i in range(nb):
                    enemy = Enemy(
                        img, x, y, move, amplitude, player_x, player_y, WIDTH, HEIGHT
                    )
                    x += img.get_width() * 2
                    if i % 2:
                        x -= 25
                        amplitude = 100
                    else:
                        x += 25
                        amplitude = 50
                    all_sprites.add(enemy)
                    enemies.add(enemy)

            if nb > 8:
                x1 = 2200
                x2 = 2200
                y = [150, 930]
                amp = [50, 100]
                compteur = 0
                compteur_amp1 = 0
                compteur_amp2 = 0
                for i in range(nb):
                    if i % 2:
                        if compteur_amp1 % 2:
                            amplitude = amp[0]
                        else:
                            amplitude = amp[1]
                        enemy = Enemy(
                            img,
                            x1,
                            y[compteur],
                            move,
                            amplitude,
                            player_x,
                            player_y,
                            WIDTH,
                            HEIGHT,
                        )
                        x1 += img.get_width() * 2
                        compteur += 1
                        compteur_amp1 += 1

                    else:
                        if compteur_amp2 % 2:
                            amplitude = amp[1]
                        else:
                            amplitude = amp[0]
                        enemy = Enemy(
                            img,
                            x2,
                            y[compteur],
                            move,
                            amplitude,
                            player_x,
                            player_y,
                            WIDTH,
                            HEIGHT,
                        )
                        x2 -= img.get_width() * 2
                        compteur -= 1
                        compteur_amp2 += 1
                    all_sprites.add(enemy)
                    enemies.add(enemy)
