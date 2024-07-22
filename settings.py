class Settings:
    """Stored all game settings"""
    def __init__(self):
        """Init game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.player_ship_speed = 1.5

        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.alien_speed = 1.0
        self.alien_drop_speed = 10
        # 1 = move right; -1 = move left
        self.fleet_direction = 1