import numpy as np 
import math as mt 
import matplotlib.pyplot as plt
from statistics import *
#from fibonnaci import *
#from bracket_minimum import *
e=mt.e

def S():
    return (1-5**.5)/(1+5**.5)

def f(x):
    return e**(x-2) -x

def PHI(n=100):
    return fibonacci(n)/fibonacci(n-1)

def fibonacci(n):
    a   =   1
    b   =   0
    for i in range(n):
        a, b = b, a + b 
    return b

# para la busqueda en linea
# se debe redefinir la funcion de acuerdo a ...
#el tamaño del paso es 0.01
# como x '  = x + alpha *d
# def f(x:float):
#	return mt.e**(x-2)-x        revisa el ejempplo 4.1 de linear search
#redefinir la funcion para cada x0 y d (conocidos) 
# x0 = 1 , d= 1
#e**(alpha -1) -(1 + alpha)
# si d=2  x0=1      x = 1 +alpha*2
#e ^() -(1+alpha)

#def objetivo(alpha,x0=1,d=1):
#    return e**(alpha -1) -(1 + alpha)

def objetivo(alpha,xo=1):
    return e**(1 -alpha/e +alpha -2) -(1 - alpha/e + alpha)

def bracket_minimum(alpha0 , s=10**-2 , k=2):  
    a, ya  =alpha0, objetivo(alpha0)                               
    b, yb = a + s, objetivo(a + s)                      
    if yb > ya:  
        a, b = b, a                              
        ya, yb = yb, ya                         
        s = -s                                                                   
    while True:
        c, yc = b + s, objetivo(b +s)
        if yc > yb:     
            if a < c:
                return np.array([a,c]) 
            else: 
                return np.array([c,a])
        a, ya, b, yb = b, yb, c, yc 
        s = s * k  

def fibonacci_search(a,b,n,epsilon=0.01):
    s =S()
    phi = PHI()
    p = (1 - s**n)/(phi*(1 - s**(n + 1))) # se entiende que estas proporciones son necesarias
    d = p*b + (1 - p)*a                                 #               se obtiene d     # a------c-----d-------b
    yd = objetivo(d)
    for i in range(1,n):
        if i == n-1:                                    #       se obtiene c    
            c = epsilon*a + (1 - epsilon)*d             #  a------c-----d-------b
        else:
            c = p*a + (1 - p)*b
        yc = objetivo(c)
        if yc < yd: #obteniendo intervalo mas pequeño
            b, d, yd = d, c, yc     #lado izquierdo
        else:
            a, b = b, c     #lado derecho
        p = (1 - s**(n - i))/(phi*(1 - s**(n - i + 1)))
    if a < b:
        return np.array([a, b])
    else:
        return np.array([b, a])
# x0 = 1 , d= 1
#e ^(alpha -1) -(1+alpha)    
    #definiendo una nueva funcion objetivo (eso creo)
    #objetive = alpha → f(x +alpha *d)
def line_search(x0 =1, d=1):
    alpha0 = 0
    I = bracket_minimum(alpha0)#obtiene el intervalo
    print('bracket_minium: '+str(mean(I))+' '+str(f(mean(I))))
    n = 100
    alpha = mean(fibonacci_search(I[0],I[1],n))
    return alpha

if __name__=='__main__':
    alpha = line_search()
    print('alpha:' + str(alpha) + 'f(1+alpha*d): '+str(f(1-alpha*(1/e-1))))
    print(1-alpha*(1/e-1))


"""
Se ha analizado la optimizacion de f univariante, de una sola
variable 
En este capitulo nos enfocaremos en funciones multivariadas
el enfoque es como utilizar modelos locales para mejorar
de forma incremental un punto de diseño hasta que se cumpla
con algun criterio de convergencia 


Se comienza analizando metodos, que (en cada iteracion )
eligen una direccion de descenso basada en un modelo local
y luego eligen un tamaño de paso
Luego se analizan metodos que restringen el paso para
que este dentro de una region donde se cree que el modelo
local es valido 
Concluyendo con un analisis de la convergencia 

iteracion de la direccion de descenso.
un enfoque comun para la optimizacion es mejorar de 
manera incremental un punto de diseño X 
mediante la adopcion de un paso que minimice el valor
objetivo en funcion de un modelo local 
El modelo local puede obtenerse ,ej, a partir de la 
aproximacion de Taylor de 1er o 2do orden 
Los algoritmos de optmizacion que siguen este enfoque 
Los algoritmos que siguen este enfoque se denominan
METODOS DE DIRECCION DESCENDENTE 
comienzan con un punto de diseño x y luego generan 
una secuencia de puntos , denominado iteracciones 
para converger a un minimo local 

el procedimiento de descenso iterativo implica : 
1 . - verificar si x^{k} cumple con las condiciones 
de terminacion , si, terminar, no , continuar 

2 . -Determinar la direccion de descenso d^{k} 
usando la informacion local como la gradiente 
o Hessiano, algunas lagoritmos suponen que ||d^{k}||=1

la eleccion de x^{1} afecta el exito del algoritmo 
el conocimiento del dominio se usa para elegir 
un valor razonable 

3 . -determinar el tamaño de paso o tasa de aprendizaje 
alpha ^{k} algunos algoritmos intentan optmizar el 
tamaño de paso alpha para que este disminuya al maximo f

4 . -calcule el siguiente punto de diseño 
    x ^{k +1} ←  x^{k} + alpha^{k} d^{k}

hay muchos metodos de optmizacion diferentes , cada 
uno con sus propias formas de determinar alpha y d    

Busqueda de Linea
suponer que se ha elegido una direccion de descenso s, 
se necesita elegir un factor de paso ALPHA para
obtener el siguiente punto de diseño 
un enfoque es usar la busqueda en linea, que 
selecciona el factor de paso que minimiza la funcion 
unidimensional
        minimizar f(x + alpha * d)
LA busqueda lineal es un problema de optmizacion univariante
podemos apicar el metodo de optmizacion univariante que elijamos
para fundamentar la busqueda podemos usar, la derivada del objetivo
de busqueda lineal, que es la derivada direccional 
a lo largo de D en x + alpha * D 




"""