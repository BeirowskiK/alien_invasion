class GameStats:
    """Store game statistics"""
    def __init__(self, ai_game):
        """Init stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Init game statistics, will change during game"""
        self.ships_left = self.settings.ship_limit