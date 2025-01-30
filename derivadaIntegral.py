from sympy import symbols, diff, integrate

def derivadaIntegral():
    # Definir la variable simbólica
    x = symbols('x')

    # Definir el polinomio
    p = x**3 - 6*x**2 + 11*x - 6

    # Mostrar el polinomio original
    print(f"Polinomio original: {p}")

    # Calcular la derivada del polinomio
    derivada = diff(p, x)
    print(f"Derivada del polinomio: {derivada}")

    # Calcular la integral del polinomio
    integral = integrate(p, x)
    print(f"Integral del polinomio (indefinida): {integral} + C")

if __name__ == "__main__":
    derivadaIntegral()