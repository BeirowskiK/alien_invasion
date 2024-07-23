import json
from pathlib import Path

class GameStats:
    """Store game statistics"""
    def __init__(self, ai_game):
        """Init stats"""
        self.settings = ai_game.settings

        self.load_high_score()
        self.reset_stats()

    def reset_stats(self):
        """Init game statistics, will change during game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_stats_in_file(self):
        score_file = Path('high_score.txt')
        score_file.write_text(str(self.high_score))


    def load_high_score(self):
        try:
            score_file = Path('high_score.txt')
            score = int(score_file.read_text())
            self.high_score = score
        except FileNotFoundError:
            self.high_score = 0
