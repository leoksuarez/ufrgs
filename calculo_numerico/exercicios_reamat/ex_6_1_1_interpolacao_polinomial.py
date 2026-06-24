import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyval

xi = np.array([-2, 0, 1, 2], dtype='double')
yi = np.array([-47, -3, 4, 41], dtype='double')

n = len(xi)
potencias = np.arange(0, n, 1)
A = np.array([xi**p for p in potencias]).transpose()

A = np.array()