import numpy as np
import math as mt 
from statistics import *
import matplotlib.pyplot as plt
from fibonnaci import * 
# en principio no funciona tan bien como el bracket
#corrigiendo algunos detalles y es mas eficiente 
# en tan solo 10 iteraciones se obtiene el optimo

def S():
    return (1-5**.5)/(1+5**.5)

def fibonacci_search(a,b,n,epsilon=0.01):
    s =S()
    phi = PHI()
    p = (1 - s**n)/(phi*(1 - s**(n + 1))) # se entiende que estas proporciones son necesarias
    d = p*b + (1 - p)*a                                 #               se obtiene d 
    print('el valor de d:'+str(d)+' f(d):'+str(f(d)))    # a------c-----d-------b
    yd = f(d)
    for i in range(1,n):
        if i == n-1:                                    #       se obtiene c    
            c = epsilon*a + (1 - epsilon)*d             #  a------c-----d-------b
            print('c:'+str(c)+' f(c):'+str(f(c)))
        else:
            c = p*a + (1 - p)*b
        print('c:'+str(c)+' f(c):'+str(f(c)))
        yc = f(c)
        if yc < yd: #obteniendo intervalo mas pequeño
            b, d, yd = d, c, yc     #lado izquierdo
        else:
            a, b = b, c     #lado derecho
        p = (1 - s**(n - i))/(phi*(1 - s**(n - i + 1)))
    if a < b:
        return np.array([a, b])
    else:
        return np.array([b, a])

def grafica(n=50):
    X  = np.linspace(0, 5, n)
    Y = mt.e**(X-2)-X
    plt.plot(X,Y,'o')
    plt.show()

if __name__=='__main__':
    #print('valor de phi'+ str(PHI(100)))
    n  = 5
    X = fibonacci_search(-2,6,n)
    print('min:' + str(round(mean(X),5))+' f(min):'+str(round(f(mean(X)),5)))
    grafica()
