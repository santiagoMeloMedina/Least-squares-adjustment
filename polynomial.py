
class Polynomial:
    def __init__(self, n=None, coefficient=None):
        self.n = n
        self.coefficient = coefficient
    
    def setCoefficients(self, coefficient):
        self.coefficient = coefficient
        return self

    def calculate(self, t):
        result = 0
        for i in range(self.n):
            result += self.coefficient[i]*(t**i)
        return result