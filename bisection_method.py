import matplotlib.pyplot as plt
import numpy as np
import math as mt 
from statistics import *
from fibonnaci import *

f =df

def bracket_sign_change(a, b, k =2):
    if a > b:
        a, b = b, a 
        center, half_width = (b + a)/2, (b - a)/2
        while f(a) * f(b) > 0:
            half_width *=k
            a = center - half_width
            b = center - half_width
    return (a,b)

def bisection(a, b, epsilon = 0.01):
    if a > b :
        a, b =b, a
    ya, yb = f(a), f(b)
    if ya == 0:
        b = a
    if yb ==0:
        a = b
    while b - a > epsilon:
        x = (a + b)/2
        y = f(x)
        if y==0:
            a, b = x, x
        else:
            if mt.fabs(y)/y == mt.fabs(ya)/ya:
                a = x
            else:
                b = x 
    return (a,b)

if __name__=='__main__':
    X = bisection(-2, 6)
    print('el min: '+ str(round(mean(X)))+' f(min): '+str(round(f(mean(X)))))
    grafica()




























"""se utilizan para encontrar los puntos donde la funcionn es 0 (una raiz)
con todo , estos metodos de busqueda de raices se pueden usar para la optmizacion 
aplicandolo a la derivada del objetivo
claro , si derivada es = 0 , se tiene un minimo , no ?
Se debera asegurar que los puntos resultantes son de hecho minimos locales 

El metodo de la biseccion mantiene un [a, b] en el que se sabe que existe al menos
una raiz 
f es continua en [a, b] tal que f(x) = y  
y hay algun 'y' en [F(a), F(b)] por el teorema del valor intermedio
estipula que existe al menos un x en [a,b] tal que f(x) =y 
de ello se deduce que se garantiza que un corchete [a,b] contiene un cero si 
f(a)  y f(b) son de signos distintos

el metodo de la biseccion corta la region entre corchetes en la mitad y
el lado que continua encerrando un 0, se puede determinar si el punto medio 
se evalua como cero , de lo contrario se puede terminar luego de un numero 
fijo de iteraciones 
el metodo converge para epsilon a x* en n=lg(b-1/epsilon)  iteracciones

Los metodos de busqueda de raices requieren intervalos [a,b ] en lados 
opuestos de un cero, ver el grafico 
el algoritmo 3.7 proporciona para determinar el intervalo donde se da el 
cambio de signo 
comienza con un intervalo de estimacion [a, b] mientras sea valido 
su tamaño se incrementa por un factor constante 
duplicar el tamaño del intervalo es una opcion comun
este metodo no siempre tendra exito como se muestra 
ej, las funciones que tienen raices cercanas pueden pasarse por alto
haciendo que el intervalo aumente indefinidamente
el metodo de brent dekker es una extension del metodo de la biseccion ,
es  un algoritmo de busqueda de raices que combina elementos 
del metodo de la secante y  la interpolacion cuadratica inversa

tiene propiedades de convergencia rapidas y confiables 
Es el algoritmo de optimizacion univariante preferido en muchos paquetes 
de optmizacion numerica









"""