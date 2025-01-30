import pygame
from random import randint
from pygame.sprite import Sprite

class Life(Sprite):

    def __init__(self, game):

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        # self.colour = self.settings.life_colour
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.transform.scale(pygame.image.load('assets/plastic.png'), (50, 50))

        self.rect = self.image.get_rect()  
        self.rect.midtop = (randint(0,560), 900)
        self.y = float(self.rect.y)

    def update(self): 
        self.y -= self.settings.life_speed
        self.rect.y = self.y

    def draw_life(self):
        # pygame.draw.rect(self.screen, self.image, self.rect)
        self.screen.blit(self.image, self.rect)



        

