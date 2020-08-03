import pygame
import sys

screen = pygame.display.set_mode((1280, 720))

while True:
    # checks if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    # draws a rectangle
    pygame.draw.rect(screen, (25, 25, 255), pygame.Rect(10, 50, 200, 100))
    pygame.display.flip()
