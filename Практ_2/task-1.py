import pygame as pg
import numpy as np
import sys

pg.init()

sc = pg.display.set_mode((1000, 1000))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LAVANDER = (243, 134, 236)
BLUE = (134, 148, 243)
PINK = (255, 20, 147)
DARKCYAN = (0, 139, 139)

matrix = np.array([[0,100],[200,300]], dtype=float)
T = np.array([[1,2],[3,1]],dtype=float)

t_matrix = matrix@T
mid_point = np.mean(matrix, axis=0)
mid_transformed = np.mean(t_matrix, axis=0)

pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
    sc.fill(WHITE)

    # Отрезок L
    pg.draw.line(sc, LAVANDER, (matrix[0][0],matrix[0][1]),(matrix[1][0],matrix[1][1]), 4)
    
    # Новый отрезок L
    pg.draw.line(sc, BLUE, (t_matrix[0][0],t_matrix[0][1]),(t_matrix[1][0],t_matrix[1][1]), 4)

    # Середина М
    pg.draw.circle(sc, DARKCYAN, (mid_point[0],mid_point[1]), 5)

    # Новая середина М
    pg.draw.circle(sc, PINK, (mid_transformed[0],mid_transformed[1]), 5)

    
    pg.display.flip()

pg.quit()
sys.exit()