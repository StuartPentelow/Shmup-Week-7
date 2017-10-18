import pygame

YELLOW = (0, 150, 150)

class Bullet(pygame.sprite.Sprite):
    #This class represents a bullet fired, derives from Sprite class in pygame
        def __init__(self, color, width, height, posX, posY, direct):
            #call parent class constructer
            super(Bullet,self).__init__()

            self.image = pygame.Surface([width, height])
            self.image.fill(YELLOW)
            self.image.set_colorkey(YELLOW)


            pygame.draw.rect(self.image, color, [posX, posY, width, height])

            self.rect = self.image.get_rect()
