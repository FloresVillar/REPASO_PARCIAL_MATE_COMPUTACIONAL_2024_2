import matplotlib.pyplot as plt
import numpy as np
import math as mt
#se analizo primero para f=(x-1)^2
""" las funciones de poca extension"""
from statistics import mean

e = mt.e

def f(x:float):
	return e**(x-2)-x

def gradF(x):
     return e**(x-2)-1

def f_b(x):
   return -((x+2)**2)*(x-3)

#para biseccion
def df_b(x):
   return -(2*(x + 2))*(x - 3)-(x + 2)**2

def fibonacci(n):
    a   =   1
    b   =   0
    for i in range(n):
        a, b = b, a + b 
    return b

def PHI(n=100):
    return fibonacci(n)/fibonacci(n-1)

def grafica():
    X = np.linspace(-5,5,100)
    Y = mt.e**(X-2)-X
    plt.plot(X,Y,'.')
    plt.show()

def grafica_b():
    X = np.linspace(-10,10,100)
    Y = -((X+2)**2)*(X-3)
    plt.plot(X,Y,'.')
    plt.show()