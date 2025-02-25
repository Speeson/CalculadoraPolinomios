import matplotlib.pyplot as plt 
from sympy import symbols, diff, integrate, sympify

def derivadaIntegral():
    # Definir la variable simbólica
    x = symbols('x')

    # Pedir al usuario que introduzca el polinomio
    polinomio_str = input("Introduce el polinomio en términos de x (ejemplo: x**3 - 6*x**2 + 11*x - 6): ")
    p = sympify(polinomio_str)  # Convierte la cadena en un objeto simbólico

    # Mostrar el polinomio original
    print(f"\nPolinomio original: {p}")

    # Calcular la derivada del polinomio
    derivada = diff(p, x)
    print(f"Derivada del polinomio: {derivada}")

    # Calcular la integral del polinomio
    integral = integrate(p, x)
    print(f"Integral del polinomio (indefinida): {integral} + C")

if __name__ == "__main__":
    derivadaIntegral()
