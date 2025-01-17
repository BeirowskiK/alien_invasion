import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Alien ship"""
    def __init__(self, ai_game):
        """Init new alien with start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_borders(self):
        """Return True if alien is next to the edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right - 30) or (self.rect.left <= 0)

    def update(self):
        """Updating alien position"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x