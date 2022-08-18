import pygame
import sys
from settings import Settings
from ship import Ship


class AlienInvader:
    def __init__(self):
        # Initializes the background settings that pygame needs to work properly.
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invaders')
        # The self argument refers to the current instance of Alien_invader
        # This is the param that gives Ship access to the game's resources, like the screen object
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            # This will update the ship's position after we've checked for keyboard events and before we update screen
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse events.
        # Pygame.event.get() returns a list of events that have taken place since the last time the function was
        # called.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            # If you stop pressing the right arrow button (KEYUP means stop pressing button)
            # We can use an elif block here because each event is connected to only ONE key (left or right)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        # Update images on the screen, and flip to the new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvader()
    ai.run_game()
