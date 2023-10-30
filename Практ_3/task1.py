import pygame as pg
import numpy as np
import sys
import math
from pygame.locals import *


WHITE = (255, 255, 255)
LAVANDER = (243, 134, 236)
DARKCYAN = (0, 139, 139)

WINDOW_SIZE = 800
pg.init()
pg.font.init()
sc = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
sc.fill(WHITE)

pg.display.update()

coord_shift = WINDOW_SIZE / 2

pg.draw.circle(sc, LAVANDER, [coord_shift, coord_shift], radius=3)
pg.display.update()

X = np.array([
    [2, 2],
    [-2, 2],
    [-2, -2],
    [2, -2]
]) * 100

X_shifted = X + coord_shift

pg.draw.polygon(sc, LAVANDER, X_shifted, width=3)
pg.display.update()

m_scale = 0.9
M = np.array([
    [m_scale, 0],
    [0, m_scale]
])

alpha = -1 * math.pi /32
V = np.array([
    [math.cos(alpha), -math.sin(alpha)],
    [math.sin(alpha), math.cos(alpha)]
])

T = V @ M
N_iterations = 30
X_i = X.T
for i in range(1, N_iterations + 1):
    X_i_transformed = T @ X_i
    X_i_shifted = X_i_transformed + coord_shift
    pg.draw.polygon(sc, LAVANDER, X_i_shifted.T, width=3)
    X_i = X_i_transformed

pg.display.update()
    
FPS = 30
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    clock.tick(FPS) 
    pg.display.update()





