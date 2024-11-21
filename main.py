import sys
import pygame
from settings import Settings
from user import User

class TechFighters:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.user = User(self)
        pygame.display.set_caption("Tech Fighters")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        self.user.blitme()
        pygame.display.flip()
    
        

if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = TechFighters()
    game.run_game()