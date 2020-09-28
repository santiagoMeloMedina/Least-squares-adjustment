
from sucesion import Sucesion
import numpy as np
import scipy.linalg

class LeastSquare(Sucesion):
    def __init__(self, t, y, n):
        self.A = None
        self.b = None
        self.t = t
        self.y = y
        self.n = n
        self.assignValues()
    
    def assignValues(self):
        self.b = np.array(self.y)
        A = []
        for a in self.t:
            tmp = [a**p for p in range(self.n)]
            A.append(tmp)
        self.A = np.array(A)
        return