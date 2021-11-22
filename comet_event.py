import pygame
from comet import *
from comet_heal import *
import game


# crée une classe pour gerer cet evenement
class CometFallEvent:
    # lors du chargement, crée un compteur
    def __init__(self, game, level):
        self.percent = 0
        self.percent_speed = 30
        self.game = game
        self.fall_mode = False
        # definir un groupe de sprite pour stocker nos cometes
        self.all_comets = pygame.sprite.Group()
        self.level = level

    def add_percent(self):
        self.percent += self.percent_speed

    def is_full_loaded(self):
        return self.percent >= ((self.level * 10) + 100)

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        lev = self.level
        print("curent level = " + str(self.level))
        if lev <= 11:
            for i in range(1, (10 - lev)):
                self.all_comets.add(comet_heal(self))

        # boucle pour les valeur entre 1 et 10
        for i in range(1, (15 + (2 * lev))):
            # apparraitre une premiere boule de feu
            self.all_comets.add(comet(self))

    def attempt_fall(self):
        # la jauge d'evenement totalement chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0 and len(self.game.all_monsters2) == 0:
            print("Pluie de cometes!")
            self.meteor_fall()
            self.fall_mode = True  # permet d'activer l'evenement

    def update_bar(self, surface):
        # ajouter du pourcentage a la bar
        self.add_percent()

        # barre noir en background
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # axe des x
            surface.get_height() - 20,  # axe des y
            surface.get_width(),  # longueur de la fenetre
            10,  # epaisseur de la barre
        ])
        # barre rouge jauge event
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe des x
            surface.get_height() - 20,  # axe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la fenetre
            10,  # epaisseur de la barre
        ])
