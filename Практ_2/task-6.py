import numpy as np
import pygame
import sys

WHITE = (255, 255, 255)
LAVANDER = (243, 134, 236)
DARKCYAN = (0, 139, 139)

L = np.array([[5, 1], [5, 2], [3, 2]])
L = L*100

T = np.array([[2, 0],[0, 2]])

L_conv = L @ T

pygame.init()

screen = pygame.display.set_mode((1280, 720))
screen.fill(WHITE)

pygame.draw.polygon(screen, LAVANDER, [(L[0, 0], L[0, 1]), (L[1, 0], L[1, 1]), (L[2, 0], L[2, 1])], 5)

pygame.draw.polygon(screen, DARKCYAN, [(L_conv[0, 0], L_conv[0, 1]), (L_conv[1, 0], L_conv[1, 1]), (L_conv[2, 0], L_conv[2, 1])], 5)

FPS = 30
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)
    pygame.display.update()