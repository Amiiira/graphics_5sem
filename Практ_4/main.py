import pygame as pg
import sys
import numpy as np
import math as m
import graphics as g
import transform as t
from pygame.locals import *

rf = g.ReferenceFrame(g.Origin(20, 580), g.Unit(65), g.Unit(65))
d = g.Drawer(800, 600, 32, rf)
d.initialize("Square Funnel")
d.color = g.DARKCYAN #ИЗМЕНИТЬ
d.draw_axes(-0.2, 11.0, -0.2, 8.5)
d.color = g.BLACK #ИЗМЕНИТЬ

L = np.matrix([
    [2.0, 0.5, 1],
    [8.0, 0.5, 1],
    [8.0, 6.5, 1],
    [2.0, 6.5, 1]
])
xc = (2.0 + 8.0) / 2
yc = (0.5 + 6.5) / 2
d.draw_polygon(L, 2)

d.color = g.LAVANDER 
d.draw_filled_circle(xc, yc, 0.1)
angle = m.pi / 64
scale = 0.95
L_last = np.zeros((3,3))
L_last = L
for k in range(0, 50):
    L_last = L_last * t.translate(-xc, -yc) * t.scale(scale, scale) * t.rotate(angle) * t.translate(xc, yc)
    d.draw_polygon(L_last, 1)

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
        
