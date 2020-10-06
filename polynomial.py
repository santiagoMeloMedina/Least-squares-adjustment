import numpy as np

class Polynomial:
    def __init__(self, n=None, coefficient=None):
        self.n = n
        self.coefficient = coefficient
    
    def setCoefficients(self, coefficient):
        self.coefficient = coefficient
        return self

    def calculate(self, t):
        result = np.zeros(len(t))
        for i in range(len(self.coefficient)):
            result += self.coefficient[i]*(t**i)
        return result