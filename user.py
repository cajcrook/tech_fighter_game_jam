import pygame
from settings import Settings

class User:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        
        self.image = pygame.image.load('assets/parachute_man.png')
        self.image_flipped = pygame.transform.flip(self.image, True, False)
        
        self.rect = self.image.get_rect()  
        self.rect.midtop = self.screen_rect.midtop
        self.rect.y = 780
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        
        self.facing_right = True
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.user_speed + (self.y/40)
            self.x += self.settings.user_speed
            
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.user_speed + (self.y/40)
            self.x -= self.settings.user_speed

    def blitme(self):
        if self.facing_right:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.image_flipped, self.rect)
        