import pygame


class User:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        self.image = pygame.image.load('assets/parachute_man.png')
        self.rect = self.image.get_rect()
        
        self.rect.midtop = self.screen_rect.midtop
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        