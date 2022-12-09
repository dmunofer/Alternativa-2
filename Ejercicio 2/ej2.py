import math

def sacar_a(formula):
    i=0
    while i in range(0, len(formula)):
        if type(formula[i])!=str:
            i+=1
        else:
            a=formula[0:i]
    return a


