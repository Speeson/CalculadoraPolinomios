from math import *
import sympy as sp
from sympy.plotting import plot

def PolTaylor():
    """
    Genera el polinomio de Taylor solicitando los parámetros al usuario.
    """
    x = sp.symbols('x')  # Definimos la variable X
    
    # Solicitar los parámetros al usuario
    print("\n--- Generador de Polinomio de Taylor ---")
    func_str = input('Introduzca la función (en términos de x - Ej. ln(x), cos(x), exp(x)): ')
    a = float(input('Introduzca el valor en torno a qué punto desea el polinomio (Eje X): '))
    n = int(input('Introduzca el orden del polinomio de Taylor: '))

    # Convertir la entrada de la función a formato simbólico
    f = sp.sympify(func_str)
    F = f  # Copia de la función original

    # Construcción del polinomio de Taylor
    T = f.subs(x, a)  # Término independiente
    for k in range(1, n + 1):
        dfk = sp.diff(f, x)  # Derivada k-ésima
        T += dfk.subs(x, a) * ((x - a) ** k) / factorial(k)  # Término del polinomio
        f = dfk  # Actualizamos la función para la siguiente derivada

    print("\nPolinomio de Taylor:")
    print(sp.expand(T))  # Expande el polinomio para mostrarlo en su forma estándar

    # Mostrar la función original y el polinomio de Taylor en una gráfica
    g = plot(F, T, (x, a - 5, a + 5), title='Polinomio de Taylor (Función en rojo)', show=False)
    g[0].line_color = 'g'  # Color verde para la función original
    g[1].line_color = 'r'  # Color rojo para el polinomio de Taylor
    g.show()

# Este bloque asegura que no se ejecute nada al importar
if __name__ == "__main__":
    PolTaylor()