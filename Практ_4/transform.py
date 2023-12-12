import numpy as np
import math as m

def rotate(angle: float):
    cs = m.cos(angle)
    sn = m.sin(angle)
    return np.matrix([
        [ cs, sn, 0],
        [-sn, cs, 0],
        [ 0, 0, 1]
    ])

def translate(Dx: float, Dy: float):
    return np.matrix([
        [1, 0, 0],
        [0, 1, 0],
        [Dx, Dy, 1]
    ])

def scale(Sx: float, Sy: float):
    return np.matrix([
        [Sx, 0, 0],
        [0, Sy, 0],
        [0, 0, 1]
    ])