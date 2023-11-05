import random
import time
from operator import itemgetter

import numpy as np
from pymoo.core.parameters import flatten
from pymoo.core.problem import ElementwiseProblem
from pymoo.util.misc import stack


class MyProblem(ElementwiseProblem):

    def __init__(self, floyed_array,hps_array,n_size):
        super().__init__(n_var=1, n_obj=2, n_ieq_constr=0)
        self.floyed=floyed_array
        self.hps=hps_array
        self.n_size=n_size


    def _calc_pareto_front(self, flatten=False, *args, **kwargs):
        f2 = lambda f1: ((f1/100) ** 0.5 - 1)**2
        F1_a, F1_b = np.linspace(1, 16, 300), np.linspace(36, 81, 300)
        F2_a, F2_b = f2(F1_a), f2(F1_b)

        pf_a = np.column_stack([F1_a, F2_a])
        pf_b = np.column_stack([F1_b, F2_b])

        return stack(pf_a, pf_b, flatten=flatten)

    def _calc_pareto_set(self, *args, **kwargs):
        x1_a = np.linspace(0.1, 0.4, 50)
        x1_b = np.linspace(0.6, 0.9, 50)
        x2 = np.zeros(50)

        a, b = np.column_stack([x1_a, x2]), np.column_stack([x1_b, x2])
        return stack(a,b, flatten=flatten)

    def _evaluate(self, x, out, *args, **kwargs):


        # print the current timestamp


        delay, coverage , influencial= 0, 0, 0

        i=1
        list=[]
        influencial=0
        for ij in range(1,self.n_size+1):
            list.append(999999999)
        for c in x[0]:
            if c==1:
                influencial=influencial+1
                for jkk in range(1,self.n_size+1):

                    if list[jkk-1]>self.floyed[i-1][jkk-1]:
                        list[jkk-1]=self.floyed[i-1][jkk-1]
            i=i+1
        list1=[]
        i=1
        for ijkk in list:
            list1.append((i,ijkk))
            i=i+1

        list1=sorted(list1, key=itemgetter(1),reverse=True)
        #print(list1)
        delay=list1[0][1]




        i=1
        list=[]
        for ij in range(1,self.n_size+1):
            list.append(999999999)

        for c in x[0]:
            if c==1:
                for jkk in range(1,self.n_size+1):

                    if list[jkk-1]>self.hps[i-1][jkk-1]:
                        list[jkk-1]=self.hps[i-1][jkk-1]
            i=i+1
        list1=[]
        i=0
        pkg=0
        for ijkk in list:
            pkg=pkg+ijkk
            i=i+1
        coverage=pkg/i

        print([delay,influencial])

        #out["F"] = np.array([random.random(), random.random(),random.random()], dtype=float)
        out["F"] = np.array([delay,influencial], dtype=float)
        # out["G"]=200-influencial

