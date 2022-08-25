import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            # This will update the ship's position after we've checked for keyboard events and before we update screen
            self.ship.update()
            self._update_bullets()
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
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
        # Create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # Update bullets and get rid of old bullets
        # Update bullet positions
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        # Update images on the screen, and flip to the new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # bullets.sprites() returns a list of all sprites in the group 'bullets'
        # To draw all fired bullets to the screen, we loop through the sprites in 'bullets' and call draw_bullet()
        # On each one
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # The draw method requires one argument: a surface (self.screen) on which to draw the element to
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvader()
    ai.run_game()
