import pygame
from pygame.sprite import Sprite

class Obstacle(Sprite):

    def __init__(self, game):

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.colour = self.settings.obstacle_colour
        self.screen_rect = game.screen.get_rect()

        self.rect = pygame.Rect(0, 0, self.settings.obstacle_width, self.settings.obstacle_height)
        self.rect.midbottom = self.screen_rect.midbottom
        self.y = float(self.rect.y)

    def update(self): 
        self.y -= self.settings.obstacle_speed
        self.rect.y = self.y

    def draw_obstacle(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)


        
        

