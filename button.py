import pygame.display

start_image = pygame.image.load('assets/parachute_man.png').convert_alpha()

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft(x,y)

def draw(self):
    pygame.draw.rect(self.image, (self.rect.x, self.rect.y))

    
start_button = Button(100,200,start_image) 