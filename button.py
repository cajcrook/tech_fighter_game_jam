import pygame

class Button:
    def __init__(self, game, msg):
        """Initialize button attributes."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        # Button dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = (192, 192, 192)  # Light gray, like Nintendo's buttons
        self.text_color = (0, 0, 0)  # Black text
        self.border_color = (128, 128, 128)  # Slightly darker gray for the border
        self.font = pygame.font.SysFont(None, 48)


        # Create button rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare the button message
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center it on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw(self):
        """Draw blank button and then the message."""
        # Draw rounded rectangle for Nintendo style
        pygame.draw.rect(self.screen, self.border_color, self.rect, border_radius=10)
        pygame.draw.rect(self.screen, self.button_color, self.rect.inflate(-4, -4), border_radius=10)

        # Draw text
        self.screen.blit(self.msg_image, self.msg_image_rect)
