import sys

import pygame

class AlienInvasion:
    """Main config game class"""
    def __init__(self):
        """Init game"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        """Main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()