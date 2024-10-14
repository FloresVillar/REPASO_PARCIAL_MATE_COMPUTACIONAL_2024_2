import numpy as np
import math as mt 
import matplotlib.pyplot as plt
from statistics import  *
from fibonnaci import *
#al inicio si siquiera se acerca al optimo, 
class Pt:
    def __init__(self,x,y):
        self.x = x
        self.y = y

#ejemplo de uso
#x = Complex(3.0, -4.5)
#x.r, x.i

def _inter(A,B, l = 1.1):
    t = ((A.y-B.y)-l*(A.x-B.x))/(2*l)       # ver el grafico las lineas de pendientes* +-l se cortaran en estos puntos al parecer
    return Pt(A.x + t, A.y -t*l)             #las distancia de a:x+→ y en y-↓

def shubert_piyasky(a, b, l=0.01,epsilon = 0.1, sigma= 0.1):
    m = (a + b)/2                           #el punto medio, comenzando el alg
    A, M, B = Pt(a, f(a)), Pt(m,f(m)), Pt(b, f(b))
    P_AM = _inter(A, M)
    P_MB = _inter(M, B)
    pts = [A, P_AM, P_MB, B]                #los 5 puntos
    delta = np.inf
    #for i in pts:
    #   print(str(i.x)+str(i.y))
    while delta > epsilon :                  # para hallar el minimo se recurrio a chta gpt GRAN AYUDA
        i = min(range(len(pts)), key=lambda idx: pts[idx].y)#el indice de menor P.y
        Pi = Pt(pts[i].x,f(pts[i].x))                            # el indice del de los 5 puntos con menor 'y'
        delta = Pi.y -pts[i].y
        if i != 0:                                  #encontrar el indice de menor P.y                       
            P_prev = _inter(pts[i-1],Pi)
            pts.insert(i, P_prev)
        if i != len(pts)-1:
            P_next = _inter(Pi, pts[i+1])
            pts.insert(i, P_next)
        pts.pop(i)
        pts.insert(i, Pi)
    intervals =[]
    P_min = pts[2 * min(range(len(pts[::2])), key=lambda i: pts[::2][i].y)-1]
    y_min = P_min.y
    for i in range(1,len(pts),2):
        if pts[i].y < y_min:
            dy = y_min
            x_lo = max(a, pts[i].x - dy/l)
            x_hi = min(b, pts[i].x + dy/l)
            if intervals and (intervals[-1][1] + sigma >= x_lo):
                intervals[-1] = (intervals[-1][1], x_hi)
            else:
                intervals.append((x_lo, x_hi))
    return (P_min,intervals)

if __name__=='__main__':
    P_min , puntos = shubert_piyasky(-2, 6)
    print('el min: '+ str(round(P_min.x,3))+' f(min): '+str(round(P_min.y,3)))
    print(puntos)
    grafica()










"""
    A diferencia de los anteriores es 
    un metodo de optimizacion global sobre un dominio
    Lo que se garantiza que converge en un minimo , 
    independientemente de minimos locales
    o de si la funcion es unimodal 

    un poco de teoria profunda*
    El metodo requiere que la funcion sea Lepschitz continua y
    -es continua
    -existe un limite superior en la magnitud de su derivada
    | f (x) - f(y)| ≤  l |x - y| for all x,y ∈ [a,b]
    viendo l  es tan grande como la mayor tasa instantanea de cambio
    sin signo que la funcion alcanza en [a, b]
    f (x0) - l(x-x0)for x > x0 and f(x0)+l(x-x0)forx < x0
    esto se supone que deriva de la expansion de taylor?

    revisar la teoria , lo de la region de incertidumbre 
    se ve interesante 

    para cada (xi, yi) y este contribuira a la region de certidumbre 
    solo si  cumple yi < ymin 
    La principal desventaja de  este metodo es que 
    requiere conocer una constante valida de lipschitz 
 
"""