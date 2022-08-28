
class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.ships_remaining = self.settings.ship_limit

    def reset_stats(self):
        self.ships_remaining = self.settings.ship_limit