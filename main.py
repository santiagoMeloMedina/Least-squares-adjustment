
from equation import NormalEquation
from householder import HouseHolder
from polynomial import Polynomial
import matplotlib.pyplot as plt
import numpy as np
import pandas

def main():
    data = pandas.read_csv("data.csv")
    t = data["t"].tolist()
    y = data["y"].tolist()
    n = 3 ## Grade of polynomial

    trainin, trainout, train_size = lambda i: float(t[i*2]), lambda i: float(y[i*2]), len(t)
    validin, validout, valid_size = lambda i: float(t[(i*2)+1]), lambda i: float(y[(i*2)+1]), len(t)//2

    training_input, training_output = [trainin(i) for i in range(train_size)], [trainout(i) for i in range(train_size)]
    validation_input, validation_output = [validin(i) for i in range(valid_size)], [validout(i) for i in range(valid_size)]

    startt, endt = min(training_input), max(training_input)
    size = 100
    functionRange = np.linspace(startt, endt, num=size)

    n = n if len(training_input) >= n else len(training_input)

    if n < 13:
        ec = NormalEquation(training_input, training_output, n)
        x = np.around(ec.solution(), 3)
    else:
        hh = HouseHolder(training_input, training_output, n)
        x = np.around(hh.solution(), 3)

    pol = Polynomial(n=n, coefficient=x)

    function = [pol.calculate(c) for c in functionRange]
    error = [pol.calculate(v) for v in validation_input]

    plt.plot(training_input, training_output, 'ro', label="Entrenamiento")
    plt.plot(functionRange, function, label="Ajuste")

    plt.legend()
    plt.show()


    
    


if __name__ == "__main__":
    main()