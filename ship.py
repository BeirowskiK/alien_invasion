import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Manage spaceship"""
    def __init__(self, ai_game):
        super().__init__()
        """Init ship"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/player_ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updateing ship position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Show ship in actual position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center ship by bottom border"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)