import numpy as np
import pygame
import sys

WHITE = (255, 255, 255)
LAVANDER = (243, 134, 236)
DARKCYAN = (0, 139, 139)

L = np.array([[-1/2, 3/2], [3, -2], [-1, -1], [3, 5/3]])
L = L*100

T = np.array([[1,2],[3,1]])

L_conv = L @ T

pygame.init()

screen = pygame.display.set_mode((1280, 720))
screen.fill(WHITE)

pygame.draw.line(screen, LAVANDER, (L[0, 0] + 200, L[0, 1] + 200), (L[1, 0] + 200, L[1, 1] + 200), 6)
pygame.draw.line(screen, LAVANDER, (L[2, 0] + 200, L[2, 1] + 200), (L[3, 0] + 200, L[3, 1] + 200), 6)

pygame.draw.line(screen, DARKCYAN, (L_conv[0, 0] + 200, L_conv[0, 1] + 200), (L_conv[1, 0] + 200, L_conv[1, 1] + 200), 6)
pygame.draw.line(screen, DARKCYAN, (L_conv[2, 0] + 200, L_conv[2, 1] + 200), (L_conv[3, 0] + 200, L_conv[3, 1] + 200), 6)


FPS = 30
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)
    pygame.display.update()