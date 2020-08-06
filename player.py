import pygame
from pygame.math import Vector2


class Player(object):

    def __init__(self, game):
        self.game = game
        size = self.game.screen.get_size()

        self.position = Vector2(size[0]/2, size[1]/2)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

        self.left_key = pygame.K_LEFT
        self.right_key = pygame.K_RIGHT
        self.up_key = pygame.K_UP
        self.down_key = pygame.K_DOWN

        self.color = (255,0,0)

    def add_force(self, force):
        self.acceleration += force

    def tick(self):
        # input
        pressed = pygame.key.get_pressed()

        if pressed[self.up_key]:
            self.add_force(Vector2(0, -1))

        if pressed[self.down_key]:
            self.add_force(Vector2(0, 1))

        if pressed[self.right_key]:
            self.add_force(Vector2(1, 0))

        if pressed[self.left_key]:
            self.add_force(Vector2(-1, 0))

        # physics

        # simulates drag
        self.velocity *= 0.9
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def draw(self):
        rect = pygame.Rect(self.position.x, self.position.y, 70, 70)
        pygame.draw.rect(self.game.screen, self.color, rect)
