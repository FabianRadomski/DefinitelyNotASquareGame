import pygame
import sys
from player import Player


class Game(object):

    def __init__(self):
        # config
        self.tps_max = 100.0

        # initialisation
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player = Player(self)

        while True:
            # checks if user quits
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            # handles ticks
            # delta holds the time in seconds
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()


if __name__ == "__main__":
    Game()
