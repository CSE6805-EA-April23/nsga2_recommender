import inspect
import pickle
import random
import string
import numpy as np
from matplotlib import pyplot as plt
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.algorithms.soo.nonconvex.pso import PSO
from pymoo.core import problem
from pymoo.factory import get_problem
from pymoo.util.display.column import Column
from pymoo.util.display.output import Output
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.visualization.scatter import Scatter

from MyMutation_cost import MyMutation
from  MyProblem_Advertise import MyProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
import pymoo.optimize as optimize
from duplicates import MyDuplicateElimination
from CR import MyCrossover
from initialization import MySampling
print("START")

class MyOutput(Output):

    def __init__(self):
        super().__init__()


    def update(self, algorithm):
        super().update(algorithm)
        print(algorithm.pop.get("X"))
        # plt.scatter(res.F[:, 0], res.F[:, 1], s=30, facecolors='none', edgecolors='b', label="Solutions")
        # plot.add(problem_1.pareto_front(), plot_type="line", color="black", alpha=0.7)
        # plot.show()



algorithm_name='NSGA2'

if algorithm_name=='NSGA3':
    ref_dirs = get_reference_directions("uniform", 2, n_partitions=12)
    algorithm = NSGA3(pop_size=100,
                      sampling=MySampling(),
                      crossover=MyCrossover(0.5),
                      mutation=MyMutation(),eliminate_duplicates=MyDuplicateElimination(),save_history=True,
                      ref_dirs=ref_dirs
                     )
if algorithm_name=='NSGA2':

    algorithm = NSGA2(pop_size=100,
                          sampling=MySampling(),
                          crossover=MyCrossover(0.5),
                          mutation=MyMutation(),eliminate_duplicates=MyDuplicateElimination(),save_history=True
                         )


if algorithm_name=='RNSGA2':
    algorithm = NSGA2(pop_size=100,
                          sampling=MySampling(),
                          crossover=MyCrossover(0.5),
                          mutation=MyMutation(),eliminate_duplicates=MyDuplicateElimination(),save_history=True
                         )


with open('floyd\\floyd', 'rb') as f:
    floyd = pickle.load(f)

with open('floyd\\hps', 'rb') as f:
    hps = pickle.load(f)



plt.figure(figsize=(7, 5))

problem_1=MyProblem(floyd,hps,376)
res = optimize.minimize(problem_1,
               algorithm,
               ('n_gen', 100),
               seed=1, output=MyOutput(),
               verbose=True)


dbfile = open('history\\social_media_d_c_c_nc'+algorithm_name, 'wb')
pickle.dump(res.history,dbfile)
dbfile.close()

ip=1
for ij in res.history:
    c='#'
    if  ip%10==0:
        for i in range(0,6):
            c=c+random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])

        lists=[]

        for k in ij.opt:
            lists.append(k.F.tolist())
        print(lists)

        plt.scatter(np.array(lists)[: , 0], np.array(lists)[:,1], s=ip, facecolors=c, edgecolors=c,label=str(ip)+'th Iteration')


    ip=ip+1

plt.title("Objective Space")
plt.legend()
plt.show()
# n_evals = np.array([e.evaluator.n_eval for e in res.history])
# opt = np.array([e.opt[0].F for e in res.history])
#
# plt.title("Convergence")
# plt.plot(n_evals, opt, "--")
# plt.yscale("log")
# plt.show()

# pf_a, pf_b = problem_1.pareto_front(use_cache=False, flatten=False)
# pf = problem_1.pareto_front(use_cache=False, flatten=True)
# plt.plot(pf_a[:, 0], pf_a[:, 1], alpha=0.5, linewidth=2.0, color="red", label="Pareto-front")
# plt.plot(pf_b[:, 0], pf_b[:, 1], alpha=0.5, linewidth=2.0, color="red")

# plt.scatter(res.F[:, 0], res.F[:, 1], s=30, facecolors='none', edgecolors='b', label="Solutions")
# plt.title("Objective Space")
# plt.legend()
# plt.show()


# print(res.pf)
# plot.add(res.pf, facecolor="none", edgecolor="red")
# plot.show()
# print("RESULTS")
# print(res)

