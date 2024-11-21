import sys
import pygame
import random
from settings import Settings
from user import User
from obstacle import Obstacle
from life import Life
from button import Button

class TechFighters:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.user = User(self)
        self.obstacles = pygame.sprite.Group()
        self.lives = pygame.sprite.Group()

        pygame.display.set_caption("Tech Fighters")
        
        # Game states
        self.game_active = False  # Track whether the game is running
        self.button = Button(self, "Start")  # Create a start button

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.obstacles.update()
            self.lives.update()

            if self.game_active:
                self.obstacles.update()
                self.user.update()
                self._load_obstacle()
                self._delete_obstacle()
                self._load_life()
                self._delete_life()
                self._collision()
                self.end_game()

            self._update_screen()
            self.clock.tick(60)
            if pygame.sprite.spritecollide(self.user, self.obstacles, True):
                self.user.collision(50)
            if pygame.sprite.spritecollide(self.user, self.lives, True):
                self.user.collision(-50)

    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active:
                if event.key == pygame.K_RIGHT:
                    self.user.moving_right = True
                    self.user.facing_right = True
                elif event.key == pygame.K_LEFT:
                    self.user.moving_left = True
                    self.user.facing_right = False
            elif event.type == pygame.KEYUP and self.game_active:
                if event.key == pygame.K_RIGHT:
                    self.user.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.user.moving_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.button.rect.collidepoint(mouse_pos) and not self.game_active:
                    # Start the game
                    self.game_active = True

    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)

        if self.game_active:
            for obstacle in self.obstacles.sprites():
                obstacle.draw_obstacle()
            for life in self.lives.sprites():
                life.draw_life()
            self.user.blitme()
        else:
            self.button.draw()  # Draw the start button when the game is inactive
        pygame.display.flip()

    def _load_obstacle(self):
        if random.randint(0, 50) == 3:
            new_obstacle = Obstacle(self)
            self.obstacles.add(new_obstacle)

    def _delete_obstacle(self):
        for obstacle in self.obstacles.copy():
            if obstacle.rect.bottom <= 0:
                self.obstacles.remove(obstacle)

#Lives
    def _load_life(self):
        if random.randint(0,200) == 3:
            new_life = Life(self)
            self.lives.add(new_life)

    def _delete_life(self):
        for life in self.lives.copy():
            if life.rect.bottom <= 0:
                self.lives.remove(life)
    
    def _collision(self):
        if pygame.sprite.spritecollide(self.user, self.obstacles, True):
                self.user.collision(50)
    
    def end_game(self):
        if self.user.rect.y >= 800:
            font = pygame.font.Font(None, 74)  # Create a font object (None uses default font)
            game_over_text = font.render("Game Over", True, (255, 0, 0))  # Render the text in red
            text_rect = game_over_text.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2))
            self.screen.blit(game_over_text, text_rect)  # Draw text at the center of the screen
            pygame.display.flip()
            pygame.time.delay(2000)  # Pause for 2 seconds before exiting
            self.game_active = False
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = TechFighters()
    game.run_game()
