import pygame


# definir la classe projectile joueur
class Projectile2(pygame.sprite.Sprite):

    # definir le constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 8
        self.player = player
        self.image = pygame.image.load('assets/axe_right.png')
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x - 10
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate2(self):
        # tourner le projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove2(self):
        self.player.all_projectiles2.remove(self)
        self.player.currentProj -= 1

    def move2(self):
            self.rect.x -= self.velocity
            self.rotate2()

            # verifier si le projectile entre en collision avec un monstre
            for monster2 in self.player.game.check_collision(self, self.player.game.all_monsters2):
                # supprimer le projectile
                self.remove2()
                #infliger des degats
                monster2.damage2(self.player.attack)

            # verifier si notre projectille n'est plus présent sur l'ecrant
            if self.rect.x < 0:
                self.remove()
