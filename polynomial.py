import numpy as np

class Polynomial:
    def __init__(self, n=None, coefficient=[]):
        self.n = n
        self.coefficient = []
        self.setCoefficients(coefficient)
    
    def setCoefficients(self, coefficient):
        for n in coefficient:
            self.coefficient.append(float(n))
        return self

    def calculate(self, t):
        result = np.zeros(len(t))
        for i in range(len(self.coefficient)):
            result += self.coefficient[i]*(t**i)
        return result
    
    def displayPol(self):
        result = []
        for c in range(len(self.coefficient)):
            if c:
                result.append("{}*t^{}".format(self.coefficient[c], c))
            else:
                result.append(str(self.coefficient[c]))
        result = ' + '.join(result)
        print("-"*len(result))
        print(result)
        print("-"*len(result))
        return self