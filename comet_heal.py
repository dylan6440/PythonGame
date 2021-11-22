import  pygame
import random

# créer une classe pour gere cette comete
class comet_heal(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #definir l'image associée
        self.image = pygame.image.load('assets/comet_1.png')
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 5)
        self.rect.x = random.randint(20, 1580)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # verifier le nombre de comet
        if len(self.comet_event.all_comets) == 0:
            print("l'event est fini")
            # remetre la bar a 0
            self.comet_event.reset_percent()
            # apparaitre a nouveaux les monstre
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster2()
            self.comet_event.game.spawn_monster2()
            self.comet_event.game.spawn_monster2()
            self.comet_event.game.spawn_monster2()



    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 800:
            self.remove()

            # si il n'y as plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                print("L'évenement est fini")
                # remetre la jauge de vie au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False


        # verifer si la boule touche le player
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_player):
            print('joueur touché!')
            # retirer la comet
            self.remove()
            #subir point de degats
            self.comet_event.game.player.heal(25)
            self.comet_event.game.player.damageUp(5)
