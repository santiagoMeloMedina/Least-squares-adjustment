
from sucesion import Sucesion
import numpy as np
import scipy.linalg

class NormalEquations(Sucesion):
    def __init__(self, t, y, level):
        self.A = None
        self.b = None
        self.x = None
        self.t = t
        self.y = y
        self.n = level
        self.assignValues()

    def assignValues(self):
        self.b = np.array(self.y)
        A = []
        for a in self.t:
            tmp = [a**p for p in range(self.n)]
            A.append(tmp)
        self.A = np.array(A)
        return
    
    def descomposition(self, A):
        L = scipy.linalg.cholesky(A, lower=True)
        LT = L.transpose()
        return L, LT
    
    def solution(self):
        ATA = np.dot(np.transpose(self.A), self.A)
        ATb = np.dot(np.transpose(self.A), self.b)
        L, LT = self.descomposition(ATA)
        y = self.sucesiveFront(L, ATb)
        x = self.sucesiveBack(LT, y)
        return x

        
    
    

    
ec = EcuacionNormal([-1.0, -0.5, 0.0, 0.5, 1.0], [1, 0.5, 0, 0.5, 2], 3)
print(["{:.3f}".format(xi) for xi in ec.solution()])

        