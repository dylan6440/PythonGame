import pygame
from projectile import *
from projectile_2 import *


# cree notre classe player
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        self.game = game
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.all_projectiles2 = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 585
        self.defaultScore = 0
        self.score = 0
        self.maxProj = 100
        self.currentProj = 0

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'as plus de point de vie
            self.game.game_over()

    def heal(self, amount):
        if self.health + amount < self.max_health:
            self.health += amount

    def updateScore(self, a):
        self.score += a

    def initScore(self):
        self.score = self.defaultScore

    def damageUp(self, amount):
        self.attack += amount

    def update_health_bar(self, surface):
        # definir la couleur / emplacement / dessiner la bar
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 95, self.rect.y - 5, self.max_health, 9])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 95, self.rect.y - 5, self.health, 9])

    def launch_projectile(self):
        # creer une nouvelle instance de classe projectile
        if self.currentProj < self.maxProj:
            self.all_projectiles.add(Projectile(self))
            self.currentProj += 1

    def launch_projectile2(self):
        if self.currentProj < self.maxProj:
            self.all_projectiles2.add(Projectile2(self))
            self.currentProj += 1

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        if not self.game.check_collision(self, self.game.all_monsters2):
            self.rect.x -= self.velocity

