import pygame

class Ship:
    """Manage spaceship"""
    def __init__(self, ai_game):
        """Init ship"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/player_ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Show ship in actual position"""
        self.screen.blit(self.image, self.rect)