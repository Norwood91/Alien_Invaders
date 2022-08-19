import pygame

class Ship:
    # Class to manage the user's ship
    def __init__(self, ai_game):
        # Initialize the ship and set its starting position
        # RECT MEANS RECTANGLE
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp') # Returns a surface representing the ship
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update the ships x value
        # self.rect.right returns the x-coord of the right edge of the ship's rectangle. If that value returned is less
        # than the value returned by self.screen_rect.right, the ship hasn't reached the right edge of the screen.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # We used two if statements instead of an if/elif so that the right arrow key doesn't have priority
        # This makes the movements more accurate when switching from right to left
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rectangle object from self.x
        self.rect.x = self.x

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)