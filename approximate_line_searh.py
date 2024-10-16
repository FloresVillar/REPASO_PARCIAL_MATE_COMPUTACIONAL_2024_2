import math as mt 
import numpy as np
from statistics import *
from fibonnaci import *
#entonces alpha , d son argumentos? bueno...

def backtracking_line_search(x, d, alpha, p = 0.5, beta =10**-4):
    y, grad = f(x), gradF(x)  #gradiente f(x)
    while f(x + alpha * d) > y + beta * alpha * grad * d:
        alpha *=p
    return alpha

def strong_backtracking(x, d, alpha =1, beta = 10**-4, sigma = 0.1):
    y0, g0, y_prev, alpha_prev, = f(x), gradF(x)*d,np.nan ,0
    alpha_lo, alpha_hi = np.nan, np.nan
    #bracket phase /fase de horquillado
    while True:
        y = f(x + alpha*d)
        if y > y0 + beta * alpha * g0 or (not np.isnan(y_prev) and y>=y_prev):
            alpha_lo, alpha_hi = alpha_prev, alpha
        g = gradF(x + alpha * d)*d
        if mt.fabs(g)<=-sigma*g0:
            return alpha 
        else:
            if g>=0:
                alpha_lo, alpha_hi = alpha, alpha_prev
        y_prev, alpha_prev, alpha = y, alpha, 2*alpha       
    #zoom phase
    y_lo = f(x + alpha_lo * d)
    while true:
        alpha = (alpha + alpha_hi)/2
        y = f(x + alpha*d)
        if (y>y0 + beta*alpha*g0) or y>=y_lo:
            alpha_hi = alpha
        else:
            g = gradF(x + alpha*d)*d
            if mt.fabs(g)<=-sigma*g0:
                return alpha
            else :
                if g*(alpha_hi-alpha_lo)>=0:
                    alpha_hi = alpha_lo
            alpha_lo = alpha

if __name__=='__main__':
    x0 = 0
    d = 1
    alpha = 10
    print(backtracking_line_search(x0, 1, alpha))    
    print(strong_backtracking(x0,d))



"""
    Busqueda de linea aproximada 

    A menudo resulta mas eficiente desde el punto de vista cmputaciones 
    realizar mas iteraciones del metodo de descenso 
    que realizar una busqueda de linea exacta en cada iteracion    
    especialmente si los calculos de la funcion y la derivada son costosos
    muchos de los metodos analizados hasta ahora pueden 
    beneficiarse del uso de una busqueda de linea aproximada
    para encontrar el tamaño de paso necesario 
    adecuado con una pequeña cantidad de evaluaciones
    Aunque se pueden aplicar diversas otras condicones para 
    fomentar una convergencia  mas rapida

    La condicion para una disminucion sufiente requiere que el
    tamaño de paso provoque una disminucion suficiente 
    en el valor de lla funcion
    f(x^{k + 1}) <=f(x^{k}) + beta * alpha *gradiente f(^{k}) en direccion d^{k}

    donde beta pertenece [0,1] a menudo beta = 10**-4 si b =0 entonces 
    cualquier disminucion es aceptable ,  beta =1 la disminucion tiene
    que ser(al menos) tan grande como la que se predeceria 
    mediante una aproximacion de primer orden 

    revisar la formula . 
    si d es una direccion de descenso valida , entonces debe existir 
    un tamaño de paso suficientemente pepqueño que satisfaga la 
    condicion de disminucion suficiente 
    por lo que se puede comenzar con una tamaño de paso grande 
    y disminuirlo mediante un factor de reduccion constante hasta
    que se cumpla la condicion de suficiencia

    este algoritmo se conoce como busqueda de linea de retroceso 
    debido a la forma en que retrocede a lo largo de la direccion 
    de descenso 
    ...
    La primera condicion es insuficiente para garantizaar 
    la convergencia a un minimo local 
    los tamaños de paso muy pequeños satifaran la primera 
    condicion pero pueden converger prematuramente
    La busqueda de linea de retroceso evita la convergencia 
    prematura al aceptar el tamaño de paso mas satisfactorio
    obtenido mediante la reduccion de escala secuencial
    y se garantiza que convergera a un minimo local
    Otra condicion, llamada de cuvatura requiere que la 
    derivada direccional en la siguiente iteracion para 
    ser mas superficial   

    grad_direccion_d^{k} f(x^{k+1})>=sigma * grad_direccion_d^{k}f(x^{k})
    
    donde sigma controla cuan superficial debe ser la siguiente 
    derivada direccional 
    beta < sigma < 1 
    sigma =0.1 cuando se utiliza con el metodo de newton 
    una alternativa a la condicion de curvatura es la condicion
    de curvatura fuerte 
    que es un criterio mas restrictivo en el sentido 
        | grad_direccond^{k} f(x^{k+1}) <= -sigma grad_direccion d^{k} f(x^{k})
    

    juntas , la condicion de disminucion suficiente  y la condicion 
    de curvatura forman las condiciones de Wolfe 
    la condicion de disminucion suficiente suele ser la 
    segunda condicion de Wolfe 
    la condicion de disminucion suficiente con la condicion de curvatura fuerte 
    forman las condiciones de wolfe fuerte 
    
    Para satisfacer las condiciones de wolfe se requiere de un algoritmo 
    mas complejo
    la busqueda de retroceso fuerte , 
        funciona en dos fases
        la primera la fase de horquillado prueba tamaños depaso 
        sucesivamente mayores para encerrar un intervalo [alpha^{k-1},alpha^{k}] 
        garantizado para contener longitudes de aso que satisfacen 
        las condiciones de wolfe.
        
"""





""""
algunos algoritmos utilizan un factor de paso fijo , los pasos grandes
tienden a generar una convergencia mas rapida
pero corren el riesgo de sobrepasar el minimo
los pasos pequeños tienden a ser mas estables

los pasos mas pequeños suelen ser mas estables pero 
su convergencia es mas lenta
En ocasiones un factor alpha constante se denomina 
tasa de aprendizaje 

otro metodo es usar un factor de paso decreciente
alpha^{k} = alpha^{1} gamma ^{k -1 }   gamma pertenece (0,1]

los factores de paso decrecientes son especialmente populares 
cuando se minimizan funciones objetivos ruidosas  y se usan comunmente
en aplicaciones de aprendizaje automatico

"""