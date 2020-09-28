
class Sucesion:
    def __init__(self):
        pass
    
    def sucesiveBack(self, A, b, n):
        x = [1 for _ in range(n)]
        x[n-1] = b[n-1]/A[n-1][n-1]
        for i in range(n-2, -1, -1):
            tmpi = b[i]
            for j in range(i+1, n):
                tmpi -= A[i][j]*x[j]
            x[i] = tmpi/A[i][i]
        return x
    
    def sucesiveFront(self, A, b, n):
        x = [1 for _ in range(n)]
        x[0] = b[0]/A[0][0]
        for i in range(1, n):
            tmpi = b[i]
            for j in range(0, i-1):
                tmpi -= A[i][j]*x[j]
            x[i] = tmpi/A[i][i]
        return x