import pygame

class Ship:
    # Class to manage the user's ship
    def __init__(self, ai_game):
        # Initialize the ship and set its starting position
        # RECT MEANS RECTANGLE
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() # Places ship in current location on screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/goku.bmp') # Returns a surface representing the ship
        self.rect = self.image.get_rect()

        # Draws and starts each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)