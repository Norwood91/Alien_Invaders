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
            self._update_aliens()
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

    def _update_aliens(self):
        # Update the positions of all aliens in the fleet
        # The update() method calls each alien's update() method
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # The available space for aliens is the screen width - the width of two alien ships
        available_xaxis_space = self.settings.screen_width - (2 * alien_width)
        # To set spacing between the alien ships, we divide the available screen space by the width of two alien ships
        # It's the width of two alien ships because the space between each alien is the width of one alien ship
        number_of_aliens_on_xaxis = available_xaxis_space // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        # This calculation is wrapped in parentheses so the outcome can be split over two lines, which results in lines
        # of 79 characters or less
        available_yaxis_space = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_of_rows = available_yaxis_space // (2 * alien_height)

        # This outer loop counts from 0 to the number of rows we want. Python uses the code for making a single row
        # and repeats it number_rows times.
        for row_number in range(number_of_rows):
            # This inner loop creates the aliens in one row
            for alien_number in range(number_of_aliens_on_xaxis):
                # Now when we call create_alien, we include the row_number argument so each row can be placed farther
                # down the screen.
                self._create_alien(alien_number, row_number)



    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        # rect.SIZE contains a tuple with the width and height of a rect object
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        # Changes an alien's ycoord value when it's not in the first row by starting with one alien's height to create
        # empty space at the top of the screen. Each row starts TWO alien heights below the previous row.
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            # If alien is at either the right or left edge of the screen
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


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
