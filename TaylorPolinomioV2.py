from math import *
import sympy as sp
from sympy.plotting import plot

def PolTaylor(a, n, func_str):
    x = sp.symbols('x')  # Definimos la variable X
    f = sp.sympify(func_str)  # Convertimos la entrada de texto en una función simbólica
    F = f  # Copia de la función original
    T = f.subs(x, a)  # Término independiente
    for k in range(1, n + 1):
        dfk = sp.diff(f, x)  # Derivada k-ésima
        T += dfk.subs(x, a) * ((x - a) ** k) / factorial(k)  # Término del polinomio
        f = dfk  # Actualizamos la función para la siguiente derivada

    print("\nPolinomio de Taylor:")
    print(sp.expand(T))  # Expande el polinomio para mostrarlo en su forma estándar

    # Graficamos la función original y el polinomio de Taylor
    g = plot(F, T, (x, a - 3, a + 3), title='Polinomio de Taylor', show=False)
    g[0].line_color = 'k'  # Color negro para la función original
    g[1].line_color = 'r'  # Color rojo para el polinomio de Taylor
    g.show()

# Este bloque asegura que no se ejecute nada al importar
if __name__ == "__main__":
    print("Este archivo está diseñado para ser importado como módulo.")