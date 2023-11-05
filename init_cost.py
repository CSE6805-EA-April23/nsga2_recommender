import math
import pickle
from operator import itemgetter
import random

import numpy as np


# h = np.full((10, 1),0, dtype=list)
#
# for i in range(10):
#     h[i, 0] = [1, 3, 4]
# print(h)
import valueGenerator


def degree_():
    degree_count={}
    f = open("floyd\\hp1.txt", "r")
    for j in f.readlines():
        ij=int(j[0:j.index(' ')])

        if ij in degree_count:
            degree_count[ij]=degree_count[ij]+1
        else:
            degree_count[ij]=1

    degrees=[]
    for i in degree_count:
        degrees.append((i,degree_count[i]))
    degrees=sorted(degrees,key=itemgetter(1),reverse=True)
    degree=degrees
    s= len(degree)//2
    strong=degree[:s]
    w=degree[s:]
    sp=math.floor(s*0.000)
    ini=[]
    for i in range(0,376):
        ini.append(0)
    for i in range(0,sp):
        ini[degree[i][0]]=1

    population=[]
    while(True):
        listo=[]
        for j in range(0,376):
            p=ini[j]
            pb=random.random()
            if pb<0.5:
                p=valueGenerator.value([0,1,2,3],0)
            listo.append(p)
        #if  0.05>sum(listo)/376:
        population.append(listo)
        if len(population)>100-1:
            break

    return population




