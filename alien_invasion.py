import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Main config game class"""
    def __init__(self):
        """Init game"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # FULL SCREEN SETTINGS
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.player_ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("Alien Invasion")

    def _check_keydown_events(self, event):
        """Processing keydown event"""
        if event.key == pygame.K_RIGHT:
            self.player_ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player_ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Processing keyup event"""
        if event.key == pygame.K_RIGHT:
            self.player_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player_ship.moving_left = False

    def _check_events(self):
        """Reaction for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_bullets(self):
        """Updating bullets position on screen, deleting invisible bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Updating screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.player_ship.blitme()
        pygame.display.flip()

    def _fire_bullet(self):
        """Create new bullet and append to the group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            self.player_ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()