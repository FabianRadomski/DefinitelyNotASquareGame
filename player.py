import pygame
from pygame.math import Vector2


class Player(object):

    def __init__(self, game):
        self.game = game
        size = self.game.screen.get_size()

        self.position = Vector2(size[0]/2, size[1]/2)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

    def add_force(self, force):
        self.acceleration += force

    def tick(self):
        # input
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w]:
            self.add_force(Vector2(0, -1))

        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, 1))

        if pressed[pygame.K_d]:
            self.add_force(Vector2(1, 0))

        if pressed[pygame.K_a]:
            self.add_force(Vector2(-1, 0))

        # physics

        # simulates drag
        self.velocity *= 0.9
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def draw(self):
        rect = pygame.Rect(self.position.x, self.position.y, 70, 70)
        pygame.draw.rect(self.game.screen, (25, 25, 255), rect)
