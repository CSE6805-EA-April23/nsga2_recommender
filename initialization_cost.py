import math
import pickle
import random
from pymoo.core.sampling import Sampling
import numpy as np
import cheks12
import init_cost

class MySampling(Sampling):

    def _do(self, problem, n_samples, **kwargs):

        population=init_cost.degree_()

        X = np.full((n_samples, 1), 0,dtype=list)


        with open('floyd\\hps', 'rb') as f:
            data = pickle.load(f)
        #print(data)

        for i in range(n_samples):
            X[i, 0] = population[i]

        return X
