import pygame
import pygame.gfxdraw

from numpy import matrix

class Origin:
    def __init__(self, x0: int, y0: int):
        self.__x0 = x0
        self.__y0 = y0

    @property
    def x0(self):
        return self.__x0
    
    @property
    def y0(self):
        return self.__y0
    
class Unit:
    def __init__(self, pixels:int):
        self.__pixels = pixels

    @property
    def pixels(self):
        return self.__pixels
    
class ReferenceFrame:
    def __init__(self, origin: Origin, ux: Unit, uy: Unit):
        self.__origin = origin
        self.__unit_x = ux
        self.__unit_y = uy

    @property
    def origin(self):
        return self.__origin
    
    @property
    def unit_x(self):
        return self.__unit_x
    
    @property
    def unit_y(self):
        return self.__unit_y


def get_x(rf: ReferenceFrame, x: float):
    scale_x = rf.unit_x.pixels
    x0 = rf.origin.x0
    return int(scale_x * x + x0)

def get_y(rf: ReferenceFrame, y: float):
    scale_y = rf.unit_y.pixels
    y0 = rf.origin.y0
    return int(-scale_y * y + y0)

def get_length(unit: Unit, dl: float):
    scale = unit.pixels
    return int(scale * dl)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LAVANDER = (243, 134, 236)
DARKCYAN = (0, 158, 151)
BLUE = (16, 5, 118)

class Drawer:
    def __init__(self, res_x: int, res_y: int, color_depth: int, rf: ReferenceFrame):
        self.rf = rf
        self.__color = BLACK
        self.resolution = (res_x, res_y)
        self.color_depth = color_depth
        self.screen = None
        self.font = None
    def initialize(self, caption: str):
        pygame.init()
        screen = pygame.display.set_mode(self.resolution, 0, self.color_depth)
        pygame.display.set_caption(caption)
        pygame.font.init()
        font = pygame.font.SysFont('Times New Romain', 24)
        self.screen = screen
        self.font = font
        self.screen.fill(WHITE)
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color: tuple):
        self.__color = color

    def draw_line(self, x1: float, y1: float, x2: float, y2: float, width: int):
        ix1 = get_x(self.rf, x1); iy1 = get_y(self.rf, y1)
        ix2 = get_x(self.rf, x2); iy2 = get_y(self.rf, y2)
        pygame.draw.line(self.screen, self.color, (ix1, iy1), (ix2, iy2), width)

    def draw_text(self, x:float, y:float, text: str):
        ix = get_x(self.rf, x)
        iy = get_y(self.rf, y)
        text_surface = self.font.render(text, False, self.color)
        self.screen.blit(text_surface, (ix, iy))

    def draw_polygon(self, points: matrix, width: int):
        n_rows = points.shape[0]
        row_points = []
        for i in range(0, n_rows):
            row_point = (get_x(self.rf, points[i,0]), get_y(self.rf, points[i,1]))
            row_points.append(row_point)
        pygame.draw.polygon(self.screen, self.color, row_points, width)

    def draw_filled_circle(self, x: float, y: float, radius: float):
        pygame.gfxdraw.filled_circle(self.screen, get_x(self.rf, x), get_y(self.rf, y), get_length(self.rf.unit_x, radius), self.color)

    def draw_axes(self, x_min: float, x_max: float, y_min: float, y_max: float):
        self.draw_line(x_min, 0.0, x_max, 0.0, 2)
        self.draw_line(0.0, y_min, 0.0, y_max, 2)
        self.draw_text(-0.17,-0.04, "O")

        