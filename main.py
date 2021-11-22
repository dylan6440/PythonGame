import pygame
from game import *
import math
pygame.init()


# generer la fenetre du jeu
pygame.display.set_caption("Covid-19 Game")
screen = pygame.display.set_mode((1600, 960))

# importer l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.png')
background = pygame.transform.scale(background, (1600, 1000))

# impoter notre banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (650, 650))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.3)

# charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (500, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.8)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#charger le jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan
    screen.blit(background, (0, 0))

    # verifier si notre jeu a commencé
    if game.is_playing:
        # declencher les instruction de la partie
        game.update(screen)
    # verifier si notre jeu n'as pas commencé
    else:
        # ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'event est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si un joueur actionne une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # detecter si la touche fleche de droite est enclenchée pour lancer notre projectile
            if event.key == pygame.K_RIGHT:
                game.player.launch_projectile()
            elif event.key == pygame.K_LEFT:
                game.player.launch_projectile2()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification si la souris click sur le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()

