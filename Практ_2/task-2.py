import numpy as np
import pygame
import sys

WHITE = (255, 255, 255)
LAVANDER = (243, 134, 236)
DARKCYAN = (0, 139, 139)

L = np.array([[50, 100], [250, 200], [50, 200], [250, 300]])

m1_AB = (L[1, 1] - L[0, 1]) / (L[1, 0] - L[0, 0])
m1_EF = (L[3, 1] - L[2, 1]) / (L[3, 0] - L[2, 0])

T = np.array([[1,2],[3,1]])

L_conv = L @ T

m1_A1B1 = (L_conv[1, 1] - L_conv[0, 1]) / (L_conv[1, 0] - L_conv[0, 0])
m1_E1F1 = (L_conv[3, 1] - L_conv[2, 1]) / (L_conv[3, 0] - L_conv[2, 0])

pygame.init()

screen = pygame.display.set_mode((1280, 720))
screen.fill(WHITE)

pygame.draw.line(screen, LAVANDER, (L[0, 0], L[0, 1]), (L[1, 0], L[1, 1]), 5)
pygame.draw.line(screen, LAVANDER, (L[2, 0], L[2, 1]), (L[3, 0], L[3, 1]), 5)

pygame.draw.line(screen, DARKCYAN, (L_conv[0, 0], L_conv[0, 1]), (L_conv[1, 0], L_conv[1, 1]), 5)
pygame.draw.line(screen, DARKCYAN, (L_conv[2, 0], L_conv[2, 1]), (L_conv[3, 0], L_conv[3, 1]), 5)


FPS = 30
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)
    pygame.display.update()