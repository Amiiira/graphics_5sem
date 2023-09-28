import numpy as np

def transform_point(x, y):
    matrix = np.array([[1, 3], [4, 1]])
    new_x = matrix[0, 0] * x + matrix[0, 1] * y
    new_y = matrix[1, 0] * x + matrix[1, 1] * y
    return new_x, new_y 

if '__name__' == '__main__':
    print('Введите координаты точки: ')
    coordinate_x = int(input('Введите x: '))
    coordinate_y = int(input('Введите y: '))
    print(transform_point(coordinate_x, coordinate_y))

