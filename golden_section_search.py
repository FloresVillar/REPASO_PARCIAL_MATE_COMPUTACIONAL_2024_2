import matplotlib.pyplot as plt
import numpy as np
import math as mt 
from statistics import *
from fibonnaci import *

def golden_section_search(a, b,epsilon=0.01):
    n = int((b -a)/(epsilon*PHI()))
    p = PHI() -1 
    d = p * b + (1 - p) * a
    yd  = f(d)
    for i in range(1, n):
        c = p*a +(1 - p) * b
        yc = f(c)
        if yc < yd: # el subintervalo der?
            b, d, yd = d, c, yc
        else:
            a, b = b, c #el izq
        i = i + 1
    if a < b:
        return i, np.array([a, b])
    else:
        return i, np.array([b, a])
    
if __name__=='__main__':    
    print('para la funcion analizada')
    i, X = golden_section_search(-2,6)
    print('min:' + str(round(mean(X),5))+' f(min):'+str(round(f(mean(X)),5))+' n: '+str(i))
    grafica()

"""
teoria.
tomando limite para n→ grande 
lim Fn / Fn-1  = phi 
La busqueda de seccion aurea usa la proporcion
aurea para aproximarse a la busqueda de fibonacci
Revisar el pdf traducido 
"""