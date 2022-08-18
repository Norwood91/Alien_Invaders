import pygame

class Ship:
    # Class to manage the user's ship
    def __init__(self, ai_game):
        # Initialize the ship and set its starting position
        # RECT MEANS RECTANGLE
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() # Places ship in current location on screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp') # Returns a surface representing the ship
        self.rect = self.image.get_rect()

        # Draws and starts each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False

    def update(self):
        # Update the ships position based on the movement flag
        # Move the ship to the right by increasing the ship's rect.x value by 1 pixel
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)