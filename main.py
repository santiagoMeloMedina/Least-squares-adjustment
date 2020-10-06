
from equation import NormalEquation
from householder import HouseHolder
from polynomial import Polynomial
import matplotlib.pyplot as plt
import numpy as np
import pandas
import math
from constant import MESSAGES, ASSETS_FOLDER, NAMES

def preparingData(file):
    data = pandas.read_csv(ASSETS_FOLDER(file))
    t = data["t"].tolist()
    y = data["y"].tolist()
    return t, y

def segregateData(t, y):
    trainin, trainout, train_size = lambda i: float(t[i*2]), lambda i: float(y[i*2]), len(t)//2
    validin, validout, valid_size = lambda i: float(t[(i*2)+1]), lambda i: float(y[(i*2)+1]), len(t)//2
    training_input, training_output = [trainin(i) for i in range(train_size)], [trainout(i) for i in range(train_size)]
    validation_input, validation_output = [validin(i) for i in range(valid_size)], [validout(i) for i in range(valid_size)]
    return training_input, training_output, validation_input, validation_output

def normalEquations(n, tt, ty):
    n = n if len(tt) >= n else len(ty)
    ec = NormalEquation(tt, ty, n)
    x = np.around(ec.solution(), 3)
    return Polynomial(n=n, coefficient=x)

def houseHolder(n, tt, ty):
    n = n if len(tt) >= n else len(ty)
    hh = HouseHolder(tt, ty, n)
    x = np.around(hh.solution(), 3)
    return Polynomial(n=n, coefficient=x)

def getValues(pol, vt, vy):
    error = [abs(v) for v in np.array(vy)-pol.calculate(np.array(vt))]
    error_medio = sum(error)/len(error)
    deviation = math.sqrt(sum([e**2 for e in error])/len(error))
    print("{}{}".format(MESSAGES["MAE"], error_medio))
    print("{}{}".format(MESSAGES["SD"], deviation))
    return

def plotting(tt, ty, vt, vy, dataRange, adjustment):
    plt.plot(tt, ty, 'ro', label=NAMES["TRAINING"], color="blue")
    plt.plot(vt, vy, 'ro', label=NAMES["VALIDATION"], color="red")
    plt.plot(dataRange, adjustment, label=NAMES["ADJUSTMENT"])
    plt.legend()
    plt.show()


def main():
    n = int(input(MESSAGES["GRADE"])) ## Grade of polynomial
    t, y = preparingData(input(MESSAGES["FILE"]))
    tt, ty, vt, vy = segregateData(t, y)
    if not int(input(MESSAGES["OPERATION"])):
        pol = normalEquations(n, tt, ty)
    else:
        pol = houseHolder(n, tt, ty)
    pol.displayPol()
    dataRange = np.linspace(min(t), max(t), num=100)
    adjustment = pol.calculate(dataRange)
    getValues(pol, vt, vy)
    plotting(tt, ty, vt, vy, dataRange, adjustment)
    return


if __name__ == "__main__":
    main()