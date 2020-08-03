import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
box = pygame.Rect(10, 10, 70, 70)


while True:
    # checks if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    # check input
    # keys is a dictionary of booleans
    keys = pygame.key.get_pressed()
    if keys [pygame.K_d]:
        box.x += 1
    if keys[pygame.K_a]:
        box.x -= 1
    if keys[pygame.K_w]:
        box.y -= 1
    if keys[pygame.K_s]:
        box.y += 1

    # draws a rectangle
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (25, 25, 255), box)
    pygame.display.flip()
