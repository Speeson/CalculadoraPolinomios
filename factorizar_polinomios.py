from sympy import symbols, factor

# Definir la variable simbólica
x = symbols('x')

# Definir el polinomio
polinomio = x**3 - 6*x**2 + 11*x - 6

# Factorizar el polinomio
factores_polinomio = factor(polinomio)

# Mostrar el polinomio original
print(f"Polinomio original: {polinomio}")

# Mostrar la factorización
print(f"Factorización del polinomio: {factores_polinomio}")




