from fibonnaci import *
import numpy as np 
import math as mt 
import matplotlib.pyplot as plt

def valor_critico(a, b, c):
    ya, yb, yc = f(a), f(b), f(c)
    return .5*(ya*(b**2-c**2)+yb*(c**2-a**2)+yc*(a**2-b**2))/(ya*(b-c)+yb*(c-a)+yc*(a-b))
    
def quadratic_fit_search(a, b, c, n=50):
    ya, yb, yc = f(a), f(b), f(c)
    for i in range(1,n-2):
        x = valor_critico(a, b, c)
        yx = f(x)
        if x > b:
            if yx > yb: #x es mayor que b y esta mas arriba 
                c, yc = x, yx #se achica hacia de derecha a izq← 
            else:
                a, ya, b, yb =b, yb, x, yx#se achica hacia → ahora b toma el lugar de a, se convierte en extremo izq
        else: #x no es mayor que b
            if yx > yb:
                a, ya = x, yx # x toma el lugar de a (→)y es el nuevo extremo izq
            else:
                c, yc, b, yb = b, yb, x, yx #achicar (←) b toma el lugar de c, se convierte en nuevo extremo der
    return np.array([a, b, c])

if __name__=='__main__':
    X = quadratic_fit_search(1, 1.5, 4)
    print('min:' + str(((X[0]+X[1])/2,5))+' f(min):'+str(round(f((X[0]+X[1]/2)),5)))
    grafica()

"""
usamos la capacidad de resolver analiticamente el minim
de una funcion cuadratica, muchos minimos locales parecen
cuadraticos cuando hacemos un zoom suficiente.
la busqueda de ajuste cuadratico ajusta iteativamente una u
una funcion cuadratica a 3 puntos de delimitacion 
resuelve un minimo  eligiendo un nuevo conjunto de puntos
de delimitacion y repite el proceso 
 q(x)=p1+p2x+p3x2  se hallaran los coeficientes
 ya=p1+p2a+p3a2     teniendo 3 puntos a,b,c y sus ya,yb,yc
 yb=p1+p2b+p3b2     reemplazando en la definicion de q(x)
 yc=p1+p2c+p3c2
 revisar la teoria del libro
 yo pensaria que al hallar pi= INV(M) *ya
 pero la expresion q(x) tiene una forma  del polinomio de lagrange 

 q(x)=ya
 (x−b)(x−c)
 (a−b)(a−c) +yb
 (x−a)(x−c)
 (b−a)(b−c) +yc
 (x−a)(x−b)
 (c−a)(c−b) (3.11)
 derivando e igualando a cero para hallar el valor critico x*
 x∗=1
 2
 ya(b2−c2)+yb(c2−a2)+yc(a2−b2)
 ya(b−c)+yb(c−a)+yc(a - b) 
"""