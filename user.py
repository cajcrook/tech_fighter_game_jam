import pygame
from settings import Settings

class User:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        
        self.image = pygame.image.load('assets/parachute_man.png')
        self.rect = self.image.get_rect()  
        self.rect.midtop = self.screen_rect.midtop
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.user_speed
            self.x += self.settings.user_speed
            
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.user_speed
            self.x -= self.settings.user_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        