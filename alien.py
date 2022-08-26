import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()


        # Start alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        # Move the alien to the right or left
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        # Return True if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True