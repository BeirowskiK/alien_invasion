import pygame.font


class Button:
    """Control button class"""
    def __init__(self, ai_game, value):
        """Init button"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width = 200
        self.height = 50
        self.bg_color = (0, 80, 200)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(value)

    def _prep_msg(self, msg):
        """Generate text as image and insert it to the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Display button with message"""
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
