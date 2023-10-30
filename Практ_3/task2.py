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

coord_shift_x = WINDOW_SIZE / 2 - 290
coord_shift_y = WINDOW_SIZE / 2

pg.draw.circle(sc, LAVANDER, [coord_shift_x, coord_shift_y], 10)
pg.display.update()

a = 10
b = 10
delta_theta = math.pi /32

theta = 0.0
coordinate_list = list()
N_iterations = 65
for i in range(1, N_iterations + 1):
    r = b + 2 * a * math.cos(theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    coordinate_list.append([x, y])
    theta = theta + delta_theta

coordinates_array = np.array(coordinate_list) * 20 + np.array([coord_shift_x, coord_shift_y])
pg.draw.lines(sc, DARKCYAN, closed=False, points=coordinates_array, width=2)
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
