import pygame
import sys
from settings import Settings
from ship import Ship


class AlienInvader:
    def __init__(self):
        # Initializes the background settings that pygame needs to work properly.
        pygame.init()
        self.settings = Settings()
        # pygame.FULLSCREEN tells pygame to figure out a window size that will fill the screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()

    def _check_keyup_events(self, event):
        if event.type == pygame.KEYUP:
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
