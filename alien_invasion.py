import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Main config game class"""
    def __init__(self):
        """Init game"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.player_ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def _check_events(self):
        """Reaction for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player_ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.player_ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player_ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.player_ship.moving_left = False

    def _update_screen(self):
        """Updateing screen"""
        self.screen.fill(self.settings.bg_color)
        self.player_ship.blitme()
        pygame.display.flip()

    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            self.player_ship.update()
            self._update_screen()
            self.clock.tick(60)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()