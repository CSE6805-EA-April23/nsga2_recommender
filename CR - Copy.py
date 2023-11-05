import random
from random import randrange

from pymoo.core.crossover import Crossover
import numpy as np

import valueGenerator

class MyCrossover(Crossover):

    def __init__(self, prob=0.5, **kwargs):
        super().__init__(2, 2, **kwargs)
        self.prob = prob

    def _do(self, problem, X, **kwargs):

        _X = np.copy(X)
        for i in range(len(_X[0])):

            list1=[]
            list2=[]
            for j in range(len(X[0][0][0])):
                p=random.choice([0,1])
                if p==1:
                    list1.append(_X[0][i][0][j])
                    list2.append(_X[1][i][0][j])
                else:
                    list2.append(_X[0][i][0][j])
                    list1.append(_X[1][i][0][j])


            _X[0][i][0]=list1
            _X[1][i][0]=list2

        return _X
