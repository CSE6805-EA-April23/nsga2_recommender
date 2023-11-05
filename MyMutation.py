import math
import random

from pymoo.core.mutation import Mutation

import valueGenerator


class MyMutation(Mutation):
    def __init__(self):
        super().__init__()

    def _do(self, problem, X, **kwargs):

        # for each individual

        for i in range(len(X)):

            r = random.random()

            list1=[]
            if r < 0.5:
                for ij in X[i, 0]:
                    list1.append(ij)

                ids=random.sample(range(376), 37)
                for ii in ids:
                    list1[ii]=valueGenerator.value([1,0],list1[ii])
                X[i,0]=list1


        return X
