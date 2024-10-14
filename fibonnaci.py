import matplotlib.pyplot as plt
import numpy as np
import math as mt
#se analizo primero para f=(x-1)^2
""" las funciones de poca extension"""
from statistics import mean

def f(x:float):
	return mt.e**(x-2)-x

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