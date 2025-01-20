from math import *
import sympy as sp
from sympy.plotting import plot

def PolTaylor(a, n):
    x = sp.symbols('x') # Definimos la variable X
    f = sp.cos(x)
    F = f # copia de la función
    T = f.subs(x, a) # Término independiente
    for k in range  (1, n+1):
        dfk= sp.diff (f, x)
        T = T+dfk.subs(x, a)*((x-a)**k)/factorial(k)
        f = dfk

    print (sp.expand(T))
    g=plot(F, T, (x, a-3, a+3),tittle = 'Polinomio de Taylor', show=False)
    g[0].line_color='k'
    g[1].line_color='r'
    g.show()

a=float(input('Introduzca el valor en torno a qué punto desea el polinomio: '))
n=int(input('Introduzca el order del polinomio de Taylor: '))
PolTaylor(a, n)
