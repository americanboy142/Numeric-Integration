import numpy as np

#%{
#   FUNCTIONS
#       the three functions given
#}

def f(x):
    return np.cos(np.pi*x)

def g(x):
    if(x >= 0):
        return x**2
    else:
        return -x**2

def h(x):
    return np.exp(-x**2/2)


#%{
#   INDEX
#       makes formating matrix easier
#}

trap_index = 0
simp_index = 3
Gauss_index = 6

# true values of each function in order of functions

TrueValues = [-0.098363164308346596735,0.11033333333333333333,1.7688741449316336902]