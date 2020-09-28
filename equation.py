
from leastSquare import LeastSquare
import numpy as np
import scipy.linalg

class NormalEquation(LeastSquare):
    
    def descomposition(self, A):
        L = scipy.linalg.cholesky(A, lower=True)
        LT = L.transpose()
        return L, LT
    
    def solution(self):
        ATA = np.dot(np.transpose(self.A), self.A)
        ATb = np.dot(np.transpose(self.A), self.b)
        L, LT = self.descomposition(ATA)
        y = self.sucesiveFront(L, ATb, len(L))
        x = self.sucesiveBack(LT, y, len(LT))
        return x
        

        