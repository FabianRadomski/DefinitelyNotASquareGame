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
        self.game_objects = []
        self.player = Player(self)
        self.game_objects.append(self.player)

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
        for game_object in self.game_objects:
            game_object.tick() 

    def draw(self):
        for game_object in self.game_objects:
            game_object.draw()


if __name__ == "__main__":
    Game()
