from math import *
import sympy as sp
import matplotlib.pyplot as plt  # Usamos matplotlib para personalizar los gráficos
import numpy as np  # Para generar datos numéricos para las gráficas

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

    # Crear puntos para graficar la función original y el polinomio
    func_lambda = sp.lambdify(x, F, 'numpy')  # Función original
    taylor_lambda = sp.lambdify(x, T, 'numpy')  # Polinomio de Taylor

    # Rango de valores alrededor del punto `a`
    x_vals = np.linspace(a - 3, a + 3, 400)
    y_func = func_lambda(x_vals)
    y_taylor = taylor_lambda(x_vals)

    # Generar el gráfico con Matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_func, label='Función Original', color='green', linestyle='-', linewidth=2)
    plt.plot(x_vals, y_taylor, label=f'Polinomio de Taylor (Orden {n})', color='red', linestyle='--', linewidth=2)
    
    # Añadir etiquetas y leyenda
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.title('Aproximación con el Polinomio de Taylor', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('f(x)', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True)
    
    # Mostrar el gráfico
    plt.show()

# Este bloque asegura que no se ejecute nada al importar
if __name__ == "__main__":
    PolTaylor()