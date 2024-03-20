import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PLAYER_FILE_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = SC_WIDTH//2
        self.rect.bottom = SC_HEIGHT-20

        self.speedx = 1
        self.speedy = 1

    def update(self):
        self.speedy = 0
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speedx = -8
        if keys[pygame.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx


        if keys[pygame.K_s]:
            self.speedy = 8
        if keys[pygame.K_w]:
            self.speedy = -8
        self.rect.y += self.speedy
        
        if self.rect.right > SC_WIDTH:
            self.rect.right = SC_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top > SC_HEIGHT - 100:
            self.rect.top = SC_HEIGHT - 100
            
        if self.rect.bottom < 100:
            self.rect.bottom = 100
            

            
    def draw(self, screen):
        screen.blit(self.image, self.rect)


     

