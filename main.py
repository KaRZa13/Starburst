import pygame
from os import path
from game import Game

# Variables de dossier assets
img_dir_player = path.join(path.dirname(__file__), "assets/img/player")
img_dir_enemy = path.join(path.dirname(__file__), "assets/img/enemy")
img_dir_effect = path.join(path.dirname(__file__), "assets/img/effect")
img_dir_fire = path.join(path.dirname(__file__), "assets/img/fire")
snd_dir = path.join(path.dirname(__file__), "assets/sounds")

# Variables globales
WIDTH = 1920
HEIGHT = 1080
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialisation de pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot 'em up")
font_name = pygame.font.match_font("arial")
clock = pygame.time.Clock()

# Importation des éléments sonores

# Importation des éléments graphiques
background = pygame.image.load(path.join(img_dir_effect, "background.png"))
background_rect = background.get_rect()

# Enemy
enemies_color = ["bleu", "rouge", "vert", "jaune", "violet", "rose"]
enemies_img = []
for i in range(20):
    for color in enemies_color:
        enemy_file = f"{i + 1}-{color}.png"
        img = pygame.image.load(path.join(img_dir_enemy, enemy_file))
        img.set_colorkey(WHITE)
        enemies_img.append(img)

# Bumpers
bumper_anim = {"blue": [], "red": [], "green": []}
for i in range(7):
    bumper_blue_file = f"bumper_blue_{i + 1}.png"
    bumper_red_file = f"bumper_red_{i + 1}.png"
    bumper_green_file = f"bumper_green_{i + 1}.png"
    img = pygame.image.load(path.join(img_dir_enemy, bumper_blue_file))
    bumper_anim["blue"].append(img)
    img = pygame.image.load(path.join(img_dir_enemy, bumper_red_file))
    bumper_anim["red"].append(img)
    img = pygame.image.load(path.join(img_dir_enemy, bumper_green_file))
    bumper_anim["green"].append(img)

# Sprites
all_sprites = pygame.sprite.Group()
boss_projectiles = pygame.sprite.Group()

# Variable de jeu
running = True
game_over = False
game_pause = False
title_screen = True
game = Game(screen)
level = 1
next_level = 100
background_x = 0
bumper_loop = 0
base_velocity = 3
boss_level = 10
boss_spawned = False
velocity = base_velocity

while running:

    if title_screen:
        screen.fill((0, 0, 0))
        game.draw_text("Starburst", 64, WIDTH / 2, HEIGHT / 2 - 100, screen)
        game.draw_text("Press any key to start", 36, WIDTH / 2, HEIGHT / 2, screen)
        pygame.display.flip()

        # Attendre que le joueur appuie sur une touche pour démarrer
        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_key = False
                elif event.type == pygame.KEYDOWN:
                    waiting_for_key = False
                    title_screen = False

    if game_over:
        screen.fill((0, 0, 0))
        game.draw_text("Game Over", 64, WIDTH / 2, HEIGHT / 2, screen)
        game.draw_text("Press any key to go to title", 36, WIDTH / 2, HEIGHT / 2 + 50, screen)
        game.draw_text(f"Score : {game.player.score}", 36, WIDTH / 2, HEIGHT / 100, screen)
        pygame.display.flip()

        # Attendre que le joueur appuie sur une touche pour redémarrer
        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_key = False
                elif event.type == pygame.KEYDOWN:
                    waiting_for_key = False
                    game_over = False

                    game.player.health = game.player.max_health
                    game.player.score = 0
                    game.player.shield = game.player.max_shield

                    for bumper in game.all_bumpers.sprites():
                        bumper.kill()

                    for enemy in game.all_enemies.sprites():
                        enemy.kill()

                    game.player.reset_pos()

                    title_screen = True

    dt = clock.tick(FPS)

    # Création des ennemies
    if not boss_spawned:
        if len(game.all_enemies) == 0:
            pass  # game.spawn_enemy()

    # Gestion des évènements (clavier)
    for event in pygame.event.get():
        # Fermeture de la fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Pause et god mod
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not game_pause:
                    game.game_paused(WIDTH, HEIGHT, screen)
            if event.key == pygame.K_INSERT:
                pass

        # Test
        if event.type == pygame.KEYDOWN:
            pass

    collisions_projectile = pygame.sprite.groupcollide(game.player.all_projectiles, game.all_enemies, True, True)
    collisions_with_bumpers = pygame.sprite.groupcollide(game.player.all_projectiles, game.all_bumpers, True, True)
    player_collisions = pygame.sprite.groupcollide(pygame.sprite.Group(game.player), game.all_enemies, False, True)
    player_collisions_with_bumpers = pygame.sprite.groupcollide(pygame.sprite.Group(game.player), game.all_bumpers, False, True)

    # Gestion des collisions des projectiles avec les ennemis
    for projectile, enemy_list in collisions_projectile.items():
        for enemy in enemy_list:
            enemy.health -= projectile.damage
            game.player.score += enemy.points

    # Gestion des collisions des projectiles avec les bumpers
    for projectile, bumper_list in collisions_with_bumpers.items():
        for bumper in bumper_list:
            bumper.health -= projectile.damage
            game.player.score += bumper.points

    # Gestion des collisions du joueur avec les bumpers
    for player, bumper_list in player_collisions_with_bumpers.items():
        for bumper in bumper_list:
            game.player.health -= bumper.body_damage
            bumper.health -= game.player.body_damage
            game.player.score += bumper.points

    # Gestion des collisions du joueur avec les ennemis
    for player, enemy_list in player_collisions.items():
        for enemy in enemy_list:
            game.player.health -= enemy.body_damage
            enemy.health -= game.player.body_damage
            game.player.score += enemy.points

    # Actualisation de l'état du jeu en fonction de la santé du joueur
    if game.player.health <= 0:
        game_over = True

    # Gestion des niveaux
    if game.player.score >= next_level:
        level += 1
        next_level *= 3
        velocity *= 1.25
        for bumper in bumper_list:
            bumper.velocity = velocity

    # Boucle pour créer les bumpers
    if not boss_spawned:
        bumper_loop += dt
        if bumper_loop >= 250:
            game.spawn_bumper(bumper_anim, velocity)
            bumper_loop = 0
            bumper_loop += dt

    # Scrolling du background
    background_x -= 2
    background_rel_x = background_x % background_rect.width

    # Draw / Render
    game.render(screen, background, background_rect, background_rel_x)

    """if level == boss_level:
        boss_spawned = True
        boss = Boss(screen, all_sprites, boss_projectiles, shoot_sound, player)
        all_sprites.add(boss)"""

    pygame.display.flip()

pygame.quit()
