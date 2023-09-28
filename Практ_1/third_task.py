from first_task import transform_point
import pygame as pg
import sys

print('Введите координаты точки: ')
coordinate_x = int(input('Введите x: '))
coordinate_y = int(input('Введите y: '))

WHITE = (255, 255, 255)
LAVANDER = (243, 134, 236)
DARKCYAN = (0, 139, 139)
SANDY = (244, 164, 96)

def new_points(x, y):
    coordinates = transform_point(coordinate_x, coordinate_y)
    return coordinates

def circles(x, y, new_x, new_y):
    pg.init()

    sc = pg.display.set_mode((600, 600))

    pg.display.update()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        
            sc.fill(WHITE)

            # Введеные координаты
            pg.draw.circle(sc, LAVANDER, (x, y), 5)
            font = pg.font.Font(None, 30)
            text = font.render(f"x={x}, y={y}", True, DARKCYAN)
            sc.blit(text, (x+10, y))

            # Новые координаты
            pg.draw.circle(sc, SANDY, (new_x, new_y), 5)
            font = pg.font.Font(None, 30)
            text = font.render(f"new_x={new_x}, new_y={new_y}", True, DARKCYAN)
            sc.blit(text, (new_x+10, new_y))
        
            pg.display.flip()
    pg.quit()
    sys.exit()


coordinates = new_points(coordinate_x, coordinate_y)
circles(coordinate_x, coordinate_y, coordinates[0], coordinates[1])