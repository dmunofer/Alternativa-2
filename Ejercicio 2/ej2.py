import math

def sacar_a(formula):
    i=0
    while i in range(0, len(formula)):
        if type(formula[i])!=str:
            i+=1
        else:
            a=formula[0:i]
    return a,i

def sacar_b(formula):
    a,i=sacar_a(formula)
    cont=0
    while i+1 in range(0, len(formula)):
        if formula[i+1]!=')':
            cont+=1
        else:
            b=formula[1+1:cont]
    return b


