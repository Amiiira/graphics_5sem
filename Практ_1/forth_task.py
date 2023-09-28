import numpy as np
import pygame as pg
import sys


matrix = np.array([[1, 3], [4, 1]])

WHITE = (255, 255, 255)
LAVANDER = (243, 134, 236)
DARKCYAN = (0, 139, 139)
SANDY = (244, 164, 96)

def transformation(x, y, x2, y2):
    points_matrix = np.array([[x, y], [x2, y2]])
    new_points_matrix = np.dot(points_matrix, matrix)
    return new_points_matrix

def circles(x, y, x2, y2, new_x, new_y, new_x2, new_y2):
    pg.init()

    sc = pg.display.set_mode((800, 800))

    pg.display.update()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        
            sc.fill(WHITE)

            # Введеные координаты
            pg.draw.line(sc, LAVANDER, [x, y],[x2, y2], 5)
            font = pg.font.Font(None, 30)
            text = font.render(f"a=({x},{y}), b=({x2},{y2})", True, DARKCYAN)
            sc.blit(text, (x+10, y))

            # Новые координаты
            pg.draw.line(sc, SANDY, [new_x, new_y],[new_x2, new_y2], 5)
            font = pg.font.Font(None, 30)
            text = font.render(f"c=({new_x},{new_y}), d=({new_x2},{new_y2})", True, DARKCYAN)
            sc.blit(text, (new_x+10, new_y))
        
            pg.display.flip()
    pg.quit()
    sys.exit()

print('Введите координаты первой точки: ')
x = int(input('Введите x: '))
y = int(input('Введите y: '))
print('Введите координаты второй точки: ')
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
new_ones = transformation(x, y, x2, y2)
circles(x, y, x2, y2,
        new_ones[0][0], new_ones[0][1], 
        new_ones[1][0], new_ones[1][1])