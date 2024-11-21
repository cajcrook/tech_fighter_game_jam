import pygame
from random import randint
from pygame.sprite import Sprite

class Obstacle(Sprite):

    def __init__(self, game):

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        # self.colour = self.settings.obstacle_colour
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('assets/java.png')

        self.rect = self.image.get_rect()  
        self.rect.midtop = (randint(0,560), 900)
        self.y = float(self.rect.y)

    def update(self): 
        self.y -= self.settings.obstacle_speed
        self.rect.y = self.y

    def draw_obstacle(self):
        self.screen.blit(self.image, self.rect)



        

