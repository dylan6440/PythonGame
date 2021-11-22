import pygame
import random
import player

# crée classe monster
class Monster2(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.image = pygame.image.load('assets/pangolin_left.png')
        self.image = pygame.transform.scale(self.image, (175, 175))
        self.rect = self.image.get_rect()
        self.rect.x = 0 - random.randint(0, 300)
        self.rect.y = 715
        self.velocity = random.randint(1, 3)
        self.player = player

    def damage2(self, amount):
        # infliger les degats
        self.health -= amount

        # verifier si son nb de vie <= 0
        if self.health <= 0:
            # réapparaitre comme new monster
            self.rect.x = 0 - random.randint(0, 300)
            self.velocity = random.randint(1, 4)
            self.health = self.max_health
            # #ajout d'un score
            # self.player.Player.updateScore(a=100)

            #si la barre d'event est chargé a son max
            if self.game.comet_event.is_full_loaded():
                # retire le monstre du jeux
                self.game.all_monsters2.remove(self)

    def update_health_bar2(self, surface):
        # definir la couleur / emplacement / dessiner la bar
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 30, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 30, self.rect.y - 20, self.health, 5])

    def forward2(self):
        # le deplacement ce fais que si il y as pas de player en collision
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x += self.velocity
        # si il es en colission mettre des damage
        else:
            self.game.player.damage(self.attack)
