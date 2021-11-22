import pygame
from player import *
from monster import *
from monster_2 import *
from comet_event import *

# creer une seconde classe qui va representer notre jeu
class Game:

    def __init__(self):
        # definir si notre jeux a commencer
        self.is_playing = False
        # generer notre joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        #generer l'evenement

        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.all_monsters2 = pygame.sprite.Group()
        self.pressed = {}
        self.level = 1
        self.comet_event = CometFallEvent(self, self.level)

    def start(self):
        self.is_playing = True

        self.spawn_monster()
        self.spawn_monster2()
        self.spawn_monster()
        self.spawn_monster2()
        self.spawn_monster()
        self.spawn_monster2()

    def game_over(self):
        # remettre le jeu a neuf
        self.all_monsters = pygame.sprite.Group()
        self.all_monsters2 = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.player.initScore()
        self.level = 1

    def update(self, screen):
        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d'evenement
        self.comet_event.update_bar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
        for projectile2 in self.player.all_projectiles2:
            projectile2.move2()

        # recuperer les monstre du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        for monster2 in self.all_monsters2:
            monster2.forward2()
            monster2.update_health_bar2(screen)

        # recuperer les comet du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()


        # appliquer l'ensemble des image de groupe projectiles
        self.player.all_projectiles.draw(screen)
        self.player.all_projectiles2.draw(screen)

        # appliquer l'ensemble des images du groupe comet
        self.comet_event.all_comets.draw(screen)

        # appliquer l'ensemble des image du groupe monstre
        self.all_monsters.draw(screen)
        self.all_monsters2.draw(screen)

        # verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def spawn_monster2(self):
        monster2 = Monster2(self)
        self.all_monsters2.add(monster2)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)



