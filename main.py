import pygame
import sys


class Alien_invader:
    def __init__(self):
        # Initializes the background settings that pygame needs to work properly.
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invaders')
        # Set background color of the screen
        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            # Watch for keyboard and mouse events.
            # Pygame.event.get() returns a list of events that have taken place since the last time the function was
            # called.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through of the loop
            self.screen.fill(self.bg_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Alien_invader()
    ai.run_game()
