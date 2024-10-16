import numpy as np
import math as mt 

"""f (x , y) = x^2 +xy +y^2 - 2y
        x + y - 2 <=0"""

def f(X):
    x, y =X
    return x**2 +x*y + y**2 - 2*y
 
def Gr(X):
    x,y = X
    dx = 2*x + y 
    dy = x +2*y -2
    return np.array([dx,dy])

def Hessian(X):
    x,y = X
    dx = 2*x + y 
    dy = x +2*y -2
    dxx = 2
    dyx = 1
    dxy = 1
    dyy = 2
    return np.array([[dxx,dyx],[dxy,dyy]])

def metodo_newton(X,nMax=50,epsilon=0.01):
    delta = np.inf
    i = 1
    while delta > epsilon and i<nMax:
        H = Hessian(X)
        gr = Gr(X)
        H_i = np.linalg.inv(H)
        X1 = X-H_i@gr
        delta = np.linalg.norm(X1-X)
        i = i + 1
        X = X1
    return X

def trust_region_descent(X,nMax = 50, n1 = 0.25, n2 = 0.5, y1 = 2, y2 =2, delta =1):
    x1 , y1 =solve_trust_region_subproblem(X,delta)   



def solve_trust_region_subproblem(X,delta):
        
    return 1



if __name__=='__main__':
    X = np.array([1,1])
    X = metodo_newton(X)
    print("minimo")
    print(X)























""""
los metodos de descenso pueden confiar demasiado en su informacion
de primer o segundo orden 
lo que puede dar como resultado pasos excesivamente grandes
o convergencia prematura 
una region de confianza es el area local del espacio de diseño donde 
se cree que el modelo local de es confiable , un metodo de confianza
o metodo de paso restringido ,mantiene un modelo de confianza que limita el paso tomado 
por la busqueda de linea tradicional y predice la mejora asoiada con tomar 
el paso 
Si la mejora se desvia del valor predicho , la region de confianza se contrae
Se proporciona una revision reciente de los metodos de region de confianza

Los metodos de region de confianza primero eligen el tamaño maximo del paso
y luego la direccion . lo que contrasta con los metodos de busqueda 
de linea que primero eligen la direccion del paso
y luego oprimizan el tamaño del paso

un enfoque de region de confianza encuentra el siguiente paso por minimizando
un modelo de la funcion objetivo f sobre una region de confianza centrada 
en el punto de diseño actual x.un ejemplo de f* es una aproximacion 
de taylor de segundo orden 
el radio de la region de confianza  'delta' se expande y se contrae 
en funcion de lo bien que el modelo predice las evaluaciones
de la funcion 
El siguiente punto x' se obtiene resolviendo :
    minimizar f*(x') 
        x'

    sujeto a || x - x' || <= delta

    donde la region de confianza esta definida por el radio positivo delta 
    y una norma vectorial 
    la ecuacion anterior es un problema de optimizacion restringida 
    figura 4.8 los metodos de region de confianza limitan el siguiente paso 
    a una region local 
    la region de confianza se expande y se contrae en funcion del 
    rendimiento predictivo de los modelos de la funcion objetivo
    El radio de la region de confianza se expande o se contrae 
    en funcion delrendimiento predictivo del modelo local 

    los metodos de la region de confianza comparan la mejora prevista
    delta y_pred = f(x) - f^(x')
    a la mejora real
    delta y_act = f(x) -f(x')
     n = mejora actual/ mejora prevista
    si n es cercana a 1, el tamaño del paso predictivo coincide
    con el tamaño de paso real,  Si la relacion es demasiado pequeña
    como por ejemplo debajo de un umbral n1
    entonces la mejora se considera suficientemente menor que la 
    esperada,  y el radio de la region de confianza se reduce
    osea que en esa region ACTUAL no se otendria una mejora 
    MEJOR respecto  a la predicha.
    por ello el radio se reduce por un factor y1<1

    en cambio si la relacion es suficientemente grande como 
    por encima de un umbral n2, entonces nuestra prediccion 
    se considera precisa
    y el radio de la region de confianza se aumenta por un factor y2>1

    el algoritmo 4.4 el metodo de descenso de la region de confianza
    f , funcion , H derivada kmax, numero de iteraciones n1.n2 parametros o
    opcionales, determinan cuanto se aumenta     o disminuye , 
    se debe proporcionar una implementacion para SOLVE_TRUST_REGION_SBPROBLEM
    que resuelve la ecuacion 4.10
    se proporciona una implementacion de ejemplo que utiliza una aprox
    de taylor de sugindo orden . sobre S0 con una regon de cofianza circular 

    condiciones de rescision :
    -maximo numero de iteraciones k>kmax

    -mejora absoluta
    f(x^{k})-f(x^{k+1}) < epsilon

    -mejora relativa
    f(x^{k})-f(x^{k+1}) < epsilon_relativo | f(x^{k})|
    
    -magnitud de gradiente 
    ||grad  f(x^{k+1})|| < epsilon_gradiente
    
    en los casos en que es probable que existan multiples minimos
    locales, puede ser beneficioso incorporar reinicios aleatorios
    despues de que se cumplan nuestras condiciones de terminacion
    donde reiniciamos nuestro metodo de descenso local desde puntos 
    iniciales seleccionados aleatoriamente

"""