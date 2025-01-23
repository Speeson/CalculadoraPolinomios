import numpy as np
from sympy import symbols, solve

def raices():
    # Solicita los coeficientes del polinomio al usuario
    print("Vamos a calcular las raíces de un polinomio.")
    print("El polinomio debe estar en la forma a*x**n + b*x**(n-1) + ... + c = 0")
    
    grado = int(input("Introduce el grado del polinomio (n): "))
    coeficientes = []

    for i in range(grado, -1, -1):
        coef = float(input(f"Introduce el coeficiente de x^{i}: "))
        coeficientes.append(coef)

    # Define la variable simbólica
    x = symbols('x')

    # Construye el polinomio simbólicamente
    polinomio = sum(coeficientes[i] * x**(grado - i) for i in range(len(coeficientes)))

    # Encuentra las raíces simbólicas
    raices_simbolicas = solve(polinomio, x)

    # Muestra las raíces simbólicas
    print(f"Polinomio: {polinomio}")
    print(f"Raíces simbólicas: {raices_simbolicas}")

    # Encuentra las raíces numéricas usando NumPy
    raices_numericas = np.roots(coeficientes)

    # Muestra las raíces numéricas
    print(f"Raíces numéricas (aproximadas): {raices_numericas}")

if __name__ == "__main__":
    raices()
