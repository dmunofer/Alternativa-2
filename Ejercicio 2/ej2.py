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

def sacar_c(formula):
    i=0
    while i in range(0,len(formula)):
        if formula[i]=='^':
            c=formula[i:]
        else:
            i+=1
    return c
def expand(formula):
    a=sacar_a(formula)
    b=sacar_b(formula)
    c=sacar_c(formula)
    x=2
    expansion=str(b**c)+' + '+str(a*c)+'x'
    while x<(c+1):
        nCr=(math.factorial(c))/((math.factorial(x))*(math.factorial(c-x)))
        expansion=expansion+' + '+str((a**x)*int(nCr))+'x^'+str(x)
        x=x+1
    return expansion

