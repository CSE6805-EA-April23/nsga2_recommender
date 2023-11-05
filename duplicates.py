from pymoo.core.duplicate import ElementwiseDuplicateElimination

class MyDuplicateElimination(ElementwiseDuplicateElimination):

    def is_equal(self, a, b):

        for i in range(len(a.X[0])):

            if a.X[0][i]!=b.X[0][i]:

                return 1

        return 0
