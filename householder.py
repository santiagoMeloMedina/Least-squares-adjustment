
from leastSquare import LeastSquare
import numpy as np
import scipy.linalg
import math

class HouseHolder(LeastSquare):
    def __init__(self, t, y, n):
        LeastSquare.__init__(self, t, y, n)
        I = [[0.0 for _ in range(len(self.A))] for _ in range(len(self.A))]
        for i in range(len(self.A)):
            I[i][i] = 1
        self.I = np.array(I)

    def vectorIsolation(self, A, col):
        vector, vectorIdentity = [], []
        for n in range(len(A)):
            vector.append(A[n][col])
            vectorIdentity.append(self.I[n][col])
        vector, vectorIdentity = np.array(vector), np.array(vectorIdentity)
        normal = 0
        for c in range(col):
            vector[c] = 0
        for row in vector:
            normal += row**2
        normal = (-1)*math.sqrt(normal) if A[col][col] > 0 else math.sqrt(normal)
        vectorIdentity *= normal
        result = vector-vectorIdentity
        return result.reshape(result.size, -1)
    
    def transformation(self, vector):
        transposed = vector.reshape(-1, vector.size)
        numerator = np.dot(vector, transposed)
        denominatorScalar = np.dot(transposed, vector)
        H = self.I - 2*(numerator/denominatorScalar)
        return H
    
    def solution(self):
        resultA, resultB = None, None
        for col in range(self.n):
            if col:
                vector = self.vectorIsolation(resultA, col)
                H = self.transformation(vector)
                resultA = np.dot(H, resultA)
                resultB = np.dot(H, resultB)
            else:
                vector = self.vectorIsolation(self.A, col)
                H = self.transformation(vector)
                resultA = np.dot(H, self.A)
                resultB = np.dot(H, self.b)
        return self.sucesiveBack(resultA, resultB, self.n)
        