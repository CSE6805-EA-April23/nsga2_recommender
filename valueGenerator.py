import random


def value(values,current_value):
    vals=[]
    for i in values:
        if i!=current_value:
            vals.append(i)
    ij=random.choice(vals)
    return ij

