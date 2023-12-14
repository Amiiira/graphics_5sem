import numpy as np
import pygame
import sys

WHITE = (255, 255, 255)
LAVANDER = (243, 134, 236)
DARKCYAN = (0, 139, 139)
BLACK = (0, 0, 0)

L = np.array([[3, -1], [4, 1], [2, 1]])
L = L*100

T = np.array([[0, 1],[-1, 0]])

L_conv = L @ T

pygame.init()

screen = pygame.display.set_mode((1280, 720))
screen.fill(WHITE)

pygame.draw.circle(screen, BLACK, (0, 0), 15)

pygame.draw.polygon(screen, LAVANDER, [(L[0, 0] + 200, L[0, 1] + 200), (L[1, 0] + 200, L[1, 1] + 200), (L[2, 0] + 200, L[2, 1] + 200)], 5)

pygame.draw.polygon(screen, DARKCYAN, [(L_conv[0, 0] + 200, L_conv[0, 1] + 200), (L_conv[1, 0] + 200, L_conv[1, 1] + 200), (L_conv[2, 0] + 200, L_conv[2, 1] + 200)], 5)

FPS = 30
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)
    pygame.display.update()