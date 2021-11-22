import pygame


# definir la classe projectile joueur
class Projectile(pygame.sprite.Sprite):

    # definir le constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 8
        self.player = player
        self.image = pygame.image.load('assets/axe_right.png')
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 190
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le projectile
        self.angle -= 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)
        self.player.currentProj -= 1

    def move(self):
            self.rect.x += self.velocity
            self.rotate()

            # verifier si le projectile entre en collision avec un monstre
            for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
                # supprimer le projectile
                self.remove()
                #infliger des degats
                monster.damage(self.player.attack)

            # verifier si notre projectille n'est plus présent sur l'ecrant
            if self.rect.x > 1600:
                self.remove()
