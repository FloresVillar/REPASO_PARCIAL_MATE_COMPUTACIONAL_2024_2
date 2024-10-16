import numpy as np
from scipy.optimize import minimize

def f(x):
    return (x[0]**2+x[1]**2+x[0]*x[1]-2*x[1])

def ff(v):
    x,y = v
    return (x**2+y**2+x*y-2*y)

def gf(x):
    return np.array([2*x[0]+x[1],x[0]+2*x[1]-2])

def grad_desc(x:np.array,lr=0.1,nMax=200,epsilon=0.0):
    points = []
    i = 0
    gr = gf(x)
    while i<nMax and np.linalg.norm(gr)>=epsilon:
        x = x -lr*gr
        gr = gf(x)
        points.append(x)
        i = i + 1
    return x

if __name__=='__main__':
    x1 = np.array([3,4])
    x = grad_desc(x1)
    print(x)
    print("scipy")
    x = minimize(ff,x0=[3,4])
    print(x.x)


"""
metodos de primer orden 
en el capitulo anterior se introdujo el concepto general de los 
metodos en la direccion de descenso 

en este capitulo se analizaran algunos algoritmos que utilizan metodos
de primer orden para seleccionar la DIRECCION DE DESCENSO adecuado 
los metodos de primer orden se basan en informacion de  gradiente para 
ayudar a dirigir la busqueda de un minimo , que se puede obtener 
usando los metodos descritos en el capitulo 2 
esto de primer orden es solo para HALLAR D direccion de descenso 

DESCENSO dE GRADIENTE :
una eleccion intuitiva para la direccion de descenso es 
la direcion de descenso mas pronunciado 
seguir la direccon de descenso mas pronunciado garantiza una mejora
siempre que la funion objetivo sea suave , el tamaño del paso 
sea lo suficientemente pequeño, y estemos ya en punto donde la gradiente es 0
la direccion de descenso mas pronunciada es la direccion opuesta al gradiente
de alli el nombre descenso de gradiente .
Por mayor comodidad en este capitulo veremos  
    g^k = delta f(x^k)
donde x^{k} es nuestro punto de diseño en la iteracion de descenso k

d^{k} = -g^{k}/||g^{k}||

se obtiene rutas de busqueda irregulares si elegimos un tamaño de paso 
que conduce a la disminucion maxima en f. De hecho la siguiente direccion 
siempre sera ortogonal  a la direccion actual 
demostracion :

conjugate gradiente
el descenso de gradiente puede tener un rendimiento deficiente 
en valles estrechos 
el metodo de gradiente conjugado supera este problema inspirandose 
en metodos de optmizacion cuadratica

minimizar f(x) = X^t A x + b^t x + c
    x

donde es simetrica definida positiva, y por lo tanto tiene un 
minimo local.

el metodo del gradiente conjugado permite optimizar funciones 
cuadraticas n dimensionales
sus direcciones son mutuamente conjungadas respcto A ????
d^(i) T   A  d^(j) = 0 
los vectores mutuamente conjugados son los vectores bases de A
generalmente no son ortogonales entre si 
las direcciones conjugadas sucesivas se calulan utilizando inforacion
del gradiente y de la direccion de descenso anterior 
el algoritmo comienza con la direccon de descenso mas pronunciado
    d1 = - g1
luego usamos la busqueda lineal para encontrar el siguiente punto 
de diseño
para cuadraticas , el factor de paso se puede calcular 
con exactitud
x^2 = x^1 + alpha^1 d^1
supongamos....
"""