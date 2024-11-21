import sys
import pygame


class TechFighters:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((520, 900))
        self.clock = pygame.time.Clock()
        self.bg_colour = (135, 206, 235)
        pygame.display.set_caption("Tech Fighters")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        # Make the most recently drawn screen visible.
            self.screen.fill(self.bg_colour)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = TechFighters()
    ai.run_game()
