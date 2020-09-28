
from equation import NormalEquation
from householder import HouseHolder
import numpy as np

def main():
    t = [-1.0, -0.5, 0.0, 0.5, 1.0]
    y = [1, 0.5, 0, 0.5, 2]
    n = 3 ## Grade of polynomial

    ec = NormalEquation(t, y, n)
    print(np.around(ec.solution(), 3))

    hh = HouseHolder(t, y, n)
    print(np.around(hh.solution(), 3))


if __name__ == "__main__":
    main()