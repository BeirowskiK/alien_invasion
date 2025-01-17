class Settings:
    """Stored all game settings"""
    def __init__(self):
        """Init game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.alien_drop_speed = 10

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings which will change during the game"""
        self.player_ship_speed = 1.5
        self.bullet_speed = 2.5

        self.alien_speed = 1.0
        self.alien_points = 50

        # 1 = move right; -1 = move left
        self.fleet_direction = 1

    def increase_speed(self):
        self.player_ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
