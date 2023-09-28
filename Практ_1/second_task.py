import pygame as pg
import sys

pg.init()

sc = pg.display.set_mode((600, 600))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LAVANDER = (243, 134, 236)
BLUE = (134, 148, 243)
PINK = (255, 20, 147)
DARKCYAN = (0, 139, 139)




pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
    sc.fill(WHITE)

    # Окружность
    pg.draw.circle(sc, LAVANDER, (100, 100), 50)
    
    # Линия
    pg.draw.line(sc, BLUE, (200, 200), (300, 350), 6)

    # Контур прямоугольника
    pg.draw.rect(sc, DARKCYAN,(440, 440, 100, 100))

    # Tекст
    font = pg.font.Font(None, 36)
    text = font.render("Эта библиотека прекрасна!", True, PINK)
    sc.blit(text, (100, 400))

    
    pg.display.flip()

pg.quit()
sys.exit()