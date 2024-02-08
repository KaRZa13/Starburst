import random
import pygame
from os import path
from player import Player
from game import Game

# Variables de dossier assets
img_dir_player = path.join(path.dirname(__file__), "assets/img/player")
img_dir_enemy = path.join(path.dirname(__file__), "assets/img/enemy")
img_dir_effect = path.join(path.dirname(__file__), "assets/img/effect")
img_dir_fire = path.join(path.dirname(__file__), 'assets/img/fire')
snd_dir = path.join(path.dirname(__file__), 'assets/sounds')


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

# Enemy
enemies_color = ['bleu', 'rouge', 'vert', 'jaune', 'violet', 'rose']
enemies_img = []
for i in range(20):
    for color in enemies_color:
        enemy_file = f"{i + 1}-{color}.png"
        img = pygame.image.load(path.join(img_dir_enemy, enemy_file))
        img.set_colorkey(WHITE)
        enemies_img.append(img)

# Bumpers
bumper_anim = {'blue': [], 'red': [], 'green': []}
for i in range(7):
    bumper_blue_file = f'bumper_blue_{i + 1}.png'
    bumper_red_file = f'bumper_red_{i + 1}.png'
    bumper_green_file = f'bumper_green_{i + 1}.png'
    img = pygame.image.load(path.join(img_dir_enemy, bumper_blue_file))
    bumper_anim['blue'].append(img)
    img = pygame.image.load(path.join(img_dir_enemy, bumper_red_file))
    bumper_anim['red'].append(img)
    img = pygame.image.load(path.join(img_dir_enemy, bumper_green_file))
    bumper_anim['green'].append(img)

# Importation des éléments sonores
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, "shoot_player.wav"))
shoot_sound.set_volume(0.1)

# Importation des éléments graphiques
background = pygame.image.load(path.join(img_dir_effect, "background.png"))
background_rect = background.get_rect()


all_sprites = pygame.sprite.Group()
player_projectiles = pygame.sprite.Group()
bumpers = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player_flames = pygame.sprite.Group()

player = Player(screen, all_sprites, player_projectiles, player_flames, shoot_sound)


# Variable de jeu
running = True
game_over = False
game_pause = False
game = Game()
background_x = 0
bumper_loop = 0


while running:
    dt = clock.tick(FPS)
    if not game_over:
        all_sprites.add(player)

    # Création des ennemies
    if len(enemies) == 0:
        min_enemy = player.power * 2
        max_enemy = player.power * 5
        nb = random.randrange(min_enemy, max_enemy)
        game.spawn_enemy(nb, enemies_img, player, all_sprites, enemies, WIDTH, HEIGHT)

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
            if event.key == pygame.K_p:
                game.spawn_bumper(all_sprites, bumpers, bumper_anim)

    # Boucle pour créer les Bumpers
    bumper_loop += dt
    if bumper_loop >= 24000:
        game.spawn_bumper(all_sprites, bumpers, bumper_anim)
        bumper_loop = 0

    # Mise à jour des sprites
    all_sprites.update()
    player.update()

    # Scrolling du background
    background_x -= 2
    background_rel_x = background_x % background_rect.width

    # Draw / Render
    screen.blit(background, (background_rel_x - background_rect.width, 0))
    screen.blit(background, (background_rel_x, 0))
    all_sprites.draw(screen)
    player.update_bar(screen)
    player.create_flame(all_sprites)
    game.draw_text(f"Score : {player.score}", 20, 10, 10, screen)

    pygame.display.flip()

pygame.quit()
